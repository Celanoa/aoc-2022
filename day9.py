def day9(text_file,n_knots):
    f = open(text_file, "r")
    inputs = f.readlines()
    rope = list([])
    for i in range(n_knots):
        rope.append([0,0])
    TF = rope[n_knots-1]
    T_hist = {}
    T_hist[0] = []
    for i, data in enumerate(inputs):
        data = data.strip()
        cmd = data.split(' ')[0]
        amt = int(data.split(' ')[1])
        for j in range(amt):
            H = rope[0]
            if cmd == 'U':
                H[1]+=1
            elif cmd == 'D':
                H[1]-=1
            elif cmd == 'R':
                H[0]+=1
            elif cmd == 'L':
                H[0]-=1
            else:
                print("ERROR: line ",i+1)
                quit()
            for k in range(1,n_knots):
                rope[k] = t_move(rope[k-1],rope[k])
                if TF[0] in T_hist.keys():
                    T_hist[TF[0]].append(TF[1])
                else:
                    T_hist[TF[0]]=[]
                    T_hist[TF[0]].append(TF[1])

    counter = 0
    for key in T_hist.keys():
        inc = len(set(T_hist[key]))
        counter+=inc
    return(counter)

def t_move(H,T):
    x = H[0]-T[0]
    y = H[1]-T[1]

    #no tail movement
    if abs(x*y) == 1 or x==0 and y==0:
        return(T)

    # lateral tail movement
    if x*y == 0:
        if x == 2:
            T[0]+=1
        elif x == -2:
            T[0]-=1
        elif y == 2:
            T[1]+=1
        elif y == -2:
            T[1]-=1
        return(T)

    #diagonal tail movement
    if abs(x*y)>1:
        if x>0:
            T[0]+=1
        else:
            T[0]-=1
        if y>0:
            T[1]+=1
        else:
            T[1]-=1
        return(T)


answer = day9('input9.txt',2)
answer2 = day9('input9.txt',10)
print(answer)
print(answer2)