
with open("input.txt","r") as fp:
    total = 0
    lines = fp.read().splitlines()
    #for i in range(len(key)):
    #    print(i, key[i])
    for x in lines:
        a,b = x.split(',')
        alow = int(a.split('-')[0])
        ahi = int(a.split('-')[1])
        blow = int(b.split('-')[0])
        bhi = int(b.split('-')[1])
        if (alow <= blow and ahi >= bhi) or (blow <= alow and bhi >= ahi):
            total+=1
    print('total',total)