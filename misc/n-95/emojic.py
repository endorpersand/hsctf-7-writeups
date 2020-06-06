def emojic(input):
    varr = [0] * 15
    for i in range(13): varr[i] = ord(input[i])
    
    if varr[1] != varr[12]:
        varr[11] -= varr[0]
    if varr[1] != varr[5]:
        varr[2] = varr[7]
    varr[1] -= varr[4]
    varr[9] += varr[6]
    if varr[4] != varr[9]:
        varr[13] = varr[3]
    varr[2] -= 8
    varr[3] = varr[12]
    varr[12] = varr[13]
    varr[1] += varr[7]
    varr[1] -= varr[3]
    varr[0] += varr[11] 
    varr[2] += 4
    varr[3] += 2
    #assert varr[3] == varr[5]
    if varr[4] != varr[9]:
        varr[4] += varr[9]
    varr[11] += 1
    varr[10] -= 8
    varr[7] += varr[8]
    varr[5] -= varr[6]
    if varr[10] != 4:
        varr[6] += varr[8]
    varr[8] += 8
    varr[0] -= varr[2]
    varr[4] -= varr[11]
    varr[2] += varr[2]
    varr[7] -= varr[11]
    if varr[10] != 0:
        varr[9] -= varr[1]
    return varr[:13]