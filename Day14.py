#rock paper scissors game
print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice:(R,P OR S) ")
print()
player1 = input("Player1: ")
print()
player2 = input("Player2: ")
print()
if player1 == player2:
  print("Tie!")
elif player1 == "R":
  if player2 == "P":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
elif player1 == "P":
  if player2 == "S":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
elif player1 == "S":
  if player2 == "R":
    print("Player 2 wins!")
  else:
    print("Player 1 wins!")
print("Thank you for playing!")
    