import random
from words import words

word = random.choice(words)

print("\n\nWelcome to Python Wordle!")
print("Guess the 5 letter word. You have 10 attempts.\n\n")

for attempt in range(10):
    guess = input(f"\nGuess {attempt + 1}/10: ").lower()

    if len(guess) != 5:
        print("Please enter exactly 5 letters.\n")
        continue

    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += guess[i].upper()  
        elif guess[i] in word:
            result += guess[i]         
        else:
            result += "_"               

    print(result)

    if guess == word:
        print("\nYou got it!")
        break
else:
    print(f"\nYou lost! The word was: {word}")
