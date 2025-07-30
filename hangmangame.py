import random

words = ["apple", "chair", "table", "house", "light"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("You win! The word is:", word)
else:
    print("You lose. The word is:", word)
