"""
1. Make a Dictionary of Lists that stores numbers divisible by 2, 3, 5, & 7
2. Display all Dictionary Lists when finished.
"""

primeDivide = {"two":[], "three":[], "five":[], "seven":[], "eleven":[]}

for i in range(1, 101):
    if i % 2 == 0:
        primeDivide["two"].append(i)
    if i % 3 == 0:
        primeDivide["three"].append(i)
    if i % 5 == 0:
        primeDivide["five"].append(i)
    if i % 7 == 0:
        primeDivide["seven"].append(i)
    if i % 11 == 0:
        primeDivide["eleven"].append(i)

for key, val in primeDivide.items():
    print("Key: %s" % (key.capitalize()))
    print("Val: %s" % (val))