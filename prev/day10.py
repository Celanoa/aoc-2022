import numpy as np
def day10(text_file,outputs):
    f = open(text_file, "r")
    inputs = f.readlines()
    nums = np.arange(20,20+40*outputs,40)
    signal = []
    sprite = np.arange(0,3)
    screen = []
    x = 1
    j = 0
    for i, data in enumerate(inputs):
        data = data.strip()
        if j%40 in sprite:
            screen.append('###')
        else:
            screen.append('...')
        j+=1
        if j%40 in nums:
            signal.append(j*x)
        if data != 'noop':
            if j%40 in sprite:
                screen.append('###')
            else:
                screen.append('...')
            j+=1
            if j in nums:
                signal.append(j*x)
            amt = int(data.split(' ')[1])
            x += amt
            sprite += amt
    answer = sum(signal)
    print_scr(screen)
    return(answer)

def print_scr(screen):
    for i in range(len(screen)):
        if i%40 == 0:
            if i!=0:
                print(string)
            string = ''
        string+=screen[i]
    print(string)



answer = day10("input10.txt",6)
print(answer)


