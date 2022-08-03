import random

print("                 Welcome to Rock, Paper, Scissors Game")
print("---------------------------------------------------------------------------")

try_again = 0

while try_again == 0:

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
    game_imgs = [rock, paper, scissors]
    try: 
        user_choice = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors? "))
        print("\nYou chose:")
        print(game_imgs[user_choice])
    except:
        print("\nInvalid choice. Try again. \n")

    computer_choice = random.randint(1,3)
    print("Computer chose:")
    print(game_imgs[computer_choice])
        
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
