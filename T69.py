string=input()
char=input()

def count_chars(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(count)
count_chars(string, char)