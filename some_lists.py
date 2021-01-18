my_list = [5, 9, 6, 10, 4]
# print the first item
print(my_list[0])

# appending to the end of a list is O(1)
my_list.append("foo")

# removing an item from the end O(1)
my_list.pop()

numbers = [1, -5, 0, 10, 100, 67, 55, 20, 34]

new_list = [num for num in numbers if num % 2 == 0]
print(new_list)

# list comprehension as opposed to regular for loops
names = ['Adam', 'Kevin', 'Anna', 'Joe', 'Bill', 'Alex']
filtered_names = [name for name in names if name.startswith('A')]

# for name in names:
#     if name.startswith('A'):
#         filtered_names.append(name)

print(filtered_names)
