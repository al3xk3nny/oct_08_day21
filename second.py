# x = input("Enter a number: ")
# y = input("Enter another number: ")

# x = int(x)
# y = int(y)

# print(x + y)


# Challenge

secret = input("Enter a number (1->100): ")
secret = int(secret)

while True:
    guess = input("Enter a guess: ")
    guess = int(guess)
    
    if guess == secret:
        print("You got it")
        break
        
    if guess < secret:
        print("Too low")
        
    if guess > secret: 
        print("Too high")