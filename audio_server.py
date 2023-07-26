import socket
import wave
import numpy as np

HOST = "127.0.0.1"  # IP address of the server
PORT = 5000  # Port number of the server

CHUNK = 1024 * 4  # Number of samples per buffer
FORMAT = "int16"  # Audio format
CHANNELS = 1  # Number of channels
RATE = 44100  # Sampling rate

# Create a server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a host and a port
serversocket.bind((HOST, PORT))
# Listen for incoming connections
serversocket.listen(5)
print("Server listening on", HOST, PORT)

# Accept a connection from a client
clientsocket, address = serversocket.accept()
print("Connection from", address)

# Receive audio data from the client and save it
with wave.open("audio.wav", "wb") as wavfile:
    # Set the parameters of the wave file
    wavfile.setparams((CHANNELS, wave.get_sample_size(FORMAT), RATE, 0, "NONE", "NONE"))
    while True:
        data = clientsocket.recv(CHUNK)
        if not data:
            break
        # Convert bytes to numpy array and back to bytes
        array = np.frombuffer(data, dtype=FORMAT)
        data = array.tobytes()
        wavfile.writeframes(data)

print("Audio saved as audio.wav")

# Close the sockets
clientsocket.close()
serversocket.close()
