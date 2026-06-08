import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) # encoding only works on strings thats why we convert it into a string first
    send_length += b' ' * (HEADER - len(send_length)) # this pads the send_length with blank spaces till it reaches the header size. The padding is necessary because tcp is a stream protocol, it doesnt know where the message ends and the next one starts, it just reads up to the header size irrespective of the actual message length
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('Hello world')
input()
send('Hello everyone')
input()
send('Hello again')
send(DISCONNECT_MESSAGE)