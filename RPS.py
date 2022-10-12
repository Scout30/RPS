import random
turns = ['rock', 'paper', 'scissors']
player_think = input("Play? y/n: ")
if player_think == 'y':
    while(True):
        playerscore = 0
        cpuscore = 0
        while(True):
            player_turn = input("Enter your turn, or type exit: ")
            cpu_turn = random.choice(turns)
            if player_turn == 'exit':
                if playerscore > cpuscore:
                    print('player wins game')
                elif playerscore < cpuscore:
                    print('cpu wins game')
                elif playerscore == cpuscore:
                    print('game is a draw')
                break
            print(f'Player:{player_turn} vs. cpu:{cpu_turn}')
            if player_turn == cpu_turn:
                print('Draw!')
            elif player_turn == 'rock' and cpu_turn == 'scissors':
                print('Player wins!')
                playerscore = playerscore + 1
            elif player_turn == 'paper' and cpu_turn == 'rock':
                print('Player wins!')
                playerscore = playerscore + 1
            elif player_turn == 'scissors' and cpu_turn == 'paper':
                print('Player wins!')
                playerscore = playerscore + 1
            elif player_turn == 'gun':
                print('Player killed cpu')
                break
            else:
                print('cpu wins!')
                cpuscore = cpuscore + 1
            print(f'player= {playerscore} / {cpuscore} =cpu')
        player_trim = input("Again?: ")
        if player_trim == 'no':
            print('Thank you for playing! Bye bye')
            break
