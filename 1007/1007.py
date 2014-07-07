n = 2001
start = 0.000
for i in range(0, n):
    summation = 0
    if start == 0.000:
        summation = 1.644934066848
    elif start == 0.500:
        summation = 1.227411277760
    elif start == 1.000:
        summation = 1.000000000000
    elif start == 2.000:
        summation = 0.750000000000
    else:
        for j in range(1, 120):
            item = 1 / (j * j * (j + 0.5) * (j + 1) * (j + 2) * (j + start))
            summation = summation + item
        summation = (((summation * (0.5 - start) + 0.1218373261546668) * (- start) + 0.19746703342399996) * (2 - start) + 0.25) * (1 - start) + 1
    print "%5.3f %16.12f" % (start, summation)
    start = start + 0.001
