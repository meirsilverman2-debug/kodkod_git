from random import choice

def get_a_word() -> str:
    """
    get nothing but returns a random word from a list of words.
    """

    words = ["perform", "paralyzed", "scratch", "itches", "plenty", "comb", "hair", "independent", "forced",
         "nursing", "helplessness", "dormmitories", "raising", "laser", "beam", "respond", "applications", "significance" ]

    word = choice(words)
    return word

# word = get_a_word()
# print(word)


def get_valid_guess(guess) -> str:
    """
    Takes a guess from the player/user and valdate it that it is one letter and alpha and NOT other special letters.
    """
    

    while not guess.isalpha() or len(guess) != 1:
        print("Invalid guess!!!")
        guess = input("Enter your guess: ")
        
    return guess.lower()
    
# guess = get_valid_guess()
# print(guess)




def create_guess_list(guesses: list[str|None], guess= None) -> list:
    """
    Gets each guess and return a list of all unique guesses.
    """

    if guess in guesses or guess == None:
        return guesses
    
    guesses.append(guess)
    return guesses

# guesses = create_guess_list(guess)
# print(guesses)


def life_amount(word: str) -> int:
    """
    Gets the random word from the get_a_word function and based on the length of the word the player receiv the amount of life.
    """
    life = len(word) +1
    return life



# attempts = life_amount(word)
# print(attempts)

def display_the_word_chosen(word:str) -> str:
    display = "-" * len(word)
    return display


def word_presentation(word: str, display: str, guess= None) -> None:
    """
    Gtes the word that have been chosen and secret_word and the guess and changes the display of the word if the guess is in the wor itself.
    """

    for i in range(len(word)):
        if word[i] == guess:
         display = display[:i] + word[i] + display[i + 1:]

    print(display)
    return display
            

    print(f"This is the corrent display of the word: {display}") 

# display = word_presentation(word, guess)
# print(display)


def welcome_message() -> None:
    print("===========================")
    print("WELCOME TO THE HANGMAN GAME")
    print("===========================")


def show_guesses(guesses = None) -> str|None:
    """
    Gets the list of guessing letters and print it in a nice presentation.
    """
    if guesses == True:
        for i, guess in enumerate(guesses):
            print("=" * len(guess))
            print(i + 1, guess)
            print("=" * len(guess))
    return

def show_result(word: str ,display_word: str ) -> None:
    """
    print the user/player a message befor leaving depending on corrent status.
    """
    if word == display_word:
        print(f"kol hkavod you guessed the word {word}")
    print(f" You did not guessed the word and you ran out of attempts byeeeee")




def hangman_game():
    """
    The  main function that runs hangman game .
    """

    secret_word = get_a_word()
    display_word = display_the_word_chosen(secret_word)
    attempts = life_amount(secret_word)
    letters_list = []

    welcome_message()

    while attempts > 0 and display_word != secret_word:
        print(f"This is your {attempts} turn")
        show_guesses(letters_list)
        guess = input("Enter your guess: ")
        display_word = word_presentation(secret_word,display_word,guess)
        get_valid_guess(guess)
        create_guess_list(letters_list, guess)
        print(create_guess_list(letters_list, guess))
        if guess not in secret_word or guess not in letters_list:
            attempts -= 1
            print("This guess is not correct!!!")
            
            
        word_presentation(secret_word, guess)
        
        
    
    show_result(secret_word,word_presentation(secret_word,display_word,guess) )


hangman_game()


