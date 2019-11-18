import json
from format import volym_weight_format

# skapade denna genom att bolla ideer med Emil Jönsson, han använder förmodligen liknande lösning
#  behöver lägga till expeption för felaktig inmatning
def get_storage_input_from_user():
    while_input = True
    storage_append = []
    while while_input:
        article = str(input("Skriv in varan du vill lägga till: ")).lower()
        amount = int(input(f"Skriv in mängden av {article} du vill lägga till: "))
        type = str(input("Är det tsk, msk, dl, l, g, hg, kg: ")).lower()
        value_type = volym_weight_format(type)
        add_list_in_storage_list = [amount * value_type]
        storage = {article: add_list_in_storage_list}
        storage_append.append(storage)
        continue_input = str(input("Vill du lägga in fler varor? Y eller N ")).lower()
        if continue_input == "n":
            return storage_append

# hittade json lösningen på W3School, gör att man kan "appenda" alla typer till .txt filen
# .append funktionen ville inte ta emot både int och str
def add_input_from_user_to_storage():
    add_storage_list = get_storage_input_from_user()
    with open('Storage_list.txt', 'a',) as storage_append:
        json.dump(add_storage_list, storage_append, ensure_ascii=False)
        storage_append.write('\n')

 # behöver lägga till expeption för felaktig inmatning
def get_recipe_input_from_user():
    recipe_name = str(input("Skriv in namn på receptet: ")).lower()
    recipe_append = []
    recipe_appender = {recipe_name: recipe_append}
    while_input = True
    while while_input:
        ingredient = str(input("Ange ingrediens ")).lower()
        ingredient_amount = int(input(f"Skriv in mängden av {ingredient} du vill lägga till: "))
        ingredient_type = str(input("Är det DL, L , G, KG osv: ")).lower()
        ingredient_type = volym_weight_format(ingredient_type)
        article_values = {ingredient: (ingredient_amount*ingredient_type)}
        ingredient_values = article_values
        recipe_append.append(ingredient_values)
        continue_input = str(input("Vill du lägga in fler ingredienser? Y eller N ")).lower()
        if continue_input == "n":
            recipe_cook = str(input("Ange tillagningsprocess: "))
            recipe_append.append(recipe_cook)
            return recipe_appender

def add_input_from_recipe_from_user():
    add_recipe_list = get_recipe_input_from_user()
    with open('Recipe_list.txt', 'a') as recipe_append:
        json.dump(add_recipe_list, recipe_append, ensure_ascii=False)
        recipe_append.write('\n')