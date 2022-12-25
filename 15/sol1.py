import itertools
def main():
    grid = {}
    target = 2000000
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
                if (Sy+i) == target:
                    if (Sy+i) in grid:
                        grid[(Sy+i)].extend(list(range((Sx-(dif-abs(i))),Sx+1+(dif-abs(i)))))
                    else:
                        grid[(Sy+i)] = list(range((Sx-(dif-abs(i))),Sx+1+(dif-abs(i))))
                    grid[Sy+i].sort()
                    grid[Sy+i] = list(k for k,_ in itertools.groupby(grid[Sy+i]))
                #print(grid[(Sy+i)])
                    if By == target:
                        grid[By].remove(Bx)
        print('Answer:',len(grid[target]))

if __name__=="__main__":
    main()