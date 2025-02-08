import socket
import tkinter as tk
from tkinter import filedialog

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345
PACKET_SIZE = 1024  # Fixed packet size

def make_pkt(file_path):

    packets = []
    with open(file_path, "rb") as file:
        while chunk := file.read(PACKET_SIZE):
            packets.append(chunk)
    return packets

def udt_send(sock, packet):
    sock.sendto(packet, (SERVER_IP, SERVER_PORT))

def rdt_send():
    file_path = filedialog.askopenfilename(title="Select BMP File", filetypes=[("BMP files", "*.bmp")])
    
    if not file_path:
        status_label.config(text="No file selected!", fg="red")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    packets = make_pkt(file_path)

    for i, packet in enumerate(packets):
        udt_send(sock, packet)
        status_label.config(text=f"Sending packet {i+1}/{len(packets)}")
        root.update_idletasks()

    # End of file transmission
    udt_send(sock, b"END")
    status_label.config(text="File sent successfully!", fg="green")

    sock.close()

# GUI Setup
root = tk.Tk()
root.title("UDP File Sender")

button = tk.Button(root, text="Select BMP File & Send", command=rdt_send, padx=20, pady=10)
button.pack(pady=20)

status_label = tk.Label(root, text="Waiting for file selection...", fg="blue")
status_label.pack()

root.mainloop()
