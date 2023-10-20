# Creating a dictionary
d = {}  # empty dictionary
otherdictionay = {'key': 'value'}  # dict with initial values
d = {**otherdictionay}  # makes a shallow copy of other dicitonary

# built in class
d = dict()
d = dict(key='value')
d = dict([('key', 'value')])
d = dict(**otherdictionay)

# Avoiding KeyError Exceptions
my_dict = {}
try:
    print(my_dict['nokey'])
except KeyError as keyerrException:
    print(keyerrException)

"""
One way to avoid key errors is to use the dict.get method, which allows you to specify a default value to return in
the case of an absent key
"""

value = my_dict.get('nokey', None)

# returns default value when key is not found.
print(value)

# Set the value if key doesn't exist, else update the value
my_dict.setdefault('nokey', 'novalue')
print(my_dict)

# Iterating over dictionary

for key, value in my_dict.items():
    print(key, value)

"""In Python, a defaultdict is a class provided by the collections module. It's a subclass of the built-in dict 
class, and it's used to create dictionaries with default values for keys that haven't been set yet. This can be quite 
useful when working with dictionaries, as it eliminates the need to check if a key exists before setting or 
retrieving its value. """

from collections import defaultdict

my_dict_new = defaultdict(int)
print(my_dict_new['key1'])  # 0
my_dict_new['key1'] = '10'
print(my_dict_new['key1'])  # 10


# Merging dictionaries
cars = {'Tata':'India', 'Mahindra':'India', 'Ford': 'USA'}
bikes = {'Honda':'Japan', 'Bajaj':'India'}

result = {**cars, **bikes}
print(result)

from collections import ChainMap
print(ChainMap(cars,bikes))


# Creating an ordered dictionary
"""
You can create an ordered dictionary which will follow a determined order when iterating over the keys in the
dictionary.
Use OrderedDict from the collections module. This will always return the dictionary elements in the original
insertion order when iterated over
"""
from collections import OrderedDict

d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4
# Outputs "first 1", "second 2", "third 3", "last 4"
for key in d:
 print(key, d[key])






