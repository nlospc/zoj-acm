import sys

def jugs(ca, cb, n):
    a = 0
    b = cb
    print 'fill B'
    while b != n:
        print 'pour B A'
        if ca - a < b:
            print 'empty A'
            b = b - ca + a
            a = 0
        else:
            print 'fill B'
            a = a + b
            b = cb
    print 'success'
    return


line = sys.stdin.readline()
while line:
    puzzle = line.split()
    ca = int(puzzle[0])
    cb = int(puzzle[1])
    n = int(puzzle[2])
    jugs(ca, cb, n)
    line = sys.stdin.readline()
