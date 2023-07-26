import socket

HOST = "127.0.0.1"  # IP address of the server
PORT = 5000  # Port number of the server

CHUNK = 1024 * 4  # Number of samples per buffer

# Create a client socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientsocket.connect((HOST, PORT))

# Send audio data to the server
with open("audio.wav", "rb") as wavfile:
    while True:
        data = wavfile.read(CHUNK)
        if not data:
            break
        clientsocket.sendall(data)

print("Audio sent")

# Close the socket
clientsocket.close()
