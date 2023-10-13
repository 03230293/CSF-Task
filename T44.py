user_name=input()
#print(len(user_name))
# vowels=('a','e', 'i', 'o', 'u')
c=0
while user_name:
    if user_name[0] in ['a','e', 'i', 'o', 'u']:
        c=c+1
    user_name=user_name[1:]
print(c)