sec_word = "George"
the_word = ""
guess=0
guess_limit = 5
while the_word != sec_word and guess < guess_limit:
    the_word = input("Enter guess: ")
    guess += 1
if guess == guess_limit:
    print("You lose")
else:
    print("You win")