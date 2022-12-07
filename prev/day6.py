def day6(text_file,length=4):
    f = open(text_file, "r")
    inputs = f.readlines()
    for i, input in enumerate(inputs):
        input = input.strip()
        for j in range(len(input)-length):
            buffer = input[j:j+length]
            for k,char in enumerate(buffer):
                counts = buffer.count(char)
                if counts>1:
                    break
                if k==length-1:
                    return(j+length,buffer)


answers = day6('input6.txt')
print(answers)
answers = day6('input6.txt',14)
print(answers)