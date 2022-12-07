with open("input.txt","r") as fp:
    x = fp.readline().rstrip()
    lookback = {}
    count = 0
    i=0
    while i < len(x):
        print(lookback)
        if x[i] in lookback:
            i = lookback[x[i]]+1
            lookback = {}
            count = 0
        else:
            lookback[x[i]] = i
            count +=1
            i+=1
        if count == 14:
            print(i)
            exit()
        