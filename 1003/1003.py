import sys

def check_score(high, low, n):
    for i in range(n, 1, -1):
        if low % i == 0:
            if check_score(high, low / i, i - 1):
                return True
        if high % i == 0:
            if check_score(high / i, low, i - 1):
                return True
    global flag
    if low == 1:
        flag = True
    elif not flag:
        return True
    if high == 1 and low == 1:
        return True
    if high == 1 and not flag:
        return True
    return False



line = sys.stdin.readline()
while line:
    scores = line.split()
    high = int(scores[0])
    low = int(scores[1])
    if low > high:
        tep = low
        low = high
        high = tep
    winner = high
    flag = False
    if not check_score(high, low, 100):
        winner = low
    print winner
    line = sys.stdin.readline()
