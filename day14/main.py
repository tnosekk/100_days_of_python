import os
from random import randint

from art import logo, vs
from game_data import data


def game():
    print(logo)
    play = True
    user_score = 0
    data_len = len(data)
    a_random = randint(0, data_len - 1)
    b_random = randint(0, data_len - 1)
    if a_random == b_random:
        a_random = randint(0, data_len - 1)
    while play == True:
        print_figure(a_or_b="A", rand_choice=a_random)
        a_followers = get_follower_count(data, a_random)
        print(vs)
        print_figure(a_or_b="B", rand_choice=b_random)
        b_followers = get_follower_count(data, b_random)

        user_choice = input("Who has more folowers? Type 'A' or 'B': ")
        won = if_won(a_followers, b_followers, user_choice)
        if won == True:
            os.system("clear")
            print(logo)
            user_score += 1
            print(f"You're right! Current score: {user_score}")
            winner = who_won(a_followers, b_followers)
            if winner == "B":
                a_random = b_random
                b_random = randint(0, data_len - 1)
            elif winner == "A":
                b_random = randint(0, data_len - 1)

            # os.system("clear")
            # if B is correct then change a_choice to b_choice and choose another b_choice
            # if A is correct then a_choice stays the same and choose another b_choice
        elif won == False:
            print(f"Sorry, thats wrong, Final score: {user_score}")
            play = False

        # if user guested wrong then end ganme with "Sorry, thats wrong, Final score: 0"
        # if user guested right then the one with more followers becomes A and i need to choose another B figure
        # if right print "You're right! Current score: {current score}"


def get_name(data, random_int):
    name = data[random_int]["name"]
    return name


def get_description(data, random_int):
    description = data[random_int]["description"]
    return description


def get_country(data, random_int):
    country = data[random_int]["country"]
    return country


def get_follower_count(data, random_int):
    followers = data[random_int]["follower_count"]
    return followers


def print_figure(a_or_b, rand_choice):
    name = get_name(data, rand_choice)
    desc = get_description(data, rand_choice)
    country = get_country(data, rand_choice)
    print(f"Compare {a_or_b}: {name}, a {desc}, from {country}")


def if_won(a_count, b_count, user_choice):
    winner = None
    if a_count > b_count:
        winner = "A"
    else:
        winner = "B"

    if user_choice == "A" and winner == "A":
        return True
    elif user_choice == "B" and winner == "B":
        return True
    else:
        return False


def who_won(a_count, b_count):
    if a_count > b_count:
        return "A"
    elif a_count < b_count:
        return "B"


game()
