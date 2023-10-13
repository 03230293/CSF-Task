import random
secret_number=random.randint(1,100)
# int(input())
print(secret_number)
for i in range(1,100):
    guess=int(input())
    if guess==secret_number:
        print("You guess the right secret number")
        break
    elif guess > secret_number:
        print("It is too high")
    else: 
        print("It is too low")
if guess!=secret_number:
    print(secret_number)      
