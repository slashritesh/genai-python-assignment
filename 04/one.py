# Q1) Find the sum of all elements in a list.

numbers = []

for num in range(0,6,1):
    value = int(input("Enter 5 elements : "))
    numbers.append(value)

print(numbers)

total_sum = 0

for i in range(0,6,1):
    total_sum = total_sum + numbers[i]

print(total_sum)  