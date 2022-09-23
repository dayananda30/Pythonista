from collections import Counter
test_list = ["gegek", "gfgk", "kingg"]

occurances = {}
for item in test_list:
        occurances[item] = dict(Counter(item))
print(occurances)

visited = occurances.values()[0]
print(occurances.values())
for item in occurances.values():
    for key in item.keys():
        if not 




