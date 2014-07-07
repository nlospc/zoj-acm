import sys

def sour_ind(source, tar):
    ind_num = 0
    indexs = []
    sour_len = len(source)
    for i in range(0, sour_len):
        if source[i] == tar:
            indexs.append(i)
            ind_num = ind_num +1
    return indexs,ind_num

def check(source, target, pos_out):
    num_in = -1
    num_check = 0
    check_str = ''
    for i in range(0, pos_out):
        if sequen[i] == 'i':
            num_in = num_in + 1
            stack[num_check] = source[num_in]
            num_check = num_check + 1
        elif sequen[i] == 'o':
            check_str = check_str + stack[num_check - 1]
            num_check = num_check - 1
    if check_str == target:
        return True
    else:
        return False


def anagrams(source, target, pos_out, pos_tar):
    global n
    if pos_tar == n or pos_out == n * 2:
        if check(source, target, pos_out):
            output = ''
            for i in range(0, pos_out):
                if i == 0:
                    output = sequen[i]
                else:
                    output = output + ' ' +sequen[i]
            output = output + ' '
            if output not in result:
                result.append(output)
                global result_num
                result_num = result_num + 1
        return
    tar = target[pos_tar]
    indexs = []
    indexs,ind_num = sour_ind(source, tar)
    global count
    global sour_flag
    sour_flag_tep = []
    sour_flag_tep = sour_flag[:]
    pos_out_tep = pos_out
    count_tep = count
    for i in range(ind_num - 1, -1, -1):
        index = indexs[i]
        sour_flag = sour_flag_tep[:]
        pos_out = pos_out_tep
        count = count_tep
        if sour_flag[index] == 'unmatch':
            for j in range(0, index - count):
                sequen[pos_out] = 'i'
                pos_out = pos_out + 1
            sequen[pos_out] = 'o'
            pos_out = pos_out + 1
            sour_flag[index] = 'matched'
            if index > count:
                count = index
            anagrams(source, target, pos_out, pos_tar + 1)



line_sour = sys.stdin.readline().strip('\n')
line_targ = sys.stdin.readline().strip('\n')
while line_sour and line_targ:
    count = -1
    sequen = []
    sour_flag = []
    stack = []
    result = []
    result_num = 0
    n = len(line_targ)
    for i in range(0, n):
        sour_flag.append('unmatch')
        stack.append('')
        sequen.append('')
        sequen.append('')
    print '['
    anagrams(line_sour, line_targ, 0, 0)
    for i in range(0,result_num):
        print result[i]
    print ']'
    line_sour = sys.stdin.readline().strip('\n')
    line_targ = sys.stdin.readline().strip('\n')
