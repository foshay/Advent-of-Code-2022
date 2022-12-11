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
        max = 0
        for i in vis:
            if vis[i] > max:
                max = vis[i]
        print(max)

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
        #if (x,y) in self.visible:
        #    return self.visible[(x,y)]
        left = self.checkLeft(x,y) 

        right = self.checkRight(x,y)
        up = self.checkUp(x,y)
        down = self.checkDown(x,y)
        self.visible[(x,y)] = up * down * left * right
        return
    def checkLeft(self, x,y):
        val = self.grid[y][x]
        #print('check left val',val)
        cnt = 0
        x-=1
        while x >= 0:
            cnt+=1
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return cnt
            x-=1
        return cnt
    def checkRight(self, x,y):
        val = self.grid[y][x]
        #print('check right val',val)
        cnt=0
        x+=1
        while x < self.length:
            cnt+=1
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return cnt
            x+=1
        return cnt
    def checkUp(self, x,y):
        val = self.grid[y][x]
        #print('check up val',val)
        cnt=0
        y-=1
        while y >= 0:
            cnt+=1
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return cnt
            y-=1
        return cnt
    def checkDown(self, x,y):
        val = self.grid[y][x]
        #print('check down val',val)
        cnt=0
        y+=1
        while y < self.length:
            cnt+=1
            if self.grid[y][x] >= val:
                #print('cant see',x,y,'val',self.grid[y][x])
                return cnt
            y+=1
        return cnt

if __name__=="__main__":
    main()