# Q2) Write a Python code to print the number pattern using a loop.

def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
num_rows = int(input("Enter the number of rows: "))
print_pattern(num_rows)
