
#empty_list.py# This file initializes an empty list named `my_list`.
my_list = []

another_list = [50, 60, 70]  # This is another
#my_list.py# This file appends several integers to the list `my_list`.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)  # Output the contents of my_list
# This will print: [10, 20, 30, 40]
my_list.insert(2, 15)  # Insert 15 at index 2
print(my_list)  # Output the updated contents of my_list

my_list.extend(another_list)  # Extend my_list with another_list
print(my_list)  # Output the final contents of my_list
