using System.Net;
using System.Net.Sockets;
using System.Runtime.InteropServices.JavaScript;
using System.Text;
using System.Threading.Tasks.Dataflow;

namespace FutureAndCallbacks;

public static class AsyncAwaitMechanism
{
    // sealed prevent this class from being inherited, so it belong only to the TasksMechanism class
    private sealed class State(Socket clientSocket)
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

    public static async Task Start()
    {
        Console.WriteLine("AsyncAwaitMechanism Start()");
        // Get the ipAddress of the host
        IPHostEntry ipHostEntry = Dns.GetHostEntry(State.Host);
        
        // Get the first ip Address of the host
        IPAddress ipAddress = ipHostEntry.AddressList[0];
        
        // create the tcp socket
        var socket = new Socket(SocketType.Stream, ProtocolType.Tcp);
        
        // bind the ipAddress and the port for the endpoint
        IPEndPoint ipEndPoint = new IPEndPoint(ipAddress, State.Port);
        
        // Initializing the state with the socket
        var state = new State(socket);

        using (socket)
        {
            await ConnectAsync(socket, ipEndPoint);
            await SendAsync(socket);
            await ReceiveAsync(state);

        }
        state.ReceiveDone.WaitOne();
        socket.Close();
    }

    private static Task<Socket> ConnectAsync(Socket socket, IPEndPoint endPoint)
    {
        Console.WriteLine("ConnectAsync called!");
        var promise = new TaskCompletionSource<Socket>();
        socket.BeginConnect(endPoint, ar =>
        {
            try
            {
                socket.EndConnect(ar);
                promise.SetResult(socket);
                Console.WriteLine("Connect succeeded!");
            }
            catch (Exception ex)
            {   
                promise.SetException(ex);
                Console.WriteLine($"Connect failed with exception: {ex}");
            }
        }, null);
        return promise.Task;
    }

    private static Task<Socket> SendAsync(Socket socket)
    {
        Console.WriteLine("SendAsync called!");
        var promise = new TaskCompletionSource<Socket>();
        var requestText = $"GET /documente-utile/ HTTP/1.1\r\nHost: {State.Host}\r\n\r\n";
        var requestBytes = Encoding.UTF8.GetBytes(requestText);
        socket.BeginSend(requestBytes, 0, requestBytes.Length, SocketFlags.None, ar =>
        {
            try
            {
                socket.EndSend(ar);
                Console.WriteLine("Request succesfully send!");
                promise.SetResult(socket);
            }
            catch (Exception ex)
            {
                promise.SetException(ex);
                Console.WriteLine($"Send exception: {ex}");
            }
        }, null);
        return promise.Task;
    }

    private static Task<Socket> ReceiveAsync(State state)
    {   
        Console.WriteLine("ReceiveAsync called!");
        var promise = new TaskCompletionSource<Socket>();
        
        void Receive()
        {
            Console.WriteLine("Receive called!");
            state.Socket.BeginReceive(state.Buffer, 0, State.BufferLength, SocketFlags.None, ar =>
            {
                try
                {
                    var receivedBytes = state.Socket.EndReceive(ar);
                    if (receivedBytes == 0)
                    {
                        Console.WriteLine(state.Content.ToString());
                        Console.WriteLine("Received all data from the server!");
                        promise.SetResult(state.Socket);
                        state.ReceiveDone.Set();
                    }
                    else
                    {
                        var receivedText = Encoding.UTF8.GetString(state.Buffer, 0, receivedBytes);
                        Console.WriteLine($"Received {receivedBytes} bytes");
                        state.Content.Append(receivedText);
                        
                        Receive(); // recursive call
                    }
                }
                catch (Exception ex)
                {
                    promise.SetException(ex);
                }
            }, null);
        }
        Receive(); // Initial call of the Receive
        
        return promise.Task;
    }
}