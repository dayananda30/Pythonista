import sys

for line in sys.stdin:
    print(line)

"""
Be aware that sys.stdin is a stream. It means that the for-loop will only terminate when the stream has ended.
You can now pipe the output of another program into your python program as follows:

$cat myfile | python myprogram.py

"""

