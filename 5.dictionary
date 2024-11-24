#A#Sort a dictionary in ascending and descending order by its keys


import operator

# Original dictionary
dict = {1: 12, 3: 14, 4: 13, 2: 11, 0: 10}
print("The original dictionary is:", dict)

# Sorting in ascending order by key
ascending = sorted(dict.items(), key=operator.itemgetter(0))
print("Dictionary in ascending order by key:", ascending)

# Sorting in descending order by key
descending = sorted(dict.items(), key=operator.itemgetter(0), reverse=True)
print("Dictionary in descending order by key:", descending)

#B#Combine multiple dictionaries into one

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}

for i in (dict1, dict2, dict3):
    dict4.update(i)

print(dict4)

#C#Find the sum of all values in a dictionary
dict={'data1':140,'data2':-54,'data3':315}
print(sum(dict.values()))
