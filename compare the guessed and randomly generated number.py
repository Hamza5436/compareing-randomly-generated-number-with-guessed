
import random


e=input('Enter "y" if you want to generate a random number and compare with the number you guessed: ')


while e=='y':
    b=random.randint(1,6)
    a=int(input("Guess the number: "))

    print('Randomly Generated Number: ',b)


    if b>a:
        print('----------------------------')
        print('The Number You guess is low!')
        print('----------------------------')
    elif b<a:
        print('_____________________________')
        print('The Number you Guess is High!')
        print('-----------------------------')
    else:
        print('----------------------')
        print('Both Numbers are equal')
        print('----------------------')
