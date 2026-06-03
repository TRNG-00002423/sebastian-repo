import random 
answer = random.randint(1, 100)
guesses_taken = 0
guess = -1

while guesses_taken < 7 and guess != answer:
    guess = int(input("Guess the number: "))
    
    if guess > answer:
        print("Lower!")
    elif guess < answer:
        print("Higher!")
    else:
        print("You got it!")
        break
    guesses_taken += 1

print(f"The number was: {answer}")


