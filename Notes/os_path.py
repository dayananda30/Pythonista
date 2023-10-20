# Join Paths

import os
os.path.join('a','b','c')

"""
The advantage of using os.path is that it allows code to remain compatible over all operating systems, as this uses
the separator appropriate for the platform it's running on.

For example, the result of this command on Windows will be:
>>> os.path.join('a', 'b', 'c')
'a\b\c'


In an Unix OS:
>>> os.path.join('a', 'b', 'c')
'a/b/c'

>>> p = os.path.join(os.getcwd(), 'foo.txt')
"""

