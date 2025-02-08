# UDP File Transfer using RDT 1.0

## Submitted Files:
1. udp_file_sender.py - GUI-based file sender
2. udp_file_receiver.py - GUI-based file receiver
3. ReadMe.txt - Instructions for running the program
4. image.bmp - Sample transfer file 

## Setup Requirements:
- Install Python 3.x
- No additional libraries needed (uses built-in Tkinter and socket)

## How to Run:
1. **Start the Receiver**:
   - Open a terminal and run: `python udp_file_receiver.py`
   - Click "Start Receiver"

2. **Start the Sender**:
   - Open another terminal and run: `python udp_file_sender.py`
   - Click "Select BMP File & Send"
   - Choose `image.bmp` and click Open

## Expected Output:
- The receiver should display **"File received and saved."**
- The transferred image should match the original.

## Notes:
- This implementation follows **RDT 1.0**, assuming a **perfectly reliable channel**.
