#Python treasure hunt game

import random, time


def display_game_intro():
    print ('''
            ----> Welcome to my 'Python Treasure Hunt Game'
                ... the most amazing game ever made.

            After a long journey, you find yourself in front of two caves.
            One cave leads to a treasure. The other? A spike filled pit!
            Being brave and a little greedy, you decide to go for the prize!

        ''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave do you want to enter? (1 or 2)')
        cave = input()
    return cave


def enter_cave(chosen_cave):
    print('\nYou have entered a cave...')
    time.sleep(1)

    random_cave = random.randint(1,2)
    #print("random_cave=" + str(random_cave))

    if random_cave == int(chosen_cave):
        print("---> Lucky you. You found the treasure.")
    else:
        print("---> You expected a chest\n... and all you found was your demise..")


def main_loop():
    ''' the main_loop() function controls the flow of the game by calling functions and using conditionals'''  

    playGameAgain = "yes"

    while playGameAgain == "yes" or playGameAgain == "y":

        display_game_intro()
        chosen_cave = choose_cave()
        enter_cave(chosen_cave)

        print("\n\nDo you want to try again?(yes or no)")
        playGameAgain = input()
        print("You said: " + playGameAgain)
        time.sleep(1)

        if playGameAgain == "yes" or playGameAgain == "y":
            print("\nLets try Again")

        else:
            print("\nSee Ya Later!")
    

main_loop()
