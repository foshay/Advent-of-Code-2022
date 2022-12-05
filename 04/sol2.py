
with open("input.txt","r") as fp:
    total = 0
    lines = fp.read().splitlines()
    for x in lines:
        a,b = x.split(',')
        alow = int(a.split('-')[0])
        ahi = int(a.split('-')[1])
        blow = int(b.split('-')[0])
        bhi = int(b.split('-')[1])
        arange = list(range(alow,ahi+1))
        brange = list(range(blow,bhi+1))
        print(arange, brange)
        for x in arange:
            if x in brange:
                total+=1
                break
        print(total)
    print('total',total)