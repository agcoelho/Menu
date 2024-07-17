import random

def play():
    

    option = 1

    while option != 2:
        
        print('###############################\n')
        print('wellcome to the hangman game!!')
        print('###############################\n')


        archive = open('fruits.txt', 'r')
        words = []

        for line in archive:
            line = line.strip()
            words.append(line)

        archive.close

        number = random.randrange(0, 44)

        secret_word = words[number]
        secret_word = secret_word.upper()
        correct = ['_' for character in secret_word]
        dead = False
        right = False
        c = 6





        while not dead and not right:
            print('jogando...\n')
            
            guess = input('Guess one character\n')
            guess = guess.strip().upper()
            
            
            if guess in secret_word:
                
                index = 0
                for character in secret_word:
                    if guess.upper() == character.upper():
                        correct[index] = character
                    index = index + 1
                    if '_' not in correct:
                        right = True
                        
            else:
                print('theres no such character.\nTry again.')
                c = c - 1
                print('you still have {} try\n'.format(c))
                if c < 1:
                    dead = True
                    print('a palavra era: {}\nGame Over!'.format(secret_word))
                if '_' not in correct:
                    right = True

            if not dead:    
                print('{}\n'.format(correct))
            if right:
                print('congratulations, you have won!!!\n')

        option = int(input('would you like to play again? 1-YES // 2-NO\n'))




