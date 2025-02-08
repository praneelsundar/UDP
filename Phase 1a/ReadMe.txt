Requirements:

Python 3.x installed
No external dependencies (uses built-in socket module)

Execution Steps:

Step 1: Start the UDP Echo Server
->Open a terminal or command prompt.
->Navigate to the directory where udp_echo_server.py is saved.
->Run the server using the following command:
   python udp_echo_server.py
->The server will start and wait for incoming messages.

Step 2: Start the UDP Echo Client
->Open another terminal or command prompt.
->Navigate to the directory where udp_echo_client.py is saved.
->Run the client using the following command:
->python udp_echo_client.py

The server will echo back the message, and it will be displayed on the client.

Expected Output:

On the Server Terminal:

Server is listening.....
Received: HELLO from('127.0.0.1', ******)

On the Client Terminal:

Sent: HELLO
Received: HELLO

Notes:

->This implementation follows basic UDP communication, where the server listens indefinitely, and the client sends one message at a time.
->Ensure that both the client and server use the same IP address and port number.
->The server must be started first before running the client.