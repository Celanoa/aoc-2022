import numpy as np

def day4(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()
    total_score = 0
    total_score1 = 0
    j=0
    k=0
    for i, input in enumerate(inputs):
        input = input.strip()
        elf1 = input.split(',')[0]
        nums1 = elf1.split('-')
        elf2 = input.split(',')[1]
        nums2 = elf2.split('-')
        print(i,nums1[0],elf2)
        a1,a2 = int(nums1[0]), int(nums1[1])
        b1,b2 = int(nums2[0]), int(nums2[1])
        # print(i)
        if a1<=b1 and a2>=b2 or a1>=b1 and a2<=b2:
            j+=1
        if a1>=b1 and a1<=b2 or b1>=a1 and b1<=a2:
            k+=1
    # print(i+1,j,k)
    return(j,k)

answers = day4('input4.txt')
print(answers)