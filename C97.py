import random
print("Number guessing game")
number=random.randint(1,9)

chances = 0

while chances < 5 :
    guess=int(input("Enter your guess\n"))
    
    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your number is too high")
    else:
        print("Congratulations you won!!")
        break
    chances+=1

if not chances < 5:
    print("You lose!! The number is",number)
