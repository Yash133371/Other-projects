import random


num = random.randint(1, 100)
attempts = 0
print("Guess the random number between 1 and 100")
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer")
        continue
    
    if guess == num:
        attempts += 1
        break
    elif guess > num:
        print("Too big!")
        attempts += 1
    elif guess < num:
        print("Too small!")
        attempts += 1

if attempts == 1:
    print("You got it in just one attempt!")
else:
    print(f"You got it right in {attempts} attempts")