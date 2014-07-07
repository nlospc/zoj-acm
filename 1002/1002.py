import sys

def checkx_row(check, row, col):
    for i in range(row - 1, check - 1, -1):
        if city[i][col] == 'X':
            return True
        elif city[i][col] == '*':
            return False
    return True

def checkx_col(check, row, col):
    for j in range(col - 1, check - 1, -1):
        if city[row][j] == 'X':
            return True
        elif city[row][j] == '*':
            return False
    return True

def checkset(n, row, col):
    if city[row][col] == 'X':
        return False
    for i in range(0, row):
        if city[i][col] == '*':
            if checkx_row(i, row, col):
                break
            return False
    for j in range(0, col):
        if city[row][j] == '*':
            if checkx_col(j, row, col):
                break
            return False
    return True

def getnum(n, position, num):
    if position == n * n:
        global max_num
        if num > max_num:
            max_num = num
        return
    row = position / n
    col = position % n
    if checkset(n, row, col):
        city[row][col] = '*'
        getnum(n, position + 1, num + 1)
        city[row][col] = '.'
    getnum(n,position + 1, num)


n = int(sys.stdin.readline())
while n:
    city = []
    tep = []
    max_num = 0
    for i in range(0, n):
        temp = sys.stdin.readline()
        for j in range(0, n):
            tep.insert(j, temp[j])
        city.insert(i, tep)
        tep = []
    position = 0
    num = 0
    temp_num = getnum(n, position, num)
    print max_num
    n = int(sys.stdin.readline())
