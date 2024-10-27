import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("WELCOME TO ROCK PAPER SCISSORS!!")
choice = [rock, paper, scissors]
result = random.randint(0, 2)

choose = int(input('Choose "0" for Rock, "1" for Paper, and "2" for Scissors" '))
#Draw Factor
if choose == result:
    print(f"You: {choice[choose]}")
    print(f"Computer: {choice[result]}")
    print("It's a draw")
#Losing Factor
elif (choose == 0 and result == 1) or (choose == 1 and result == 2) or (choose == 2 and result == 0):
    print(f"You: {choice[choose]}")
    print(f"Computer: {choice[result]}")
    print("Computer Wins!\n Try Again?")

#Win Factor
else:
    print(f"You: {choice[choose]}")
    print(f"Computer: {choice[result]}")
    print("You Win!\n Try Again?")