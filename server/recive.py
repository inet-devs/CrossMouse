import socket
from pynput.mouse import Controller

mouse = Controller()

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2025

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"UDP server listening on {HOST}:{PORT}")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        x_str, y_str = data.decode().split(',')
        x = float(x_str)
        y = float(y_str)
        mouse.position = (x, y)
        print(f"Moved mouse to: X={x}, Y={y}")
except KeyboardInterrupt:
    print("UDP server shutting down.")
finally:
    sock.close()
