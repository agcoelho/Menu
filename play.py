import hangman
import guess

option = int(input('select the game:\n1-hangman\n2-guess the number\n3-quit\n'))
if option == 1:
        hangman.play()
elif option == 2:
        guess.play()
else:
    print('you quit the menu')

