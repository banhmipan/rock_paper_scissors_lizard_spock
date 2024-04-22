# Rock Paper Scissors (Lizard Spock) CP Project 🙏
import random

name = input("Enter your name: ")
def game():
  player = int(input(f"----------------------------------\nHowdy {name}, let's play Rock Paper Scissors Lizard Spock!\n 1) ✊\n 2) ✋\n 3) ✌\n 4) 🦎\n 5) 🖖\nChoose a number: "))
  computer = random.randint(1, 5)
  rock = "✊"
  paper = "✋"
  scissors = "✌"
  lizard = "🦎"
  spock = "🖖"

  # Player/Computer Declarations
  if player == 1:
    print(f"\n{name} chose: {rock}")
  elif player == 2:
    print(f"\n{name} chose: {paper}")
  elif player == 3:
    print(f"\n{name} chose: {scissors}")
  elif player == 4:
    print(f"\n{name} chose: {lizard}")
  elif player == 5:
    print(f"\n{name} chose: {spock}")
  else:
    print("Invalid input.")

  if computer == 1:
    print(f"CPU chose: {rock}")
  elif computer == 2:
    print(f"CPU chose: {paper}")
  elif computer == 3:
    print(f"CPU chose: {scissors}")
  elif computer == 4:
    print(f"CPU chose: {lizard}")
  elif computer == 5:
    print(f"CPU chose: {spock}")
  else:
    print("Error.")

  # Winning/Losing System (Computer)
  if player == computer:
    print(f"\n{name} ties with CPU! GG!")
  elif player == 1 and computer == 2:
    print("\nPaper covers rock, and CPU wins! GG!")
  elif player == 2 and computer == 3:
    print("\nScissors cut paper, and CPU wins! GG!")
  elif player == 5 and computer == 4:
    print("\nLizard poisons spock, and CPU wins! GG!")
  elif player == 3 and computer == 5:
    print("\nSpock smashes scissors, and CPU wins! GG!")
  elif player == 4 and computer == 3:
    print("\nScissors beat lizard, and CPU wins! GG!")
  elif player == 2 and computer == 4:
    print("\nLizard eats paper, and CPU wins! GG!")
  elif player == 5 and computer == 2:
    print("\nPaper disproves spock, and CPU wins! GG!")
  elif player == 1 and computer == 5:
    print("\nSpock vaporizes rock, and CPU wins! GG!")
  elif player == 3 and computer == 1:
    print("\nRock breaks scissors, and CPU wins! GG!")
  elif player == 4 and computer == 1:
    print("\nRock crushes lizard, and CPU wins! GG!")

  # Winning/Losing System (Player)
  elif computer == 1 and player == 2:
    print(f"\nPaper covers rock, and {name} wins! GG!")
  elif computer == 2 and player == 3:
    print(f"\nScissors cut paper, and {name} wins! GG!")
  elif computer == 5 and player == 4:
    print(f"\nLizard poisons spock, and {name} wins! GG!")
  elif computer == 3 and player == 5:
    print(f"\nSpock smashes scissors, and {name} wins! GG!")
  elif computer == 4 and player == 3:
    print(f"\nScissors beat lizard, and {name} wins! GG!")
  elif computer == 2 and player == 4:
    print(f"\nLizard eats paper, and {name} wins! GG!")
  elif computer == 5 and player == 2:
    print(f"\nPaper disproves spock, and {name} wins! GG!")
  elif computer == 1 and player == 5:
    print(f"\nSpock vaporizes rock, and {name} wins! GG!")
  elif computer == 3 and player == 1:
    print(f"\nRock breaks scissors, and {name} wins! GG!")
  elif computer == 4 and player == 1:
    print(f"\nRock crushes lizard, and {name} wins! GG!")

  retryPrompt = int(input("\nWould you like to play again?\n1) Yes\n2) No\n\n"))
  while retryPrompt != 2:
    print(f"Aight {name}, let's run it back!")
    return game()
  if retryPrompt == 2:
    print(f"I hope you had fun, {name}! :]")
  else:
    print("Error")
game()