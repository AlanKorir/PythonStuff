# import random, sys

# wins = 0
# ties = 0
# losses = 0

# while True:
#     print('%s Wins,%s Ties,%s Losses' % (wins,ties,losses))

#     while True:
#         print('Enter move: (r)ock, (p)aper, (s)cisssors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit()

#         elif playerMove == 'r' or playerMove == 'p' or playerMove == 'q':
            
#             break
#         else:
#             print('Type one of r, p, s, or q.')

        
#     if playerMove == 'r':
#         print('Rock versus ...')

#     elif playerMove == 'p':
#         print('Paper versus ...')

#     elif playerMove == 's':
#         print('Scissors versus ...')

#     randomNumber = random.randint(1,3)

#     if randomNumber == 1:
#         computerMove = 'r'
#         print ('ROCK!')

#     elif randomNumber == 2:
#         computerMove = 'p'
#         print ('PAPER!')

#     elif randomNumber == 3:
#         computerMove = 's'
#         print ('SCISSORS!')

#     if computerMove == playerMove:
#         print ('Its Tied')

         
for i in range (1,11):
    print (i)

# i = 0
# while i < 100:
#     i = i+2
#     print(i)