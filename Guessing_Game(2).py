secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("guess the word: ")
        guess_count += 1
    else:
        print("you lose")
        out_of_guess = True
if not out_of_guess:
    print("you win")
