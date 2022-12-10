# import numpy as np
def day11(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()    
    for i, data in enumerate(inputs):
        data = data.strip()

    # return(answer)


answer = day11("input11.txt")
print(answer)
