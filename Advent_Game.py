import time
import random


def print_pause(print_message):
    print(print_message)
    time.sleep(1)


def introduction(item, option):
    print_pause("You find yourself standing inside a front door of a open gym "
                "with basketball courts.\n")
    print_pause("Rumor has it that a " + option + " is somewhere around "
                "here, and beating everyone in one on one.\n")
    print_pause("In front of you is a open court.\n")
    print_pause("To your right is a court occuppied by"
                "a tall unrecognizable player.\n")
    print_pause("On your feet is your trusty but beatup basketball shoes.\n")


def open_court(item, option):
    if "gymbag" in item:
        print_pause("\nYou walk to the empty court.")
        print_pause("\nYou've been here before, and gotten all"
                    " the swag. It's just an empty court"
                    " now.")
        print_pause("\nYou walk back to the frontdoor.\n")
    else:
        print_pause("\nYou approach the empty court.")
        print_pause("\nIt turns out to there was a shoe box.")
        print_pause("\nYou open the box and shock to see "
                    "the shoes.")
        print_pause("\nIt is some Air Jordan Is!!!!")
        print_pause("\nYou take off your shoes and put on "
                    "the new shoes.")
        print_pause("\nYou walk back to the front door.\n")
        item.append("gymbag")
    front_door(item, option)


def right_court(item, option):
    print_pause("\nYou approach the player.")
    print_pause("\nOh no! It is " + option + "!")
    print_pause(option + " challenges you!\n")
    if "gymbag" not in item:
        print_pause("You feel a bit embarrassed for this, "
                    " with no dope kicks.\n")
    while True:
        choice2 = input("Would you like to (1) play or (2) "
                        "walk away?\n")
        if choice2 == "1":
            if "gymbag" in item:
                print_pause("\nAs the " + option + " tries to block you, "
                            "you unleash a sick move.")
                print_pause("\n" + option + " can not believe the move!")
                print_pause("\n" + option + " takes one look at you "
                            "and gives you a head nod!")
                print_pause("\nYou have got the respect of " + option +
                            ". Sounds like a WIN to me!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your footwear is no match for "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou walk back to the front door. "
                        "\nLuckily, no one saw that.\n")
            front_door(item, option)
            break


def front_door(item, option):
    print_pause("Enter 1 to challenge the player.")
    print_pause("Enter 2 to play by yourself.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            right_court(item, option)
            break
        elif choice1 == "2":
            open_court(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\nExcellent! Lets go champ ...\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\nThanks for playing!.\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Michael Jordan", "Kobe Bryant",
                            "Shaq", "Lebron James"])
    introduction(item, option)
    front_door(item, option)


play_game()
