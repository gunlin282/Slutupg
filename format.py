# en function för att sortera listor i bokstavsordning
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
