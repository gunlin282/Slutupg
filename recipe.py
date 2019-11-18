
def current_recipe_name():
    my_recipe = []
    recipe = open("Recipe_list.txt", "r")
    for lines in recipe:
        first_word = lines.split()[0]
        my_recipe.append(first_word)
    return my_recipe

def current_recipe():
    my_recipe = []
    with open("Recipe_list.txt", "r") as file:
        reader = file.readlines()
        for item in reader:
            my_recipe.append(item.rstrip("\n", ))
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


# ska gå igenom storage_list och matcha mot recipe_list
# skriver ingredienserna som saknade fast dom finns, behöver ses över!
my_ingredient = current_ingredient()
def dinner_tip():
    recipes = {}
    with open('Recipe_list.txt', 'r') as f:
        for line in f:
            words = line.split()
            if words:
                recipes[words[0]] = words[1:]

    for recipe, ingredients in recipes.items():
        for ingredient in ingredients:
            if ingredient not in my_ingredient:
                shopping_cart = open('Shop_list.txt', 'a')
                shopping_cart.write('{}\n'.format(ingredient))
                print("Saknad vara {} är tillagd i handlingslisan".format(ingredient))
                shopping_cart.close()
                break
        else:
            print("Du har varor för laga {}".format(recipe))



# test av olika lösningar för middagstips:

# dict1 = current_ingredient()
# dict2 = current_recipe()
# diff = set(dict2) - set(dict1)
# shopping_cart = open('Shop_list.txt', 'a')
# shopping_cart.write('{}\n'.format(diff))
# print("Saknad vara {} är tillagd i handlingslisan".format(diff))
# shopping_cart.close()

# dict1 = {"recept": [{"ost": [1000]}, {"fisk": [100]}, {"bacon": [100]}, {"rödbeta": [1000]}, {"pasta": [1000]}, {"lök": [1000]}]}
# dict2 = {"carbonara": [{"pasta": 2}, {"bacon": 2}, "laga mat"]}
# for key in dict(dict1.keys()):
#     if key in dict(dict2.keys()):
#         print(key)
