import numpy as np

def day8(text_file):
    l,w = get_size(text_file)
    f = open(text_file, "r")
    inputs = f.readlines()
    forest = np.zeros((l,w), dtype=int)
    outside = l*w - (l-2)*(w-2)
    counter = outside
    ############################################# forest mapping
    for i, data in enumerate(inputs):
        trees = data.strip()
        for j,tree in enumerate(trees):
            forest[i][j]=tree
    #############################################
    for i in range(1,l-1):
        for j in range(1,w-1):
            try:
                tree = forest[i][j]
                left = max(forest[i][:j])
                right= max(forest[i][j+1:w+1])
                top  = max(forest.T[j][:i])
                bot  = max(forest.T[j][i+1:w+1])
                check=min([left,right,top,bot])

                if tree> check:
                    counter+=1
            except:
                print("ERROR: ",i,j,tree)
                exit()
    answer = counter
    ########################### part 2 starts ###########################
    top_score = 0           
    for i in range(1,l-1):
        for j in range(1,w-1):
            try:
                tree = forest[i][j]
                if tree <8: #assuming best score would be coming from a tree at least height 8
                    continue

                left = forest[i][:j][::-1]
                right= forest[i][j+1:w+1]
                top  = forest.T[j][:i][::-1]
                bot  = forest.T[j][i+1:w+1]
                scores = score(tree,left,right,top,bot)
                tot_score = np.prod(scores)
                if tot_score>top_score:
                    top_score=tot_score
            except:
                print("ERROR: ",i,j,tree)
                exit()
    answer2 = top_score

    return(answer,answer2)

def get_size(text_file):
    f = open(text_file, "r")
    inputs = f.readlines()
    for i, data in enumerate(inputs):
        trees = data.strip()
        for j, tree in enumerate(trees):
            continue
    return(i+1,j+1)

def score(tree1,left,right,top,bot):
    counter = [0,0,0,0]
    i=0
    for tree in left: 
        counter[i]+=1
        if tree1<=tree:
            break
    i+=1
    for tree in right: 
        counter[i]+=1
        if tree1<=tree:
            break
    i+=1
    for tree in top: 
        counter[i]+=1
        if tree1<=tree:
            break
    i+=1
    for tree in bot: 
        counter[i]+=1
        if tree1<=tree:
            break
    return(counter)


answer = day8('input8.txt')
print(answer)