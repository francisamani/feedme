# Francis Oludhe
# Feed Me

import random
import time
import sys

# Greetings
def greet(who= ''):
    print('\nHello', who+',')

pick = ('1', '2', '3', '4', '5', '6', '7')

name = input('\nWhat is your name? ')

greet(who = name)

# Variables
b = 0
l = 0
s = 0
breakfast = []
lunch = []
supper = []

# To fill any empty lists
def none(breakfast, lunch, supper):
    if len(breakfast) < 2:
        add = input('\nWhat would you like to add to your morning options? ')
        breakfast.append(add)
        print (add, "has been added to your breakfast list.")
        none(breakfast, lunch, supper)

    if len(lunch) < 2:
        add = input('\nWhat would you like to add to your lunch options? ')
        lunch.append(add)
        print (add, "has been added to your lunch list.")
        none(breakfast, lunch, supper)

    if len(supper) < 2:
        add = input('\nWhat would you like to add to your supper options? ')
        supper.append(add)
        print (add, "has been added to your supper list.")
        none(breakfast, lunch, supper)

none(breakfast, lunch, supper)

# Options
print ('\nOptions.', '\n1- Pick food for Breakfast', '2- Pick food for Lunch',
 '3- Pick food for Supper', '4- Add Breakfast options', '5- Add Lunch options', '6- Add Supper options', '7- Close', sep='\n')

# Function to kick off operations
def meal(breakfast, lunch, supper, b, l, s):
    choice = input('\nPick an action? ')

    while choice not in pick:
        print('\nKindly pick a number between 1 and 7.')
        choice = input('\nPick an action? ')

    if choice == '1':
        b = random.choice(breakfast)
        print ("\nFor breakfast you'll have", b)
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '2':
        l = random.choice(lunch)
        print ("\nFor lunch you'll have", l)
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '3':
        s = random.choice(supper)
        print ("\nFor supper you'll have", s)
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '4':
        add = input('\nWhat would you like to add to your morning options? ')
        breakfast.append(add)
        print ('\n', add, "has been added to your breakfast list.")
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '5':
        add = input('\nWhat would you like to add to your lunch options? ')
        lunch.append(add)
        print ('\n', add, "has been added to your lunch list.")
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '6':
        add = input('\nWhat would you like to add to your supper options? ')
        supper.append(add)
        print ('\n', add, "has been added to your supper list.")
        meal(breakfast, lunch, supper, b, l, s)

    if choice == '7':
        print ("\nThank you.")
        time.sleep(1)
        print ('Enjoy your meals.')
        time.sleep(2)
        sys.exit()

# Start of the operation
meal(breakfast, lunch, supper, b, l, s)
