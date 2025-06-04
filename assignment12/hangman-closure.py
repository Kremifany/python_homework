# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display = ""
        allGuessed = True
        for letter in secret_word:
            if letter in guesses:
                display += letter
            else:
                display += "_"
                allGuessed=False
        print(display)
        return allGuessed
    return hangman_closure

secret_word = input("Please enter the secret word to guess :  ")
hangman_closure = make_hangman(secret_word)
allGuessed = False
while not allGuessed:
    letter = input("\nPlease guess letter:  ")
    allGuessed = hangman_closure(letter)
print("Well done!!!!")