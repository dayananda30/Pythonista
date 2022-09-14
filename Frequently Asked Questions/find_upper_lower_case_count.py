def find_upper_lower_count(input_string):
    upper_count = sum([1 for item in input_string if item.isupper()])
    lower_count = sum(1 for item in input_string if item.islower())
    # Above for loop returns a list which has list of 1's which are equal to number of uppercase letters.
    # upper_count = sum ([iterator])
    print(upper_count)
    print(lower_count)


find_upper_lower_count("Today is Best Day to Start Work")

"""
sum functions expects iterables of type integer not strings hence we are returning 1.
syntax: 
    sum([1,2,3,4,5]) --> sum([1,2,3,4,5],0)
    sum([1,2,3,4,5], 10) --> If we want to start counting from 10.
"""
