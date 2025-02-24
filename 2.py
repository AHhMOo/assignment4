submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#1
if attended[0] in submitted :
    print(attended[0]+" has submitted their assignments and attended the class")
if attended[1] in submitted :
    print(attended[1]+" has submitted their assignments and attended the class")
if attended[2] in submitted :
    print(attended[2]+" has submitted their assignments and attended the class")
if attended[3] in submitted :
    print(attended[3]+" has submitted their assignments and attended the class")

#2

submitted.sort()
attended.sort()
if submitted == attended :
    print("lists are identical")

#3
if attended[3] not in submitted :
    attended.remove(attended[3])
if attended[2] not in submitted :
    attended.remove(attended[2])
if attended[1] not in submitted :
    attended.remove(attended[1])
if attended[0] not in submitted :
    attended.remove(attended[0])
print(attended)
