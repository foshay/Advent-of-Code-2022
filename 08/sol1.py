def main():
    grid = [ [] for i in range(9)]
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        length = len(lines[0])
        grid = [ [] for i in range(length)]
        for x in range(len(lines)):
            #print(lines[x])
            for i in lines[x]:
                grid[x].append(int(i))
        forest = trees(grid)
        #for i in forest.getGrid():
        #    print(i)
        #print(forest.checkVisible(1,3))
        #exit()
        for i in range(1,length-1):
            for j in range(1,length-1):
                forest.checkVisible(i,j)
        vis = forest.getVisible()
        total = 0
        for i in vis:
            if vis[i]:
                total+=1
                #print(i)
        print(total+(length*2)+((length-2)*2))

class trees:
    grid = []
    length = 0
    visible = {}
    def __init__(self, grid):
        self.grid = grid
        self.visible = {}
        self.length = len(grid[0])
    def getGrid(self):
        return self.grid
    def getVisible(self):
        return self.visible
    def checkVisible(self, x,y):
        #print(x,y)
        if (x,y) in self.visible:
            return self.visible[(x,y)]
        if self.checkLeft(x,y): 
            #print('visible left')
            self.visible[(x,y)] = True
            return True
        if self.checkRight(x,y): 
            self.visible[(x,y)] = True
            return True
        if self.checkUp(x,y): 
            self.visible[(x,y)] = True
            return True
        if self.checkDown(x,y): 
            self.visible[(x,y)] = True
            return True
        self.visible[(x,y)] = False
        return False
    def checkLeft(self, x,y):
        val = self.grid[y][x]
        #print('check left val',val)
        x-=1
        while x >= 0:
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return False
            x-=1
        return True
    def checkRight(self, x,y):
        val = self.grid[y][x]
        #print('check right val',val)
        x+=1
        while x < self.length:
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return False
            x+=1
        return True
    def checkUp(self, x,y):
        val = self.grid[y][x]
        #print('check up val',val)
        y-=1
        while y >= 0:
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return False
            y-=1
        return True
    def checkDown(self, x,y):
        val = self.grid[y][x]
        #print('check down val',val)
        y+=1
        while y < self.length:
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return False
            y+=1
        return True

if __name__=="__main__":
    main()