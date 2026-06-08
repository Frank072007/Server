import socket
import threading #threading is a way of creating multiple threads in one python program. A thread allows us to spread code out so its not waiting for another code to finish before it can execute

HEADER = 64
PORT = 5050
#SERVER = '192.168.56.1' bottom does it the same
SERVER = socket.gethostbyname(socket.gethostname()) #this gets your local ip address automatically for you
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) # this binds the socket to the address and port thaat is passed in, in this case, ADDR. Anything comes to both that address and port would hit that socket

def handle_client(conn, addr):     # this handles the actual communication with the client and the server
    print(f'[NEW CONNECTIONS] {addr} connected')
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # this is a blocking line of code, nothing else would run until a message is gotten, this is a thread so other threads would run
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f'[{addr}], {msg}')
            conn.send('Msg received'.encode(FORMAT))
    
    conn.close()




def start():    # this function handles the acceptance and distribution of connections to the server
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()# blocking line of code. it waits for other clients
        thread = threading.Thread(target = handle_client, args=(conn, addr)) # this creates a new thread for each client that connect, the thread doesnt start yet. the target is the function thatll run in the thread and the args are the arguments thatll be passed into the target function
        thread.start() # this starts the thread
        print()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}') # the -1 is because the main thread is also counted so we have to remove it

print('[STARTING] server is starting...')
start()
