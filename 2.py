
# Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_set = set(submitted)
attended_set = set(attended)

both_set = submitted_set.intersection(attended_set)

both_list = list(both_set)

print("Students who both submitted their assignments and attended the class:", both_list)

# Task 2
identical_lists = sorted(submitted) == sorted(attended)
print(f"Are the lists identical regardless of order?", identical_lists)

# Task 3
attended.pop(1)
attended.pop(-1)
print(f"Attended list after removing students who didn't submit:", attended)




