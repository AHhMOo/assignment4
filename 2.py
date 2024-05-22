
# Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Convert lists to sets for easier comparison
submitted_set = set(submitted)
attended_set = set(attended)

# Find the intersection of the two sets
both_submitted_and_attended = submitted_set.intersection(attended_set)

print("Students who both submitted their assignments and attended the class:")
print(both_submitted_and_attended)

# Task 2
identical_lists = sorted(submitted) == sorted(attended)
print(f"Are the lists identical regardless of order?", identical_lists)

# Task 3
attended.pop(1)
attended.pop(-1)
print(f"Attended list after removing students who didn't submit:", attended)




