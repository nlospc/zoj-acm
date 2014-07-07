import sys
line = sys.stdin.readline()
while line:
    a = line.split()
    print int(a[0]) + int(a[1])
    line = sys.stdin.readline()
