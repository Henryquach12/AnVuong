import random
class WordGuesser:
    def __init__(self):
        self.file = "Week 1\pokemon-2.txt"
    def choose_word(self):
        with open(self.file, "r") as file:
            data = file.read()
        words = data.split(",")
        clean_words = []
        for word in words:
            clean_words.append(word.strip().lower())
        return random.choice(clean_words)

    def display_word(self, hidden_word, guessed_letters):
        progress = ""
        for letter in hidden_word:
            if letter in guessed_letters:
                progress += letter
            else:
                progress += "_"
        return progress

    def play_game(self):
        hidden_word = self.choose_word()          
        guessed_letters = []                 
        turns = 0
        while True:
            print("Turn:", turns + 1)
            progress = self.display_word(hidden_word, guessed_letters)
            print("Word:", progress)
            if "_" not in progress:
                print("Congratulations! You guessed the word:", hidden_word)
                print("It took you", turns, "turns.")
                break
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single alphabetical letter.")
                continue
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            guessed_letters.append(guess)
            turns += 1
        return progress
word_guesser = WordGuesser()
word_guesser.play_game()