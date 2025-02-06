import random

def guess_number():
    num = random.randint(1, 100)
    while True:
        guess = int(input("Guess the number: "))
        if guess > num:
            print("Your number is higher")
        elif guess < num:
            print("Your number is lower")
        else:
            print("Congrats! You guessed the correct number!")
            break  

def main():
    guess_number()

main()
