from appJar import gui
from user_input import get_recipe_input_from_user
from user_input import get_storage_input_from_user
from format import sort_lists
from threading import Thread
from recipe import *
import socket
import pickle

buffer_size = 1024
recipe_pack = []
storage_pack = []

def Main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    s.connect((host, port))
    my_gui()

    while True:

        storage_send = pickle.dumps(storage_pack)
        s.send(storage_send)

        recipe_send = pickle.dumps(recipe_pack)
        s.send(recipe_send)

        print("varor inlagda")
        s.close()



def sent_input():
    pass

def call_storage_list(button):
    storage_list = current_ingredient()
    if button == "Lista varor":
        for item in storage_list:
            print(item)
            app.stop()


def call_recipe_list(button):
    if button == "Receptlista":
        recipe_list = current_recipe_name()
        recipe_list = sort_lists(recipe_list)
        for item in recipe_list:
            item = (item.rstrip().replace("{", "").replace('"', '').replace(":", ""))
            print(item)
            app.stop()


def call_shopping_list(button):
    if button == "Handlingslista":
        shopping_list = current_shop_list()
        for item in shopping_list:
            print(item)
            app.stop()


def call_to_storage(button):
    if button == "Lägg till varor":
        storage_input = get_storage_input_from_user()
        storage_pack.append(storage_input)
    app.stop()


def call_to_recipe(button):
    if button == "Lägg till recept":
        recipe_input = get_recipe_input_from_user()
        recipe_pack.append(recipe_input)

    app.stop()

 # har inte definerat klart functionerna men vill ha kvar layouten på gui så därav en pass på funtionen
def call_dinner_tip(button):
    pass

# har inte definerat klart functionerna men vill ha kvar layouten på gui så därav en pass på funtionen
def call_value(button):
    pass


app = gui()

def my_gui():

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
    app.addButton("Ta bort varor", call_value, row=2, column=2)
    app.stopFrame()

    app.go()

if __name__ == "__main__":
    Main()


