import itertools
def main():
    occupied = {}
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        #Generate all rock locations
        for l in lines:
            coordsList = l.split(' -> ')
            #print('coordsList',coordsList)
            for i in range(len(coordsList)):
                coordsList[i] = list(map(int,coordsList[i].split(',')))
                if i > 0:
                    if coordsList[i][0] < coordsList[i-1][0]:
                        #print("Moving X")
                        temp = list(map(lambda e: [e,coordsList[i][1]], list(range(coordsList[i][0],coordsList[i-1][0]+1))))
                        for i in temp:
                            occupied[tuple(i)] = True
                    elif coordsList[i][0] > coordsList[i-1][0]:
                        #print("Moving X")
                        temp = list(map(lambda e: [e,coordsList[i][1]], list(range(coordsList[i-1][0],coordsList[i][0]+1))))
                        for i in temp:
                            occupied[tuple(i)] = True
                    elif coordsList[i][1] < coordsList[i-1][1]:
                        #print("Moving Y")
                        temp = list(map(lambda e: [coordsList[i][0],e], list(range(coordsList[i][1],coordsList[i-1][1]+1))))
                        for i in temp:
                            occupied[tuple(i)] = True
                    elif coordsList[i][1] > coordsList[i-1][1]:
                        #print("Moving Y")
                        temp = list(map(lambda e: [coordsList[i][0],e], list(range(coordsList[i-1][1],coordsList[i][1]+1))))
                        for i in temp:
                            occupied[tuple(i)] = True
                    else:
                        occupied[tuple(coordsList[i])] = True
                        #print("No Movement")
                    #print('occupied',occupied)
        #Done generating rock locations
    #print(occupied)
    ground = 161
    blocks = 0
    #print(occupied)
    print('ground',ground)
    while (500,0) not in occupied:
        #print('dropping sand block number',(blocks+1))
        occupied = dropSand(occupied, ground)
        blocks+=1
        if blocks%1000 == 0:
            print("sent this many sand blocks",blocks)
    print(blocks)
    return True
def dropSand(grid,bottom):
    sandLoc = [500,0]
    while sandLoc[1] < bottom+1:
        #print(sandLoc)
        if tuple([x+y for x, y in zip(sandLoc,[0,1])]) not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[0,1])]
        elif tuple([x+y for x, y in zip(sandLoc,[-1,1])]) not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[-1,1])]
        elif tuple([x+y for x, y in zip(sandLoc,[1,1])]) not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[1,1])]
        else:
            grid[tuple(sandLoc)] = True
            #print('Did not hit ground',sandLoc)
            return grid
    #print('Hit the ground',sandLoc)
    grid[tuple(sandLoc)] = True
    return grid

if __name__=="__main__":
    main()