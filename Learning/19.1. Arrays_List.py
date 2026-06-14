
# ? Operation Complexity
# Access by Index	        O(1)
# Update	                O(1)
# Search	                O(n)
# Insert at End	            O(1)
# Insert in Middle	        O(n)
# Delete	                O(n)

list1 = ["Roaunak", "Aashika", "Uday", "Meenu", "Sumit", "Manish","Roaunak"]
print(list1[2])
print(list1[-2])  # Negative index used to find the backword indexing.

# Adding Data to the list
list1.append("Gaurav")
print(list1)

# Insert Data on Spesific Index
list1.insert(2, "Satyam")
print(list1)

# Modifying Elements
list1[1] = "Puchki"
print(list1)

# Remove Elements form list
list1.remove("Manish")
print(list1)

# Remove Element by index
list1.pop(3)
print(list1)

# Lenth of List
print(f"Length of List : {len(list1)}")

# Traversing a List
for name in list1:
    print(name)

# Searching in List:
if "Uday" in list1:
    print("Founded")
else:
    print("Not Found")

# Sort the list
list1.sort()
print("Shorted List : " ,list1)

# Reverse the list
list1.reverse()
print("Reversed List : " ,list1)

# Count the Occurrences of the value
print(list1.count("Roaunak"))

# Find and give the first occurrence index of the value if exist and if not give error
print(list1.index("Roaunak"))