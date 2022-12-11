import numpy as np
def day11(text_file, rounds=20, stress=False):
    f = open(text_file, "r")
    inputs = f.readlines()
    objs = list()
    divide = 1                      #Least common multiple of test values
    for i, data in enumerate(inputs):
        data = data.strip()
        info = data.split(' ')
        if info[0] == 'Test:':
            test = int(info[3])
            if divide%test != 0:
                divide*= test       #getting the LCM of the test values
            continue

    for i, data in enumerate(inputs):
        data = data.strip()
        info = data.split(' ')
        if data == '':
            continue
        if info[0] == 'Monkey':
            continue
        if info[0] == 'Starting':
            items = info[2:]
            for j in range(len(items)):
                items[j] = int(items[j].replace(",", "", 1))
                items[j] = np.uint64(items[j])
            items = np.asarray(items)
            continue
        if info[0] == 'Operation:':
            op = info[4]
            num = info[5]
            continue
        if info[0] == 'Test:':
            test = int(info[3])
            continue
        if info[1] == 'true:':
            m1 = int(info[5])
            continue
        if info[1] == 'false:':
            m2 = int(info[5])
            objs.append(Monkey(items,op,num,test,m1,m2,divide,stress))

    answer = throw(objs, rounds)
    return(answer)

class Monkey():

    def __init__(self, items, op, num, test, m1, m2, divide, stress=False):
        self.items = items
        self.op = op
        self.num = num
        self.test = test
        self.m1 = m1
        self.m2 = m2
        self.divide = divide
        self.stress = stress
        
    def func(self):
        if self.num == 'old':
            self.new = self.items.copy()
            if self.op == '*':
                for i in range(len(self.items)):
                    self.new[i] = self.items[i]**2
            else:
                for i in range(len(self.items)):
                    self.new[i] = self.items[i]*2
        else:
            self.num = int(self.num)
            if self.op == '*':
                self.new = (self.items*self.num)
            else:
                self.new = (self.items+self.num)
                
        if not self.stress:
            self.new = self.new//3
        self.dec = []
        for i in range(len(self.new)):
            if self.new[i]>=self.divide:
                self.new[i] = self.new[i]%self.divide
            if self.new[i]%self.test == 0:
                self.dec.append(self.m1)
            else:
                self.dec.append(self.m2)
        return(self.dec)    
        
def throw(monkeys, rounds):
    monkey_business = [0]*len(monkeys)
    for k in range(rounds):
        for i in range(len(monkeys)):
            dec = monkeys[i].func()
            monkey_business[i]+=len(monkeys[i].items)
            for j in range(len(dec)):
                monke = dec[j]
                item = monkeys[i].new[0]
                rec_monke = monkeys[monke]
                rec_monke.items = np.append(rec_monke.items,item)
                monkeys[i].items = monkeys[i].items[1:]
                monkeys[i].new = monkeys[i].new[1:]

    sorted_mb = sorted(monkey_business, reverse=True)
    return(sorted_mb[0]*sorted_mb[1])

        

answer = day11("input11.txt")
print(answer)
print("==============================================")
answer = day11("input11.txt",10000,True)
print(answer)

