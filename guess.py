from random import randint
a = randint(1,100)
i = 0
b = 0
#print(a)
print ("WELCOME TO GUESS THE NUMBER!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're in COLD zone")
print("If your guess is within 10 of my number, I'll tell you you're in WARM zone")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
print("If you lose your temper type 'LOSE'")
while True:
    # try and except to take valid input without breaking
    try:
        num = input('enter number: ')
        if num.lower() == 'lose':
            print(f'The number is {a}  YOU LOSE')
            break
        num = int(num)

        if num < 1 or num > 100:
            print("Out of bound")
            continue
        elif num == a:
            # addding number of guesses.
            i += 1
            print(f'You have guess the number {a} and your guesses are {i}')
            break
            #  checking for guesses in which zone according to rules.
        elif i >= 1:
            if abs(num - a) <= abs(b - a):
                b = num
                print('Warmer')
                i += 1
            else :
                b= num
                print ('colder')
                i += 1
        else:
            if abs(num - a) < 10 :
                b = num
                print ('Warm')
                i += 1
            else :
                b = num
                print ('Cold')
                i += 1

    except:
        print('Enter valid input')
        continue
