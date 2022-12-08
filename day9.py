def day9(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()

    for i, data in enumerate(inputs):
        data = data.strip()
        cmds = data.split(' ')



answer = day9('input9.txt')
print(answer)