
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = 0
for i in range(num1, num2 + 1):
    sum += i
print("The sum of all numbers between", num1, "and", num2, "is", sum)