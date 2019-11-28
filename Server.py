import socket
from threading import Thread
import json
import pickle


buffer_size = 1024
clients = {}

def threaded(conn):
    while True:

            # data received from client
        data = conn.recv(buffer_size)
        data2 = pickle.loads(data)
        if len(data) < 1:
            print('input complete')
            break
        elif data2 == "quit":
            message = "quit"
            msg = pickle.dumps(message)
            conn.send(msg)
            user_left()
            print("user left")
            return False
        else:
            input_output_with_client(data)


def user_left():
    message = "User left"
    msg = pickle.dumps(message)
    for client in clients:
        client.send(msg)


def input_output_with_client(data):
    client_input = pickle.loads(data)
    print(client_input)

    if client_input[0] == "s":
        storage_input = client_input
        with open('Storage_list.txt', 'a', ) as storage_append:
            json.dump(storage_input[1:], storage_append, ensure_ascii=False)
            storage_append.write('\n')
            message = "Varor inlagda"
            msg = pickle.dumps(message)
            for client in clients:
                client.send(msg)

    elif client_input[0] == "r":
        recipe_input = client_input
        with open('Recipe_list.txt', 'a', ) as recipe_append:
            json.dump(recipe_input[1:], recipe_append, ensure_ascii=False)
            recipe_append.write('\n')
            message = "Recept inlagt"
            msg = pickle.dumps(message)
            for client in clients:
                client.send(msg)

    elif client_input == "list_storage":
        storage_list = current_ingredient()
        storage_send = pickle.dumps(storage_list)
        conn.send(storage_send)

    elif client_input == "list_recipe":
        recipe_list = current_recipe_name()
        recipe_send = pickle.dumps(recipe_list)
        conn.send(recipe_send)

    elif client_input == "list_shopping":
        shopping_list = current_shop_list()
        shopping_send = pickle.dumps(shopping_list)
        conn.send(shopping_send)


def current_recipe_name():
    my_recipe = []
    recipe = open("Recipe_list.txt", "r")
    for lines in recipe:
        first_word = lines.split()[0]
        my_recipe.append(first_word)
    return my_recipe

def current_ingredient():
    ingredient_list = []
    with open("Storage_list.txt", "r") as file:
        reader = file.readlines()
        for item in reader:
            ingredient_list.append(item.rstrip("\n",))
    return ingredient_list

def current_shop_list():
    shopping_list = []
    with open('Shop_list.txt', 'r')as file:
        reader = file.readlines()
        for item in reader:
            shopping_list.append(item.rstrip("\n"))
    return shopping_list


if __name__ == '__main__':
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")
    while True:
        conn, addr = s.accept()
        clients[conn] = addr


        print('Connected to :', addr[0], ':', addr[1])

        myThread = Thread(target=threaded, args=(conn, ))
        myThread.start()
