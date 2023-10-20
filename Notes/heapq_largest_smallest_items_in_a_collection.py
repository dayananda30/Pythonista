"""
heapq:
    Largest and smallest items in a collection

    To find the largest items in a collection, heapq module has a function called nlargest, we pass it two arguments,
    the first one is the number of items that we want to retrieve, the second one is the collection name. """

import heapq

numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(4, numbers))

# Similarly, to find the smallest items in a collection, we use nsmallest function

print(heapq.nsmallest(4, numbers))

# There is another optional argument - key that can be used for complex datastructure
people = [
 {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
 {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
 {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
 {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
 {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
 {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
]

oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
print(oldest)

