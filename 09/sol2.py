def main():
    seen = {}
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        #(x,y)
        #x+=1 right
        #y+=1 up
        head = [0,0]
        tail = [0,0]
        root = knot(None)
        knotNum = 10
        knots = [root]
        for i in range(0,knotNum-1):
            #print(i)
            knots.append(knot(knots[i]))
            knots[i].setTail(knots[i+1])
            knots[i+1].setXY([0,0])
        #print('knot len',len(knots))
        root.setXY([0,0])
        knots[1].setXY([0,0])
        #for i in knots:
        #    print(i.getXY(),end='')
        #    t = i.getTail()
        #    if t:
        #        print(t.getXY())
        #print('------')
        move = 0
        for x in lines:
            dir,amt = x.split(' ')
            amt = int(amt)
            delta = [0,0]
            if dir == 'R':
                delta = [1,0]
            elif dir == 'L':
                delta = [-1,0]
            elif dir == 'U':
                delta = [0,1]
            elif dir == 'D':
                delta = [0,-1]
            #print("move",move)
            while amt > 0:
                root.setXY([(a+b) for a, b in zip(root.getXY(), delta)])
                kn = 1
                #print("Head:",root.getXY())
                for i in knots[1:]:
                    if i.touching():
                        pass
                    else:
                        #print("not touching ",end='')
                        #print(i.getXY(), i.getHead().getXY())
                        dif = [(b-a) for a, b in zip(i.getXY(), i.getHead().getXY())]
                        for j in range(len(dif)):
                            if dif[j]!=0:
                                dif[j] = int(dif[j]/abs(dif[j]))
                        #print(dif)
                        #if kn == 9:
                        i.setXY([(a+b) for a, b in zip(i.getXY(), dif)])
                    #print("Knot",str(kn)+":",i.getXY(),i.getHead().getXY(),dif)
                    kn+=1
                amt-=1
        #print(knots[-1].getVisible())
        print(len(knots[-1].getVisible()))
        exit()
        print(len(seen))
#H = (x1,y1)
#T = (x2,y2)

class knot:
    headPointer = None
    tailPointer = None
    linear = 1
    XY = [0,0]
    visible = {tuple(XY):True}
    def __init__(self, head):
        self.headPointer = head
        self.tailPointer = None
        self.visible = {}
        self.XY = [0,0]
        self.linear =1
    def touching(self):
        if self.linearTouch(): return True
        return self.diagTouch()
    def setXY(self,coord):
        self.XY = coord
        self.visible[tuple(coord)] = True
    def linearTouch(self):
        H = self.headPointer.getXY()
        dirs = [
            [0,1], #up
            [0,-1], #down
            [-1,0], #left
            [1,0], #right
            [0,0], #same
        ]
        for i in dirs:
            if [a+b for a, b in zip(i, self.XY)] == H:
                self.linear = 1
                return True
        return False
    def diagTouch(self):
        H = self.headPointer.getXY()
        dirs = [
            [-1,-1],#bottom left
            [-1,1], #top left
            [1,-1], #bottom right
            [1,1]   #top right
        ]
        for i in dirs:
            if [a+b for a, b in zip(i, self.XY)] == H:
                self.linear = 0
                return True
        return False
    def setHead(self,head):
        self.headPointer = head
    def setTail(self,tail):
        self.tailPointer = tail
    def getHead(self):
        return self.headPointer
    def getTail(self):
        return self.tailPointer
    def getXY(self):
        return self.XY
    def getVisible(self):
        return self.visible

if __name__=="__main__":
    main()