
user_inputs = []
for i in range(3):
    user_input = int(input("Enter a number: "))
    user_inputs.append(user_input)
user_inputs.append(10)

def is_even(user_inputs ):
    for number in user_inputs:
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")
is_even(user_inputs )