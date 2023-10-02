"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    stringlst = [str(x) for x in items]
    for x in stringlst:
        frequencies[x] = stringlst.count(x)

    return frequencies

print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))