import random
import art
import game_data
import subprocess


def random_data():
    data = random.choice(game_data.data)
    return data

def more_follower(data1, data2, c):
    if data1['follower_count'] > data2['follower_count'] and c == 'A': 
        return True
    elif data1['follower_count'] < data2['follower_count'] and c == 'B':
        return True
    else:
        return False

def game():
    account1 = random_data()
    account2 = random_data()
    score = 0
    print(art.logo)

    while True:
        account1 = account2
        account2 = random_data()

        while account1 == account2:
            account2 = random_data()
        
        print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}")
        print(art.vs)
        print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == 'A' or user_choice == 'B':
            bigger_account = more_follower(account1, account2, user_choice)
        else:
            print("Enter 'A' or 'B' only")
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            bigger_account = more_follower(account1, account2, user_choice)
        subprocess.run("cls", shell=True)
        print(art.logo)
        if bigger_account:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


game()