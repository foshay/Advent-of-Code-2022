def main():
    monkeys=[]
    #make the monkeys TEST MONKEYS
    monkeys.append(monkey([79, 98],1,19,23))
    monkeys.append(monkey([54, 65, 75, 74],0,6,19))
    monkeys.append(monkey([79, 60, 97],2,0,13))
    monkeys.append(monkey([74],0,3,17))
    monkeys[0].setMonkeys(monkeys[2],monkeys[3])
    monkeys[1].setMonkeys(monkeys[2],monkeys[0])
    monkeys[2].setMonkeys(monkeys[1],monkeys[3])
    monkeys[3].setMonkeys(monkeys[0],monkeys[1])

    #monkeys.append(monkey([50, 70, 54, 83, 52, 78],1,3,11))
    #monkeys.append(monkey([71, 52, 58, 60, 71],2,0,7))
    #monkeys.append(monkey([66, 56, 56, 94, 60, 86, 73],0,1,3))
    #monkeys.append(monkey([83, 99],0,8,5))
    #monkeys.append(monkey([98, 98, 79],0,3,17))
    #monkeys.append(monkey([76],0,4,13))
    #monkeys.append(monkey([52, 51, 84, 54],1,17,19))
    #monkeys.append(monkey([82, 86, 91, 79, 94, 92, 59, 94],0,7,2))
    #monkeys[0].setMonkeys(monkeys[2],monkeys[7])
    #monkeys[1].setMonkeys(monkeys[0],monkeys[2])
    #monkeys[2].setMonkeys(monkeys[7],monkeys[5])
    #monkeys[3].setMonkeys(monkeys[6],monkeys[4])
    #monkeys[4].setMonkeys(monkeys[1],monkeys[0])
    #monkeys[5].setMonkeys(monkeys[6],monkeys[3])
    #monkeys[6].setMonkeys(monkeys[4],monkeys[1])
    #monkeys[7].setMonkeys(monkeys[5],monkeys[3])
    for i in monkeys:
        print(i.getItems())
    print('----')
    for i in range(20):
        for j in monkeys:
            j.inspect()
    ins = []
    for i in monkeys:
        ins.append(i.getInspect())
    ins.sort()
    print(ins[-2]*ins[-1])

class monkey:
    items=[]
    worry=0
    op = 0
    test=1
    inspectCount=0
    monkeyTrue=None
    monkeyFalse=None
    def __init__(self, items, op, worry, test):
        self.items = items
        self.worry = worry
        self.op = op
        self.test = test
        self.monkeyTrue=None
        self.monkeyFalse=None
    def getWorry(self, old):
        if self.op == 0:
            return old + self.worry
        elif self.op == 1:
            return old * self.worry
        else:
            return old * old
    #M1 is true M2 is false
    def setMonkeys(self,M1,M2):
        self.monkeyTrue = M1
        self.monkeyFalse = M2
    def throw(self):
        #print('throw',self.items[0])
        if self.items[0]%self.test == 0:
            self.monkeyTrue.getItems().append(self.items[0])
            self.items = self.items[1:]
        else:
            self.monkeyFalse.getItems().append(self.items[0])
            self.items = self.items[1:]
    def getItems(self):
        return self.items
    def inspect(self):
        leng = len(self.items)
        for i in range(leng):
            self.inspectCount+=1
            #print("item before",self.items[0])
            self.items[0] = int(self.getWorry(self.items[0])/3)
            #print("item after",self.items[0])
            self.throw()
    def getInspect(self):
        return self.inspectCount
if __name__=="__main__":
    main()