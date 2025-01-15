#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i == 8 and j == 9:
            break
        elif i < j:
            print("{:d}{:d}, ".format(i, j), end='')
print(89)
