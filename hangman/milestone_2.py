import random

word_list = ["orange", "apple", "banana", "watermelon", "kiwi"]
print(word_list)
word = random.choice(word_list)
print(word)


def user_guess():
    guess = input("Enter a letter")
    if(len(guess) == 1 and guess.isalpha()):
        print("Good guess!")
        return guess
    else:
        print("Oops! That is not a valid input.")
        user_guess()

guess = user_guess()
print(guess)