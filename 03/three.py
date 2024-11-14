# Q3) Print the list in reverse order using a loop

def print_reverse(input):
    for i in range(len(input) - 1, -1, -1):
        print(input[i])


my_list = [1, 2, 3, 4, 5]
print("List in reverse order:")
print_reverse(my_list)
