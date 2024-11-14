# Q1) Use a While Loop to count down from n to 1.

def countdown(n):
    while n > 0:
        print(n)
        n -= 1

num = int(input("Enter a number to count down from: "))
countdown(num)
