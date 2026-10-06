def overlapping(list1, list2):
# Get the length of both lists
    c = len(list1)
    d = len(list2)

# Iterate through each element in list1 
    for i in range(c):
# Compare each element in list1 with each element in list2 
        for j in range(d):
            if list1[i] == list2[j]:
                return 1 # Found a common element, return 1 return 0 # No common elements found, return 0
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

if overlapping(list1, list2): 
    print("overlapping")
else:
    print("not overlapping")
