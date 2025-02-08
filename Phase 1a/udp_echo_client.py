import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "HELLO"
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
    print("Sent:", message)

    data, _ = sock.recvfrom(1024)
    print("Received:", data.decode())

client()
