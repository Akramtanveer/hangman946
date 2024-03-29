import random




def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while(True):
        guess = input("Enter a letter")
        if len(guess) == 1 and guess.isalpha():
            break
        print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

fruit_list = ["orange", "apple", "banana", "watermelon", "kiwi"]
word = random.choice(fruit_list)
print(word)
ask_for_input()
