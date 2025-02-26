import json

filename = "C:\\Users\\kylem\\Desktop\\Application of Python for DH\\01_Creating_Database\\data\\kings.json"

def Choices():
    print('K I N G S')
    print('Data Management System')
    print('(1) View Data')
    print('(2) Edit Data')
    print('(3) Exit')
    
def view_data():
    with open(filename,mode='r') as f:
        temp = json.load(f)
        for entry in temp:
            name = entry["name"]
            begin = entry["begin"]
            end = entry["end"]
            print(f'Name of King: {name}')
            print(f'Begin of Reign: {begin}')
            print(f'End of Reign: {end}')
            print('\n\n')

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
        print('3')
    else:
        print('You did not select a number, please read more carefully.')
        
