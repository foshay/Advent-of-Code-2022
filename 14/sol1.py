import itertools
def main():
    occupied = []
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
                        occupied.extend(list(map(lambda e: [e,coordsList[i][1]], list(range(coordsList[i][0],coordsList[i-1][0]+1)))))
                    elif coordsList[i][0] > coordsList[i-1][0]:
                        #print("Moving X")
                        occupied.extend(list(map(lambda e: [e,coordsList[i][1]], list(range(coordsList[i-1][0],coordsList[i][0]+1)))))
                    elif coordsList[i][1] < coordsList[i-1][1]:
                        #print("Moving Y")
                        occupied.extend(list(map(lambda e: [coordsList[i][0],e], list(range(coordsList[i][1],coordsList[i-1][1]+1)))))
                    elif coordsList[i][1] > coordsList[i-1][1]:
                        #print("Moving Y")
                        occupied.extend(list(map(lambda e: [coordsList[i][0],e], list(range(coordsList[i-1][1],coordsList[i][1]+1)))))
                    else:
                        occupied.extend(coordsList[i])
                        #print("No Movement")
                    #print('occupied',occupied)
        #Done generating rock locations
    #print(occupied)
    occupied.sort()
    occupied = list(k for k,_ in itertools.groupby(occupied))
    ground = max(map(lambda x: x[1], occupied))
    blocks = 0
    while True:
        #print('dropping sand block number',(blocks+1))
        occupied, status = dropSand(occupied, ground)
        if status:
            blocks+=1
        else:
            break
    print(blocks)
    return True
def dropSand(grid,bottom):
    sandLoc = [500,0]
    while sandLoc[1] < bottom:
        #print(sandLoc)
        if [x+y for x, y in zip(sandLoc,[0,1])] not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[0,1])]
        elif [x+y for x, y in zip(sandLoc,[-1,1])] not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[-1,1])]
        elif [x+y for x, y in zip(sandLoc,[1,1])] not in grid:
            sandLoc = [x+y for x, y in zip(sandLoc,[1,1])]
        else:
            grid.append(sandLoc)
            #print(grid)
            return grid, True
    print('Fell through the ground')
    return grid, False

if __name__=="__main__":
    main()