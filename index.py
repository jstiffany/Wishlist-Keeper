# Created on 04-14-2026
# Finished on 04-16-2026

# This program is a wishlist where you can add different items
# and change the list to your liking.

# Please note this wishlist is only tempoary as it is not
# linked to any database of some sort.

# ------------ INTRO

print("------ WELCOME TO: Wishlist Keeper ------")
print("Here, you list your items along with their price.\nYou can add, delete, and update different items.\n")

# ------------ FUNCTIONS

item_list = []


def view_list():
    print(item_list)
    
def add_item():
    item_add_input = input("What would you like to add to your list? ")
    itemadd_price = int(input("\nWhat is the price of this item?\nThere is no need to add the $ sign. "))
    
    item_add_final = f"{item_add_input} ${itemadd_price}"
    
    item_list.append(item_add_final)
    print("\nYour item has been added and updated. Here is a view.")
    print(item_list)
    
def rem_item():
    item_rem_req = input("What would you like to remove?\nPlease note this is case sensitive including the price. ")
    
    if item_rem_req in item_list:
        item_list.remove(item_rem_req)
        print("\nYour item has been removed and updated. Here is a view.")
        print(item_list)
    else:
        print("\nYour response was either not valid or doesn't exist.\n")
    
    
# ------------ MAIN CODE

print("1 = View list\n2 = Add item\n3 = Remove item\n5 = Exit list")

func_type = int(input("\nHow would you like to manage your wishlist? "))

while func_type != 5:

    if func_type == 1:
        view_list()
        func_type = int(input("\nHow would you like to manage your wishlist? "))

    elif func_type == 2:
        add_item()
        func_type = int(input("\nHow would you like to manage your wishlist? "))

    elif func_type == 3:
        rem_item()
        func_type = int(input("\nHow would you like to manage your wishlist? "))

    else:
        print("\nThat is not a valid input.")
        func_type = int(input("\nHow would you like to manage your wishlist? "))