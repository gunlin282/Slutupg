from appJar import gui
from user_input import get_recipe_input_from_user
from user_input import get_storage_input_from_user
from threading import Thread
import socket
import pickle

buffer_size = 1024
recipe_pack = []
storage_pack = []

def Main():
    while True:

        # data received from server
        data = s.recv(buffer_size)
        data2 = pickle.loads(data)
        if len(data) < 1:
            print('output complete')
            break
        elif data2 == "quit":
            print("connection closed")
            s.close()
            return False
        else:
            output_from_server(data)


def thread():
    myThread = Thread(target=Main)
    myThread.start()


def output_from_server(data):
    server_output = pickle.loads(data)
    print(server_output)



def call_storage_list(button):
    message = "list_storage"
    message = pickle.dumps(message)
    s.send(message)



def call_recipe_list(button):
    message = "list_recipe"
    message = pickle.dumps(message)
    s.send(message)



def call_shopping_list(button):
    message = "list_shopping"
    message = pickle.dumps(message)
    s.send(message)



def call_to_storage(button):
    if button == "Lägg till varor":
        storage_input = get_storage_input_from_user()
        storage_pack.append("s")
        storage_pack.append(storage_input)
        storage_send = pickle.dumps(storage_pack)
        s.send(storage_send)



def call_to_recipe(button):
    if button == "Lägg till recept":
        recipe_input = get_recipe_input_from_user()
        recipe_pack.append("r")
        recipe_pack.append(recipe_input)
        recipe_send = pickle.dumps(recipe_pack)
        s.send(recipe_send)

def call_close(button):
    message = "quit"
    msg = pickle.dumps(message)
    s.send(msg)
    app.stop()


# har inte definerat klart functionerna men vill ha kvar layouten på gui så därav en pass på funtionen
def call_dinner_tip(button):
    pass

def call_value():
    pass


app = gui()


def my_gui():


    app.thread(thread)
    app.setSize(600, 400)
    app.setResizable(canResize=False)
    app.startFrame("LEFT", row=0, column=0, rowspan=0, colspan=0)
    app.setFont(size=15, family="Arial Black", weight="normal")
    app.addButton("Lista varor", call_storage_list, row=1, column=0)
    app.addButton("Receptlista", call_recipe_list, row=1, column=1)
    app.addButton("Middagstips", call_dinner_tip, row=1, column=2)
    app.addButton("Handlingslista", call_shopping_list, row=4, colspan=3)
    app.addButton("Lägg till varor", call_to_storage, row=2, colspan=2)
    app.addButton("Lägg till recept", call_to_recipe, row=3, colspan=2)
    app.addButton("Ta bort recept", call_value, row=3, column=2)
    app.addButton("Avsluta", call_close, row=2, column=2)
    app.stopFrame()
    app.go()



if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "172.20.201.214"
    port = 12345
    s.connect((host, port))
    my_gui()
