# 2. Filtering even numbers
# nums to check 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


list_of_strings = input().split(",")

list_of_int = [int(str) for str in list_of_strings]
filtered = [num for num in list_of_int if num % 2 != 0]

print(list_of_int)
print(filtered)
