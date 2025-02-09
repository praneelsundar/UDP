Title and Authors
-Project Name: UDP Echo Communication
-Phase: Phase 1A
-Author: Praneel Sundar

Environment
-Operating System: Windows, Linux, MacOS (Compatible)
-Programming Language: Python
-Python Version: 3.x

Libraries Used: Built-in socket (No external dependencies)

Submitted Files:
-udp_echo_server.py - UDP echo server
-udp_echo_client.py - UDP echo client
-ReadMe.txt - Instructions for running the program

Setup Requirements:
-Install Python 3.x (if not already installed)
-No additional libraries are required since socket is built-in

Instructions
How to Run
1. Start the UDP Echo Server:
-Open a terminal and navigate to the project directory.
-Run the following command:
 python udp_echo_server.py

--The server will start and wait for incoming messages--

The server code is structured as follows:
-Binds to SERVER_IP and SERVER_PORT
-Listens indefinitely for messages
-Echoes received messages back to the sender

2.Start the UDP Echo Client:
-Open another terminal and navigate to the project directory.
-Run the following command:
 python udp_echo_client.py

-The client code:
 Sends a "HELLO" message to the server
 Waits for and prints the echoed response

-Expected Output
 On the Server Terminal:
 The server should display:

 Server is listening.....
 Received: HELLO from('127.0.0.1', ******)

-On the Client Terminal:
 The client should display:
 Sent: HELLO
 Received: HELLO

Notes
This implementation follows basic UDP communication, where the server listens indefinitely, and the client sends one message at a time.
Ensure that both the client and server use the same IP address and port number.
The server must be started first before running the client.