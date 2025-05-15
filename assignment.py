# 1. Create an empty list called my_list
my_list = []
print("1. Empty list created:", my_list)

# 2. Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2. After appending elements:", my_list)

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("3. After inserting 15 at position 2:", my_list)

# 4. Extend with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("4. After extending with [50, 60, 70]:", my_list)

# 5. Remove the last element
removed_element = my_list.pop()
print(f"5. Removed last element ({removed_element}):", my_list)

# 6. Sort in ascending order
my_list.sort()
print("6. After sorting in ascending order:", my_list)

# 7. Find and print the index of 30
index_of_30 = my_list.index(30)
print("7. Index of value 30:", index_of_30)
