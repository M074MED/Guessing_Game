secret_word = "python"
guess = input("guess the word: ")
guess_count = 0
while guess != secret_word:
    if guess_count < 2:
        guess = input("guess the word: ")
        guess_count += 1
    else:
        print("you lose")
        break
if guess == secret_word:
    print("you win")
