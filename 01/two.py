# Q2) Print the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    print("Fibonacci sequence:", ', '.join(map(str, sequence[:n])))

# Example usage
num = int(input("Enter the number of terms: "))
if num > 0:
    fibonacci(num)
else:
    print("Please enter a positive integer.")

