from appJar import gui
from recipe import current_ingredient
from recipe import current_recipe_name
from recipe import current_shop_list
from user_input import add_input_from_user_to_storage
from user_input import add_input_from_recipe_from_user
from recipe import dinner_tip
from format import clear_shop_list
from format import sort_lists


def call_storage_list(button):
    storage_list = current_ingredient()
    if button == "Lista varor":
        for item in storage_list:
            print(item)

def call_recipe_list(button):
    if button == "Receptlista":
        recipe_list = current_recipe_name()
        recipe_list = sort_lists(recipe_list)
        for item in recipe_list:
            item = (item.rstrip().replace("{", "").replace('"', '').replace(":", ""))
            print(item)

def call_shopping_list(button):
    if button == "Handlingslista":
        shopping_list = current_shop_list()
        for item in shopping_list:
            print(item)

def call_to_storage(button):
    if button == "Lägg till varor":
        add_input_from_user_to_storage()
        app.stop()

def call_to_recipe(button):
    if button == "Lägg till recept":
        add_input_from_recipe_from_user()
        app.stop()

def call_dinner_tip(button):
    if button == "Middagstips":
        clear_shop_list()
        dinner = dinner_tip()
        print(dinner)
        app.stop()

# har inte definerat klart functionerna men vill ha kvar layouten på gui så därav en pass på funtionen
def call_value(button):
    pass

app = gui()
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