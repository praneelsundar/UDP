import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))
    print("Server is listening...")

    while True:
        data, addr = sock.recvfrom(1024)
        print("Received:", data.decode(), "from", addr)
        sock.sendto(data, addr)  # Echo back

server()
