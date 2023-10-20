
user_inputs = []
for i in range(3):
    num = int(input("Enter a number: "))
    user_inputs.append(num)
def is_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")
is_even(user_inputs)