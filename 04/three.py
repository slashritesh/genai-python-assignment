# Q3) Check if a particular element exists in a list.

numbers = []
flag : False

for num in range(0,6,1):
    value = int(input("Enter 5 elements : "))
    numbers.append(value)

print(numbers)

value = int(input("Enter the Value you want to cheak : "))

if value in numbers:
    print("element in array")
else :
    print("don't exist in array")