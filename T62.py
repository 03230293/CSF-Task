user_inputs = []
for i in range(3):
    user_input = int(input("Enter a number: "))
    user_inputs.append(user_input)
user_inputs.append(10)

def is_even(user_inputs ):
    for number in user_inputs:
        if number % 2 != 0:
            print(False)
            break
        else:
            print(True)
is_even(user_inputs )

#or
# Create an empty array called user_inputs
user_inputs = []

# Get three user input of three numbers and add them to the array
for i in range(3):
    # Prompt the user to enter a number
    num = input(f"Enter number {i+1}: ")
    # Convert the input to an integer and append it to the array
    user_inputs.append(int(num))

# Write a function called is_even that takes in the user_inputs array as an argument
def is_even(array):
    # Loop through each element in the array
    for x in array:
        # Check if the element is not even
        if x % 2 != 0:
            # Return False and exit the function
            return False
    # If all elements are even, return True
    return True

# Call the function with the user_inputs array and print the result
result = is_even(user_inputs)
print(f"All numbers are even: {result}")
#Bing chat with GPT-4
