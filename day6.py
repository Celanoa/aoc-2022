def day6(text_file,length=4):
    f = open(text_file, "r")
    inputs = f.readlines()
    # total_score = 0
    # total_score1 = 0
    # j=0
    # k=0
    for i, input in enumerate(inputs):
        input = input.strip()
        for j in range(len(input)-length):
            buffer = input[j:j+length]
            for k,char in enumerate(buffer):
                counts = buffer.count(char)
                print(buffer)
                if counts>1:
                    break
                if k==length-1:
                    return(j+length,buffer)
                # print(j,buffer)
    # return(input)





answers = day6('input6.txt')
print(answers)
answers = day6('input6.txt',14)
print(answers)