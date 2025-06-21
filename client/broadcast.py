import socket
import time
from pynput.mouse import Controller

mouse = Controller()
print('enter ip:')
HOST = input()  # Replace with the server's IP address
PORT = 2025

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        time.sleep(1)
        curloc = mouse.position
        message = f"{curloc[0]},{curloc[1]}"  # convert tuple to "x,y" string
        client_socket.sendall(message.encode())
        print("Sent:", message)
except KeyboardInterrupt:
    print("Client stopping.")

client_socket.close()
