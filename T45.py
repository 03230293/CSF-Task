user_name=input()
# print(len(user_name))
vowels=('a','e', 'i', 'o', 'u')
v=0
for i in user_name: 
    if i in vowels:
        v=v+1
print("vowels in name", v)