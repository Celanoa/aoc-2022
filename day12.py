import numpy as np
def day12(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()



    for i, data in enumerate(inputs):
        data = data.strip()
        info = data.split(' ')



answer = day12("input12.txt")
print(answer)
# print("==============================================")
# answer = day12("input11.txt")
# print(answer)

