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

    answer = 0

    # return(answer,answer2)


answer = day7('input7.txt')
print(answer)