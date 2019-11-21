import socket
from _thread import *
import threading
import json
import pickle

print_lock = threading.Lock()
buffer_size = 1024

def threaded(conn):
    while True:

        # data received from client
        data = conn.recv(buffer_size)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break
    conn.close()

def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        conn, addr = s.accept()

        # lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (conn,))
        s.close()

if __name__ == '__main__':
    Main()



def input_from_client(conn, buffer_size):
    client_input = conn.recv(buffer_size)
    client_input = pickle.loads(client_input)
    print(client_input)

    if client_input == "storage":
        storage_input = client_input
        with open('Storage_list.txt', 'a', ) as storage_append:
            json.dump(storage_input, storage_append, ensure_ascii=False)
            storage_append.write('\n')

    elif client_input == "recipe":
        recipe_input = client_input
        with open('Recipe_list.txt', 'a', ) as recipe_append:
            json.dump(recipe_input, recipe_append, ensure_ascii=False)
            recipe_append.write('\n')


def output_to_client():
    pass