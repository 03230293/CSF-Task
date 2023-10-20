
def reverse_string(string):
    # initialize an empty string to store the reversed string
    reversed_string = ""
    # loop through the original string from the end to the beginning
    for i in range(len(string) - 1, -1, -1):
        # append each character to the reversed string
        reversed_string += string[i]
    # return the reversed string
    return reversed_string
