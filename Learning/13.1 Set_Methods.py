collaction_1 = {1.3, "Roaunak Gupta", 24}
collaction_2 = {2, "Roaunak Gupta", "Puchki", (2024, 2025, 2026), 1.3, 24}

print(collaction_1)
collaction_1.add("B.Tech in CSE")  # This is an method to add data to set
print(collaction_1)
collaction_1.remove(1.3)   # This is an method to remove data to set
print(collaction_1)
# This the method of set to pop any random values from Set.
print(collaction_1.pop())
collaction_union = collaction_1.union(collaction_2) # This is the method to create union of the 2 sets
collaction_inter = collaction_1.intersection(collaction_2) # This is the method to create intersection of the 2 sets
print("This is the Union collaction of Sets", collaction_union)
print("This is the Intersection collaction of Sets", collaction_inter)

collaction_1.clear()  # This is an method to clear all elements of set
