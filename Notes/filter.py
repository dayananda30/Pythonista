"""
filter(function, iterable)

To filter or discard elements of a sequence based on some condition.
"""

names = ['Daya', 'Soma', 'Manja', 'Raju', 'Dayananda', 'Somashekhar', 'Manjunatha']


def get_names_of_size_four(name):
    return len(name) == 4


print(list(filter(get_names_of_size_four, names)))
