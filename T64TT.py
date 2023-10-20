n=(2,9,5,3)
z=0

def find_max(n):
    for i in n:
        s=set(n)
        if s != z:
            z=z+1
            print(z)
find_max(n)