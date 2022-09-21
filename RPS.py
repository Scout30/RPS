import random

player = input("enter your choice: ")
choice = ["paper", "rock", "scissors"]

cpu = random.choice(choice)

if player == cpu:
    print('Draw!')
elif player == 'parer' and cpu == 'rock':
    print('Pleyer wins!')
elif player == 'scissors' and cpu == 'paper':
    print('Pleyer wins!')
elif player == 'rock' and cpu == 'scissors':
    print('Pleyer wins!')
else:
    print('CPU wins!')
