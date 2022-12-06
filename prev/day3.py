def char2int(character):
    if character.isupper():
        number = ord(character.lower()) - 70
    else:
        number = ord(character) - 96
    # print(number)
    return(number)

def check(bag):
    length = len(bag)
    comp1 = bag[:length//2]
    comp2 = bag[length//2:]
    # print(bag)
    # print(comp1)
    # print(comp2)
    score = 0
    for char1 in comp1:
        for char2 in comp2:
            if char1 == char2:
                # print(char1)
                score = char2int(char1)
                break
        if score != 0:
            break
    return(score)

def group(bags):
    score = 0
    for char1 in bags[0]:
        for char2 in bags[1]:  
            if char1 == char2:
                for char3 in bags[2]:
                    if char2 == char3:
                        score = char2int(char1)
                        return(score)
    return("ERROR")

def day3(text_file):
    f = open(text_file, "r")
    cals = f.readlines()
    total_score = 0
    total_score1 = 0
    bags = [[],[],[]]
    j = 0
    for i, cal in enumerate(cals):
        bag = cal.strip()
        index = (i+1)%3
        score = check(bag)
        bags[index]=bag
        if index == 0:
            score1 = group(bags)
            bags = [[],[],[]]
            j+=1
            total_score1+=score1
        total_score += score
        # break
    # return(total_score,total_score1)
    print(i+1,j)
    return(total_score,total_score1)

scores = day3("input3.txt")
print(scores)
