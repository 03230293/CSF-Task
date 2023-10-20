string=input()
char=input()

def count_chars():
    for i in range(len(string)):
        if (string[i]==char):
            count=0
            count=count+1
            print(count)
        
count_chars()