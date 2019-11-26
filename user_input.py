
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

def sort_lists(sort):
    sort_me = sorted(sort)
    return sort_me

def clear_shop_list():
    shopping_list = open('Shop_list.txt', 'w')
    shopping_list.close()

def volym_weight_format(items):
    mesurement = {"ml": 1, "tsk": 5, "msk": 15, "dl": 100, "l": 1000, "g": 1, "hg": 100, "kg": 1000}
    if items in mesurement.keys():
        items = mesurement[items]
    return items
