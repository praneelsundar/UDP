import socket
import tkinter as tk

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
PACKET_SIZE = 1024  # Fixed packet size

def extract(packet):
    """Extracts data from the received packet (trivial in RDT 1.0)."""
    return packet 

def deliver_data(data):
    """Writes the extracted data to a file."""
    with open("received_image.bmp", "wb") as file:
        file.write(data)

def rdt_rcv():
    """Receives packets and assembles them in order."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((SERVER_IP, SERVER_PORT))

    status_label.config(text="Listening for incoming file...", fg="blue")
    root.update_idletasks()

    received_data = bytearray()

    while True:
        packet, addr = sock.recvfrom(PACKET_SIZE)
        if packet == b"END":
            break
        received_data.extend(extract(packet))  

    deliver_data(received_data)  

    status_label.config(text="File received and saved.", fg="green")
    sock.close()

# GUI Setup
root = tk.Tk()
root.title("UDP File Receiver")

button = tk.Button(root, text="Start Receiver", command=rdt_rcv, padx=20, pady=10)
button.pack(pady=20)

status_label = tk.Label(root, text="Click to start listening...", fg="blue")
status_label.pack()

root.mainloop()
