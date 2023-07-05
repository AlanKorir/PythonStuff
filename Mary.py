User1 = 'Mary'
password_User1 = 'Mary1'

User2 = 'Jane'
password_User2 = 'Jane1'

user = input('Enter Name: ')


Attempts = 0
if user == User1:
    print('Hello Mary!')
    while Attempts < 3:
        password_user = input('Enter Password: ')
        if password_User1 == password_user:
            print('Access Granted!')
            continue
        else:
            print('Access Denied! ')
            Attempts == Attempts + 1
        
        if Attempts == 3:
            print ('Contact Administrator')
            break


