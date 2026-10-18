


record = dict()
print('==== Record Keeping App ====')

while True :
    print('a. Add Data')
    print('b. Delete Data')
    print('c. End')

    action = input('Select action: ')

    if action == 'a' :
        key = input('Enter a key: ')
        value = input('Enter value: ')
        record[key.upper()] = value
        print(record)

    elif action == 'b' :
        key = input('Enter a key: ')

        if key.upper() in record :
            del record[key.upper()]
            print(record)
        else :
            print('=== Key does not exist! ===')

    elif action == 'c' :
        print('Thank you. Program will now end')
        break


    else :
        print('Invalid action. Please try again.')



