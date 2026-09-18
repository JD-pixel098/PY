starting_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_inefficient_list = []

for i in starting_numbers:
    my_inefficient_list.append(i + 10)

print(my_inefficient_list)

new_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
my_efficient_list = []
for i in new_list:
    my_efficient_list.append(i + 10)
print(my_efficient_list)
