# Function to print out screen
import random


def set_field(position_list):
    print("\t\t\t\t 0 | 1 | 2")
    print("\t\t\t\t __|___|___")
    print("\t\t\t\t 3 | 4 | 5")
    print("\t\t\t\t __|___|___")
    print("\t\t\t\t 6 | 7 | 8")
    print("\t\t\t\t   |   |  ")
    print()

    print("\t\t\t\t " + str(position_list[0]) + " | " + str(position_list[1]) + " | " + str(position_list[2]))
    print("\t\t\t\t __|___|___")
    print("\t\t\t\t " + str(position_list[3]) + " | " + str(position_list[4]) + " | " + str(position_list[5]))
    print("\t\t\t\t __|___|___")
    print("\t\t\t\t " + str(position_list[6]) + " | " + str(position_list[7]) + " | " + str(position_list[8]))
    print("\t\t\t\t   |   |    ")


def game_won(position_list):
    global winner
    for x in range(0, 7, 3):
        if position_list[x] == position_list[x+1] == position_list[x+2] and position_list[x] != " ":
            winner = position_list[x]
            return True
    for x in range(0, 3):
        if position_list[x] == position_list[x+3] == position_list[x+6] and position_list[x] != " ":
            winner = position_list[x]
            return True

    if position_list[0] == position_list[4] == position_list[8] and position_list[0] != " ":
        winner = position_list[0]
        return True
    if position_list[2] == position_list[4] == position_list[6] and position_list[2] != " ":
        winner = position_list[2]
        return True

    return False


def run_game():
    global fields
    global winner
    fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    while not game_won(fields) and " " in fields:
        set_field(fields)
        fields = user_input(fields)
        if game_won(fields):
            set_field(fields)
            break
        fields = ai_input(fields)
        if game_won(fields):
            set_field(fields)
            break

    set_field(fields)
    if winner == "C":
        print("The computer wins")
    elif winner == "U":
        print("You, the player, won!")
    else:
        print("The game ended in a draw")


def user_input(c_fields):
    counter = 0
    while counter == 0:
        pick = int(input("Enter your move: "))

        if 0 <= pick < 9 and c_fields[pick] == " ":
            c_fields[pick] = "U"
            counter += 1

        else:
            print("Error, Please enter another value: ")
            print()
    return c_fields


def ai_input(c_fields):
    counter = 0
    while counter == 0:
        move = random.randint(0, 8)
        if c_fields[move] == " ":
            c_fields[move] = "C"
            counter += 1

    return c_fields



run_game()