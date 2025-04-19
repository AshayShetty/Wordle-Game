import random # to choose random word

# converts text file into list
def load_dictionary(file_path): 
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


# checks if the guessed word is an English 5 lettered word
def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses


# evaluation of the guessed word
def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i] + " " # makes the matching letter green
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i] + " "# makes the correct letter nut wrong position yellow
            else:
                str += "\033[0m" + guess[i] + " " # default
    
    return str + "\033[0m"


# checks if the user wants to continue playing
def play_again():
    ans = input("\n Do you want to Play again? (y/n) \n")
    if ans=="y":
        wordle(guesses , answers)
    else:
        exit()

# takes user guesses and gives results
def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")
    secret_word = random.choice(answers).lower() # converts all letters of secret word into smaller case

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower() # converts all letters of guessed word into smaller case
        
        if not is_valid_guess(guess, guesses):
            print("Invalid guess.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            play_again()
            

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
    
    if attempts > max_attempts:
        print("Game over. The secret word was:", secret_word)
        play_again()


guesses_dictionary = "guesses.txt" # contains the valid words
answers_dictionary = "answers.txt" # contains the words that game chooses

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

wordle(guesses, answers) # calling the function


