import random
secret_number=random.randint(1,100)
# int(input())
print(secret_number)
while True:
    guess=int(input())
    if guess==secret_number:
        print("You guess the right secret number")
        break
    elif guess > secret_number:
        print("It is too high")
    else: 
        print("It is too low")
    
        
