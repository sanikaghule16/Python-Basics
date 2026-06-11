import random
words = ["python", "java", "code"]
word = random.choice(words)
guessed = ""
turns = 5
while turns > 0:
    display = ""
    for ch in word:
        if ch in guessed:
             display += ch
        else:
             display += "_"
    print(display)
    if display == word:
        print("You win!")
        break
    guess = input("Guess a letter: ")
    guessed += guess
    if guess not in word:
        turns -= 1
        print("Wrong! Turns left:", turns)
