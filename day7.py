def day7(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()
    # total_score = 0
    # total_score1 = 0
    # j=0
    # k=0
    directory = {}
    directory['/']={}
    cwd = []
    counter = 0
    total = {}
    total_memory = 0
    j = 0
    for i, data in enumerate(inputs):
        data = data.strip()
        cmds = data.split(' ')
        if cmds[0]=='$':
            if cmds[1]=='ls':
                continue
            if cmds[1]=='cd':
                if cmds[2]=='/':
                    continue
                elif cmds[2]=='..':
                    cwd.pop()
                else:
                    counter+=1
                    total[counter]=0
                    cwd.append(counter)
        elif cmds[0]=='dir':
            continue
        else:
            j+=1
            total_memory += int(cmds[0])
            total = adder(total,cwd,int(cmds[0]))

    answer = 0
    for key in total.keys():
        if total[key]<=100000:
            answer+=total[key]

    needed_space = total_memory - 4*10**7
    answer2 = 10**8 
    answer_key = 0
    temp = 0
    for j,key in enumerate(total.keys()):
        if total[key]>=needed_space:
            contender = total[key]
            if contender<answer2:
                answer2=contender
                answer_key = j
    return(answer,answer2)


def adder(total,dirs,inc):
    for dir in dirs:
        total[dir]+=inc
    return(total)



answer = day7('input7.txt')
print(answer)