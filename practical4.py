#practical4a:Check if two lists have any common elements.
def find_common(st1, st2):
    res = False
    for x in st1:
        for y in st2:
            if x == y:
                res = True
    return res

print(find_common([4, 6, 8, 10, 12], [5, 7, 8, 10, 11]))  # Output: True
print(find_common([3, 5, 7, 9, 11], [2, 4, 6, 8]))        # Output: False

#practical4b:Remove elements from a list by their index.
list = [10, 15, 20, 25, 30, 35, 40, 45]
print("List after removing the 0th, 2nd, 4th, and 5th elements:")

list = [x for i, x in enumerate(list) if i not in (0, 2, 4, 5)]
print(list)

#practical4c:#Create an exact copy of a list
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
clonelist = list(list1)
print("Original list:", list1)
print("Cloned list:", clonelist)

