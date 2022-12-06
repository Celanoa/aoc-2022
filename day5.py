#         [M]     [B]             [N]
# [T]     [H]     [V] [Q]         [H]
# [Q]     [N]     [H] [W] [T]     [Q]
# [V]     [P] [F] [Q] [P] [C]     [R]
# [C]     [D] [T] [N] [N] [L] [S] [J]
# [D] [V] [W] [R] [M] [G] [R] [N] [D]
# [S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
# [N] [M] [F] [D] [R] [C] [W] [T] [M]
#  1   2   3   4   5   6   7   8   9 


def init_inputs(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()
    stacks = {}
    indices = []
    counts = 0
    for i, input in enumerate(inputs):
        # input = input.strip()   
        offset = len(input) - len(input.lstrip(' '))
        input = input.strip()   
        input = input.replace("\n","")
        if input == '':
            break
        for j, char in enumerate(input):
            if char.isalpha():
                index = (offset+j-1)//4+1
                check = indices.count(index)
                if check > 0:
                    stacks[index].insert(0,char)
                else:
                    stacks[index] = []
                    stacks[index].insert(0,char)
                    indices.append(index)
    new_stacks={}
    for i in sorted(stacks.keys()):
        new_stacks[i]=stacks[i]
    return(new_stacks)
            

def cmds(input):
    answers = []
    output = input.split(' ')
    for inputs in output:
        if inputs.isnumeric():
            answers.append(int(inputs))
    return(answers[0],answers[1],answers[2])


def day5(text_file, reverse=True):
    f = open(text_file, "r")
    inputs = f.readlines()
    total_score = 0
    total_score1 = 0
    j=0
    k=0
    flag = True
    stacks = init_inputs(text_file)
    for i, num in enumerate(inputs):
        buffer = []
        num = num.strip()
        num = num.replace("\n","")
        if num != '' and flag:
            continue
        if num == '':
            flag = False
            continue
        a,b,c = cmds(num)
        length = len(stacks[b])
        buffer = stacks[b][-a:]
        if reverse:
            buffer.reverse()
        stacks[c].extend(buffer)
        # print(stacks[b])
        del stacks[b][length-a:]
        
        # for i in stacks.keys():
        #     print(i,stacks[i])

        # print('\n',b, buffer)
        # # print(stacks[b])
        # print(c, stacks[c])

        # input()
        j+=1
    # print(i+1,j)
    return(stacks)
        







    # return(j,k)

# print(init_inputs('input5.txt'))
stacks = day5("input5.txt")
for i in stacks.keys():
    print(stacks[i][-1],end='')
print('\n')
stacks = day5("input5.txt",False)
for i in stacks.keys():
    print(stacks[i][-1],end='')