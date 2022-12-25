import itertools
def main():
    grid = {}
    bounds = 4000000
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        for l in lines:
            print(l)
            Sx = int(l.split('=')[1][:-3])
            Sy = int(l.split('=')[2][:-24])
            sensor = [Sx,Sy]
            Bx = int(l.split('=')[3][:-3])
            By = int(l.split('=')[4])
            beacon = [Bx,By]
            dif = [abs(x-y) for x, y in zip(sensor,beacon)]
            dif = dif[0]+dif[1]
            #print('Sensor: ' + str(sensor) + " - Beacon: "+str(beacon)+" Dif: " + str(dif))
            for i in range(-dif,dif+1):
                #print(i,' ',(dif-abs(i)),' ',end='')
                delta = (dif-abs(i))
                low = Sx-delta
                if low < 0: low = 0
                high = Sx+1+delta
                if high > bounds: high = bounds
                if (Sy+i) <= bounds and (Sy+i >= 0):
                    print("Checking",(Sy+i))
                    if (Sy+i) in grid:
                        grid[(Sy+i)].extend(list(range(low,high)))
                    else:
                        grid[(Sy+i)] = list(range(low,high))
                    grid[Sy+i].sort()
                    grid[Sy+i] = list(k for k,_ in itertools.groupby(grid[Sy+i]))
                #print(grid[(Sy+i)])
                    #if By <= bounds and By in grid and Bx in grid[By]:
                    #    grid[By].remove(Bx)
        lenNormal = 0
        if len(grid[0]) == len(grid[1]):
            lenNormal = len(grid[0])
        else:
            lenNormal = min(len(grid[0]),len(grid[1]))
        print(lenNormal)
        for i in range(0,bounds+1):
            if len(grid[i]) != lenNormal:
                for j in range(0,bounds+1):
                    if j not in grid[i]:
                        print('answer',j*4000000 +i)
                        exit()
        #print('Answer:',len(grid[target]))

if __name__=="__main__":
    main()