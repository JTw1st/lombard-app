import csv

FIELDS = ['ID', 'Title', 'Price']
FILENAME = "database.csv"


def display_menu():
    print("""What would you like to do?
    1 - Add item
    2 - Remove item
    3 - Search for items
    4 - Display all items
    x - Go to drink some coffee""")

    return input("> ")


def read_data(data):
    with open(FILENAME, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.update({row.pop("ID"): row})


def save_data(data):
    with open(FILENAME, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(FIELDS)
        for k, v in data.items():
            writer.writerow([k, *v.values()])


def add_data(new_data, data):
    try:
        data.update({str(int(list(data)[-1]) + 1): dict(zip(FIELDS[1:], new_data))})
    except:
        data.update({"1": dict(zip(FIELDS[1:], new_data))})
    save_data(data)
    return data


def delete_data(data, delete_value):
    flag = False
    for i in list(data):
        if data[i]["Title"].lower() == delete_value.lower():
            del data[i]
            flag = True
    save_data(data)
    return flag


def search_data(data, search_value):
    for i in list(data):
        if data[i]["Title"].lower() == search_value.lower():
            return "|".join([i, *data[i].values()])


def display_data(data):
    res_row = "No data"
    if len(data) > 0:
        res_row = '|'.join(FIELDS)
        for i in data:
            res_row += '\n' + '|'.join([i, *data[i].values()])
    return res_row
