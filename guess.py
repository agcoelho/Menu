import random


def play():
    print('###############################')
    print('Wellcome to the guessing game!')
    print('###############################')
    guess = 0
    secret_number = random.randrange(1,100)

    attempts = int(input('How many attempts do you wish to have?\n'))
    while attempts > 0 and guess != secret_number:
        # print(secret_number)
        
        print('attempts left:', attempts)
        guess = int(input('Type your guess:\n'))

        above = guess > secret_number
        under = guess < secret_number

        print('\nYou guessed:', guess,'\n')

        if secret_number == guess:
            print('You won!! Congratulations!!\n')
        else:
            if above:
                print('Your guess is above the right number.\n')
                attempts = attempts - 1
                if attempts > 0:
                    print('Pls try again')
                else:
                    print('you loose')
            elif under:
                print('Your guess is under the right number.\n')
                attempts = attempts - 1
                if attempts > 0:
                    print('Pls try again')
                else:
                    print('you loose')
    print('the secret number was {}'.format(secret_number))
