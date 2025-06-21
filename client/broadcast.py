import socket
import time
from pynput.mouse import Controller

mouse = Controller()
print("IP:")
SERVER_IP = input()'  # Replace with your server (Windows) IP
PORT = 2025

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    last_pos = None
    while True:
        pos = mouse.position
        if pos != last_pos:
            message = f"{pos[0]},{pos[1]}"
            sock.sendto(message.encode(), (SERVER_IP, PORT))
            print("Sent:", message)
            last_pos = pos
        time.sleep(0.05)  # adjust as needed
except KeyboardInterrupt:
    print("UDP client stopped.")
finally:
    sock.close()
