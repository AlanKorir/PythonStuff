import sys
password = 'James'
while True:
    print("Enter password to exit program: ")
    response = input()
    if response == 'James':
        print ('Access Granted')
        sys.exit()
    else: 
        print('Try Again!')
