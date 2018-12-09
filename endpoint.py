import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('127.0.0.1', 8018))
print("Bound...")
# sock.listen(1)
sock.settimeout(1)
message = {
    'message_type': 'manual',
    'ab': 90,
    'bc': 0,
    'cd': 0,
    'de': 0
}

sock.sendall(json.dumps(message).encode())

sock.close()