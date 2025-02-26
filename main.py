import json

filename = "C:\\Users\\kylem\\Desktop\\Application of Python for DH\\01_Creating_Database\\data\\kings.json"

def Choices():
    print('K I N G S')
    print('Data Management System')
    print('(1) View Data')
    print('(2) Add Data')
    print('(3) Delete Data')
    print('(4) Edit Data')
    print('(5) Exit')
    
def view_data():
    with open(filename,mode='r') as f:
        temp = json.load(f)
        i = 0
        for entry in temp:
            name = entry["name"]
            begin = entry["begin"]
            end = entry["end"]
            print(f'Index #: {i}')
            print(f'Name of King: {name}')
            print(f'Begin of Reign: {begin}')
            print(f'End of Reign: {end}')
            print('\n\n')
            i += 1
            
def edit_data():
    view_data()
    new_data = []
    with open(filename,mode='r') as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print('Which index number would you like to edit? ')
    edit_option = input(f'Select a number 0-{data_length}: ')
    i = 0
    for entry in temp:
        if i == int(edit_option):
            name = entry["name"]
            begin = entry["begin"]
            end = entry["end"]
            print(f'Current Name of King: {name}')
            name = input('What would you like the new name to be: ')
            print(f'Current Begin of Reign: {begin}')
            begin = input('What would you like the new begin to be: ')
            print(f'Current End of Reign: {end}')
            end = input('What would you like the new end to be: ')
            new_data.append({"name":name,"begin":begin,"end":end})
            i +=1
        else:
            new_data.append(entry)
            i += 1
    with open(filename,mode='w') as f:
        json.dump(new_data,f,indent=4)
            
def delete_data():
    view_data()
    new_data = []
    with open(filename,mode='r') as f:
        temp = json.load(f)
        data_length = len(temp)-1
    print('Which index number would you like to delete? ')
    delete_option = input(f'Select a number 0-{data_length}: ')
    i = 0
    for entry in temp:
        if i == int(delete_option):
            pass
            i +=1
        else:
            new_data.append(entry)
            i += 1
    with open(filename,mode='w') as f:
        json.dump(new_data,f,indent=4)

def add_data():
    item_data = {}
    with open(filename,mode='r') as f:
        temp = json.load(f)
    item_data["name"] = input('Name of King: ')
    item_data["begin"] = input('Begin of Reign: ')
    item_data["end"] = input('End of Reign: ')
    temp.append(item_data)
    with open(filename,mode='w') as f:
        json.dump(temp,f,indent=4)
    
while True:
    Choices()
    choice = input('\nEnter number: ')
    if choice == '1':
        view_data()
    elif choice == '2':
        add_data()
    elif choice == '3':
        delete_data()
    elif choice == '4':
        edit_data()
    elif choice == '5':
        break
    else:
        print('You did not select a number, please read more carefully.')
        
