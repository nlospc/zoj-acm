import sys

def getrotor(j, alpha):
    return ord(alpha) - ord('A') - j

def rotor_roll(n, m):
    temp = []
    temp = rotor[0][0 : n-1]
    temp.insert(0, rotor[0][n-1])
    rotor[0] = temp
    if m / n > 0 and m % n == 0:
        temp = []
        temp = rotor[1][0 : n-1]
        temp.insert(0, rotor[1][n-1])
        rotor[1] = temp
    if m / n > 1 and m % (n * n) == 0:
        temp = []
        temp = rotor[2][0 : n - 1]
        temp.insert(0, rotor[2][n - 1])
        rotor[2] = temp

def rotor_match(n, rotor_ind, index):
    for i in range(0, n):
        if (i + rotor[rotor_ind][i]) % n== index:
            return i

def rotor_decode(text_cry, n):
    text_plain = ''
    num = 0
    for i in range(0, len(text_cry)):
        index = (ord(text_cry[i]) - ord('A')) % n
        index = rotor_match(n, 2, index)
        index = rotor_match(n, 1, index)
        index = rotor_match(n, 0, index)
        text_plain = text_plain + chr(index + ord('A'))
        num = num + 1
        rotor_roll(n, num)
    return text_plain


n = int(sys.stdin.readline())
num = 0
while n:
    rotor_origin = []
    rotor = []
    tep = []
    plain = []
    num = num + 1
    for i in range(0, 3):
        temp = sys.stdin.readline()
        for j in range(0, n):
            tep.insert(j, getrotor(j, temp[j]))
        rotor_origin.insert(i, tep)
        tep = []
    rotor = rotor_origin[:]
    m = int(sys.stdin.readline())
    for j in range(0, m):
        temp_cry = sys.stdin.readline().strip('\n')
        plain.append(rotor_decode(temp_cry, n));
        rotor = rotor_origin[:]
    if num > 1:
        print
    print 'Enigma ' + str(num) + ':'
    for k in range(0, m):
        print plain[k].lower()
    n = int(sys.stdin.readline())
