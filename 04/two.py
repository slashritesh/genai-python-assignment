# Q2) Count how many times an element appears in a list.

numbers = [10,21,10,10,23,45,9,27]
count = 0

value = int(input("Cheak element repeated : "))

if value in numbers:
    for i in numbers:
        if i == value:
            count += 1
    
    print(f"{value} is appered in array {count} times")
else : 
    print("value does't exist in array!")


