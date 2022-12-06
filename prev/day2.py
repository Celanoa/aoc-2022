
def day2(text_file):
    f = open(text_file, "r")
    cals = f.readlines()
    total_score = 0
    total_score1 = 0
    for cal in cals:
        strat = cal.strip()
        # Mars = strat.split(" ")[0]
        # Nathan = strat.split(" ")[1]
        # print(strat)
        score,score1 = scoring(strat)
        total_score+=score
        total_score1+=score1
        # break
    return(total_score,total_score1)

        

def scoring(strat):
    # Mars = strat.split(" ")[0]
    # Nathan = strat.split(" ")[1]
    choice ={"A":1,"B":2,"C":3}
    choice1 ={"A X":4,"B X":1,"C X":7,"A Y":8,"B Y":5,"C Y":2,"A Z":3,"B Z":9,"C Z":6}
    choice2 ={"A X":3,"B X":1,"C X":2,"A Y":4,"B Y":5,"C Y":6,"A Z":8,"B Z":9,"C Z":7}
    score = choice1[strat]
    score1=choice2[strat]
    return(score,score1)

    


Jesse, Daniel = day2("input2.txt")
print(Jesse,Daniel)

# ehe = scoring("X A")