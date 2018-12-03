"""
1. Create A List Of Prime Numbers Up To 100.
2. Display all Dictionary Lists when finished.
"""
from IsPrime import IsPrime
primeDivide = { }

for i in range(1, 101):
    if IsPrime(i):
        primeDivide[i] = []

for i in range(1, 101):
    for num in primeDivide:
        if i % num == 0:
            primeDivide[num].append(i)

for key, val in primeDivide.items():
    print("Key: %s" % (key))
    print("Val: %s" % (val))