using System.Net;
using System.Net.Sockets;
using System.Threading;
using System.Text;

namespace FutureAndCallbacks;

public static class DirectCallbacks
{
    private class State(Socket clientSocket)
    {
        // the port and the host of the server
        public const int Port = 80; 
        public const string Host = "www.cnatdcu.ro";

        // the buffer where the data will be stored
        public const int BufferLength = 2048;
        public readonly byte[] Buffer = new byte[BufferLength];
        
        // the socket that will be used for connection with the server
        public Socket Socket { get; } = clientSocket;

        public readonly StringBuilder Content = new();

        public readonly ManualResetEvent ReceiveDone = new(false);
    }

    public static void Start()
    {   
        // Get the ip address of the host
        IPHostEntry ipHostInfo = Dns.GetHostEntry(State.Host);
        
        // Get the first IP_Address associated with the host
        IPAddress ipAddress = ipHostInfo.AddressList[0];
        
        // Create a socket and connect to the server
        var socket = new Socket(SocketType.Stream, ProtocolType.Tcp);
        
        // Bind the IPAddress with the port 
        var remoteEndPoint = new IPEndPoint(ipAddress, State.Port);
        
        // Create the state bound to the socket
        var state = new State(socket);
        
        // Connect to the server
        socket.BeginConnect(remoteEndPoint, ConnectCallback, state);
        Console.WriteLine("socket.BeginConnect called");
        
        // closing the connection with the server
        state.ReceiveDone.WaitOne();
        state.Socket.Close();
    }

    /// <summary>
    /// The function that is called after the connection have been made
    /// </summary>
    private static void ConnectCallback(IAsyncResult asyncResult)
    {
        // The asyncResult is the state passed into the BeginConnect
        var state = asyncResult.AsyncState as State ??
                    throw new InvalidOperationException("AsyncResult is null or is not of type state!");
        
        // Completes the asynchronous connection attempt initiated by Socket.BeginConnect
        state.Socket.EndConnect(asyncResult);
        
        // Sending the request to the server
        var requestText = $"GET /documente-utile/ HTTP/1.1\r\nHost: {State.Host}\r\n\r\n";
        // convert the request text into bytes
        var requestBytes = Encoding.UTF8.GetBytes(requestText);
        
        // Start sending the request to the server
        state.Socket.BeginSend(
            requestBytes,
            0,
            requestBytes.Length,
            SocketFlags.None,
            SendCallback,
            state
        );
        Console.WriteLine("socket.BeginSend called");
    }


    public static void SendCallback(IAsyncResult asyncResult)
    {
        // The AsyncResult is the state passed by to BeginSend
        var state = asyncResult.AsyncState as State ??
                    throw new InvalidOperationException("The asnycResult is null or is not of type State");

        var bytesSent = state.Socket.EndSend(asyncResult);
        
        // I think that this is no needed because the EndState does throw exceptions if there are some errors
        if (bytesSent == 0)
        {
            throw new Exception("There was an error sending the request to the server!");
        }
        
        // start the receiving process
        state.Socket.BeginReceive(
            state.Buffer,
            0,
            State.BufferLength,
            SocketFlags.None,
            ReceiveCallback,
            state
        );
        Console.WriteLine("socket.BeginReceive called first time");
    }

    public static void ReceiveCallback(IAsyncResult asyncResult)
    {   
        Console.WriteLine("ReceiveCallback called");
        
        // The AsyncResult is the state passed to the BeginReceive
        var state = asyncResult.AsyncState as State ??
                    throw new InvalidOperationException("The asyncResult is null or is not of type State");

        var bytesReceived = state.Socket.EndReceive(asyncResult);
        Console.WriteLine($"Bytes received: {bytesReceived}");

        if (bytesReceived == 0)
        {
            // if there are no more bytes to read, print the content
            Console.WriteLine("No more bytes to read");
            Console.WriteLine(state.Content.ToString());
            state.ReceiveDone.Set();
        }
        else
        {
            var responseText = Encoding.UTF8.GetString(state.Buffer, 0, bytesReceived);
            state.Content.Append(responseText);
            Console.WriteLine("Response text appended to content!");
            
            // start another receive callaback
            state.Socket.BeginReceive(
                state.Buffer,
                0,
                State.BufferLength,
                SocketFlags.None,
                ReceiveCallback,
                state
            );
            Console.WriteLine("socket.BeginReceive called again");
        }
    }
}