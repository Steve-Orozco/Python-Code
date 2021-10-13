#!/usr/bin/python3

# Game: Dragon Realm

import random
import time
 
def displayIntro():
    print('''You are in a land full of dragons. In front of you,
    you see four caves. In one cave, the dragon is friendly
    and will share his treasure with you. The second cave the dragon
    is greedy and hungry, and will eat you on sight. The third cave 
    there you smell a familiar aroma.. should you follow? The last
    cave, there is a faint sound of metal tinging that intruges you''')
    print()
 
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4':
        print('Which cave will you go into? (1, 2, 3 or 4)')
        cave = input()

    return cave
 
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    notfriendly = random.randint(3, 4)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!') 
    elif chosenCave == str(friendlyCave):
        print('Gives you a chicken!')
    elif chosenCave == str(notfriendly):
        print('Smacks yo mama')
    elif chosenCave == str(notfriendly):
        print('punches you in da face!')
    else:
        print('Gobbles you down in one bite!')
    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()