with open("input.txt","r") as fp:
    lines = fp.readlines()
    most = 0
    cur = 0
    all = []
    for x in lines:
        if x == '\n':
            all.append(cur)
            cur = 0
        else:
            cur += int(x)
        
    all.sort()
    print(sum(all[-1:]))
