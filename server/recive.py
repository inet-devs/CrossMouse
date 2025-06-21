# server.py
import socket
import pyautogui
import time
HOST = '0.0.0.0'
PORT = 2025
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

try:
    while True:
        time.sleep(1)
        data = conn.recv(1024)
        if not data:
            break
        x_str, y_str = data.decode().split(",")
        x = int(x_str)
        y = int(y_str)
        print(f"Mouse Position Received: X={x}, Y={y}")
        pyautogui.moveTo(x, y)
except KeyboardInterrupt:
    print("Server shutting down.")

conn.close()
server_socket.close()
