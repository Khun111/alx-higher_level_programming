#!/usr/bin/python3
if __name__ == "__main__":
    import hidden4
printeds = dir(hidden4)
for i in printeds:
    if i[:2] is not '__':
	    print(i)
