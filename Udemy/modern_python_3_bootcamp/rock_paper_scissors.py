print("Rock!")
print("Paper!")
print("Scisccors!")
player1 = input("Enter your choice, Plyaer 1! ")
player2 = input("Enter your choice, Player 2! ")
print("Shoot!")

if player1.lower() == 'rock':
    if player2.lower() == 'scissors':
        print("Player 1 Wins!")
    elif player2.lower() == 'rock':
        print("Draw! Try again!")
    elif player2.lower() == 'paper':
        print("Player 2 Wins!")
    else:
        print("Unknown choice entered for Player 2. Try again.")
elif player1.lower() == 'paper':
    if player2.lower() == 'rock':
        print("Player 1 Wins!")
    elif player2.lower() == 'paper':
        print("Draw! Try again!")
    elif player2.lower() == 'scissors':
        print("Player 2 Wins!")
    else:
        print("Unknown choice entered for Player 2. Try again.")
elif player1.lower() == 'scissors':
    if player2.lower() == 'paper':
        print("Player 1 Wins!")
    elif player2.lower() == 'scissors':
        print("Draw! Try again!")
    elif player2.lower() == 'rock':
        print("Player 2 Wins!")
    else:
        print("Unknown choice entered for Player 2. Try again.")
else:
    print("Unknown choices entered. Try agian.")