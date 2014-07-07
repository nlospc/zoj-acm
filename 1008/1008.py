import sys

def checkset(n, row, col, i):
    if row < 1 and col < 1:
        return True
    if row < 1:
        if termination[row][col - 1][1] == squares[i][3]:
            return True
        else:
            return False
    elif col < 1:
        if termination[row - 1][col][2] == squares[i][0]:
            return True
        else:
            return False
    else:
        if termination[row][col - 1][1] == squares[i][3] and termination[row - 1][col][2] == squares[i][0]:
            return True
        else:
            return False

def tetravex(n, position, diff):
    global solve
    if solve == 1:
        return
    if position == n * n:
        solve = 1
        return
    row = position / n
    col = position % n
    for i in range(0, diff):
        if flag[i] > 0:
            if checkset(n, row, col, i):
                termination[row][col] = squares[i]
                flag[i] = flag[i] - 1
                tetravex(n, position + 1, diff)
                flag[i] = flag[i] + 1



n = int(sys.stdin.readline())
count = 0
while n:
    count = count + 1
    squares = []
    termination = []
    flag = []
    diff = 0
    for i in range(0, n):
        tep = []
        for j in range(0, n):
            temp = sys.stdin.readline().split()
            tep.append('')
            if temp in squares:
                ind = squares.index(temp)
                flag[ind] = flag[ind] + 1
            else:
                squares.append(temp)
                flag.append(1)
                diff = diff + 1
        termination.append(tep)
    position = 0
    solve = 0
    tetravex(n, position, diff)
    if count > 1:
        print ""
    if solve == 1:
        print "Game "+ str(count) +": Possible"
    else:
        print "Game "+ str(count) +": Impossible"
    n = int(sys.stdin.readline())
