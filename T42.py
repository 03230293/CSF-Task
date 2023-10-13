user_name=input()
vowels=['a','e', 'i', 'o', 'u']
vowel_found= False

while user_name != "":
    for a in user_name:
        if a in vowels:
            vowel_found=True
    break
print(vowel_found)

