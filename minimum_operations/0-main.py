#!/usr/bin/python3
"""testing file
"""

minOperations = __import__('0-minoperations').minOperations

n = 2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 16
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
