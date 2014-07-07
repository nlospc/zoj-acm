import sys

def chartoint(rule_char):
    for i in range(0, 28):
        if rule[i] == rule_char:
            return i

def twist(key, cipher):
    n = len(cipher)
    plaincode = []
    ciphercode = []
    plaintext = ''
    for i in range(0, n):
        plaincode.append('')
        ciphercode.append(chartoint(cipher[i]))
    for j in range(0, n):
        plaincode[key * j % n] = (ciphercode[j] + j) % 28
    for k in range(0, n):
        plaintext = plaintext + rule[plaincode[k]]
    print plaintext

line = sys.stdin.readline().strip('\n')
endflag = 1
if len(line) == 1:
    endflag = int(line)
rule = []
for i in range(0,28):
    if i == 0:
        rule.append('_')
    elif i == 27:
        rule.append('.')
    else:
        rule.append(chr(i + 96))
while line and endflag != 0:
    case = line.split()
    key = int(case[0])
    cipher = case[1]
    twist(key, cipher)
    line = sys.stdin.readline().strip('\n')
    endflag = 1
    if len(line) == 1:
        endflag = int(line)
