# UDP File Transfer using RDT 1.0

Title and Authors
-Project Name: UDP-Based File Transfer System
-Phase:  Phase 1B
-Author: Praneel Sundar

Environment
-Operating System: Windows, Linux, MacOS (Compatible)
-Programming Language: Python
-Python Version: 3.x
-Libraries Used: Built-in `socket` and `tkinter` (No external dependencies)

Submitted Files
1.udp_file_sender.py- GUI-based file sender
2.udp_file_receiver.py- GUI-based file receiver
3.ReadMe.txt- Instructions for running the program
4.image.bmp- Sample file for transfer

Setup Requirements
-Install Python 3.x (if not already installed)
-No additional libraries are required since `tkinter` and `socket` are built-in

Instructions
How to Run
1. Start the Receiver:
- Open a terminal and navigate to the project directory.
- Run the following command:
	"python udp_file_receiver.py"
- Click on "Start Receiver"in the GUI.

2. Start the Sender:
- Open another terminal and navigate to the project directory.
- Run the following command:
       "python udp_file_sender.py"
- Click "Select BMP File & Send"in the GUI.
- Choose `image.bmp` and click Open.

Expected Output
- The receiver should display:
  "File received and saved."
- The transferred image should match the original `image.bmp`.

Notes
- This implementation follows **RDT 1.0**, assuming a **perfectly reliable channel**.
- No error checking or retransmission mechanisms are included, as per the RDT 1.0 model.





