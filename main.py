import os

from utils import *

data = {}
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as _:
        pass
read_data(data)

while True:
    option = display_menu()

    if option == "1":
        new_data = []
        for title in FIELDS[1:]:
            new_data.append(input(f"Enter {title.lower()}: "))
        add_data(new_data, data)
    elif option == "2":
        del_value = input("What would you like to delete? ")
        result = delete_data(data, del_value)
        if result:
            print("Successfully deleted")
        else:
            print("No such data")
    elif option == "3":
        search_value = input("What would you like to search for? ")
        result = search_data(data, search_value)
        if result is not None:
            print(f"{'|'.join(FIELDS)}\n{result}")
        else:
            print("No such data")
    elif option == "4":
        print(display_data(data))
    elif option == "x":
        print("Thank you! Shutting down.")
        break
