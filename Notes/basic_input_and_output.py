# Input from a file

# let's create an example file:
with open('shoppinglist.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')
with open('shoppinglist.txt', 'r') as fileobj:
    # this method makes a list where each line
    # of the file is an element in the list
    lines = fileobj.readlines()

"""
If the size of the file is tiny, it is safe to read the whole file contents into memory. 
If the file is very large it is often better to read line-by-line or by chunks, and process the input in the same loop.
"""

with open('shoppinglist.txt', 'r') as fileobj:
    # this method reads line by line:
    lines = []
    for line in fileobj:
        lines.append(line.strip())


"""
Note: When reading files, be aware of the operating system-specific line-break characters. Although for line in
fileobj automatically strips them off, it is always safe to call strip() on the lines read, as it is shown above
"""

"""
When they are first opened the file handle points to the very beginning of the file, which is the position 0. 
The file handle can display its current position with tell
"""

fileobj = open('shoppinglist.txt', 'r')
pos = fileobj.tell()
print('We are at %u.' % pos) # We are at 0.

"""
The file handler position can be set to whatever is needed:
"""

fileobj = open('shoppinglist.txt', 'r')
fileobj.seek(7)
pos = fileobj.tell()
print('We are at character #%u.' % pos)

"""
You can also read any length from the file content during a given call. To do this pass an argument for read()
"""

# reads the next 4 characters
# starting at the current position
next4 = fileobj.read(4)
# what we got?
print(next4) # 'cucu'
# where we are now?
pos = fileobj.tell()
print('We are at %u.' % pos) # We are at 11, as we was at 7, and read 4 chars.
fileobj.close()



