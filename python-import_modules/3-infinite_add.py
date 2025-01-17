#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addargs = 0
    for i in range(1, len(sys.argv)):
        addargs += int(sys.argv[i])
    print(addargs)
