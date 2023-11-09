#Write a function called "reverse_string" that takes a string as an argument and returns the reverse of the string.
string=input()
def reverse_string(string):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    # Loop through the original string from the last character to the first
    for i in range(len(string) - 1, -1, -1):
        # Append each character to the reversed string
        reversed_string += string[i]
    # Return the reversed string
    return reversed_string
print(reverse_string(string))
reverse_string(string)