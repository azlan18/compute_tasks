# Add a list of elements to a set
set1 = {1, 2, 3}
list_to_add = [3, 4, 5]
set1.update(list_to_add)
print("Set after adding elements:", set1)

# Return a new set of identical items from two sets
set2 = {3, 4, 5, 6}
intersection_set = set1.intersection(set2)
print("Intersection of two sets:", intersection_set)

# Get only unique items from two sets
unique_items_set = set1.symmetric_difference(set2)
print("Unique items from two sets:", unique_items_set)

# Update the first set with items that don’t exist in the second set
set1.difference_update(set2)
print("Set1 after updating with items not in Set2:", set1)

# Remove items from the set at once
items_to_remove = {1, 2}
set1.difference_update(items_to_remove)
print("Set1 after removing items:", set1)
