using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace FutureAndCallbacks;

using System; 
using System.Threading.Tasks;

public static class TasksMechanism
{
    // sealed prevent this class from being inherited, so it belong only to the TasksMechanism class
    private sealed class State(Socket clientSocket)
    {
        // the port and the host of the server
        public const int Port = 80; 
        public const string Host = "www.test.com";

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
        // getting the IPAdress from the dns
        IPHostEntry ipHostEntry = Dns.GetHostEntry(State.Host);
        
        // getting the first ip address from the host entry
        IPAddress ipAddress = ipHostEntry.AddressList[0];
        
        // creating new TCP socket
        var socket = new Socket(SocketType.Stream, ProtocolType.Tcp);

        // binding the ipAddress and the port
        var endPoint = new IPEndPoint(ipAddress, State.Port);
        
        // creating the state
        var state = new State(socket);
        
        // the using statement ensure the socket is disposed even if an error occur   
        using (socket)
        {
            Task<Socket> futureConnect = ConnectTask(socket, endPoint);
            futureConnect.ContinueWith((Task<Socket> connectTask) =>
            {
                if (connectTask.IsCompletedSuccessfully)
                {
                    Console.WriteLine("Connection succeeded!");
                    Task<Socket> futureSend = SendTask(connectTask.Result);
                    futureSend.ContinueWith((Task<Socket> sendTask) =>
                    {
                        if (sendTask.IsCompletedSuccessfully)
                        {
                            ReceiveTask(state);
                                                        
                        } else if (sendTask.IsFaulted)
                        {
                            Console.WriteLine($"Sending the request failed: {sendTask.Exception}");
                        }

                    });
                }
                else if (connectTask.IsFaulted)
                {
                    Console.WriteLine($"Connection failed: {connectTask.Exception}");
                }
            });

            state.ReceiveDone.WaitOne();
        }
        
        // socket and state.Socket are the same since state holds a reference of the socket     
        state.Socket.Close();
    }
    
    // The endpoint is used only to establish the connection with the server through the socket
    private static Task<Socket> ConnectTask(Socket socket, IPEndPoint endPoint)
    {
        // create a promise that will be resolved when the connection is made
        var promise = new TaskCompletionSource<Socket>();
        // starting a task that tries to connect a socket to the endpoint of the server 
        socket.BeginConnect(endPoint, (asyncResult) =>
        {
            try
            {
                // see if the connection was successful 
                socket.EndConnect(asyncResult);
                // if so, set the socket as the result of the promise
                promise.SetResult(socket);
            } catch (Exception ex) {
                promise.SetException(ex);
            }
        }, null);
        return promise.Task;
    }

    private static Task<Socket> SendTask(Socket socket)
    {
        var promise = new TaskCompletionSource<Socket>();
        var requestText = $"GET /documente-utile/ HTTP/1.1\r\nHost: {State.Host}\r\n\r\n";
        var requestBytes = Encoding.UTF8.GetBytes(requestText);
        socket.BeginSend(requestBytes, 0, requestBytes.Length, SocketFlags.None, asyncResult =>
        {
            try
            {
                socket.EndSend(asyncResult);
                promise.SetResult(socket);
            }
            catch (Exception ex)
            {
                promise.SetException(ex);
            }
        }, null);
        return promise.Task;
    }
    
    
    
    private static Task<Socket> ReceiveTask(State state)
    {
        var promise = new TaskCompletionSource<Socket>();

        void Receive()
        {
            state.Socket.BeginReceive(state.Buffer, 0, State.BufferLength, SocketFlags.None, asyncResult =>
            {
                try
                {
                    var bytesReceived = state.Socket.EndReceive(asyncResult);
                    if (bytesReceived == 0)
                    {
                        // there are no more bytes to be received
                        Console.WriteLine(state.Content.ToString());
                        Console.WriteLine("All the data has been received!");
                        promise.SetResult(state.Socket);
                        state.ReceiveDone.Set();
                    }
                    else
                    {
                        var receivedText = Encoding.UTF8.GetString(state.Buffer, 0, bytesReceived);
                        state.Content.Append(receivedText);
                        Receive(); // recursive call to read more data
                    }
                }
                catch (Exception ex)
                {
                    promise.SetException(ex);
                }
            }, null);
        }
        
        Receive(); // start the receiving process 
        return promise.Task;
    }
}