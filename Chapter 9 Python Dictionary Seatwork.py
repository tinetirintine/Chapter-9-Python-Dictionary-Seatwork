
record = dict()

while True:
    print('a. Add Data')
    print('b. Delete Data')
    print('c. End')

    action = input('Select action: ')

    if action == 'a' :
        key = input('Enter a key: ')
        value = input('Enter value: ')
        record[key.upper()] = value
        print(record)

    if action == 'b' :
        key = input('Enter a key: ')








    elif action == 'c' :
        print('Thank you. Program will now end')
        break

