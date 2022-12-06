import numpy as np

def day1(text_file):
    f = open(text_file, "r")
    cals = f.readlines()
    i = 0
    buffer = []
    top3 = [0, 0, 0]
    answer = 0
    for cal in cals:
        if cal.strip() =='':
            i+=1
            sum1 = sum(buffer)
            buffer = []
            if sum1 > top3[0]:
                top3.append(sum1)
                top3.sort()
                top3.pop(0)

            # if sum1 > answer:
            #     num = i #nth elf
            #     answer = sum1
            continue
        buffer.append(int(cal))
    return(top3[2], np.sum(top3))
        

part1, part2 = day1("input1.txt")
print(part1, part2)