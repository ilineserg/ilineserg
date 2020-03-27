def short_string(weight):
    alpha = []
    num = 1
    step = 0
    for i in range(65, 91):
        letter = chr(i)
        if letter == 'A':
            alpha.append((num, letter))
            num += 1
            step +=1
        else:
            previous = alpha[step-1][0]
            alpha.append((num * previous + previous, letter))
            num += 1
            step += 1

    STRING = ''

    while weight != 0:
        for i in reversed(w):
            if weight < i[0]:
                continue
            else:
                STRING += i[1]
                weight -= i[0]
                
    return ''.join(sorted(STRING))
