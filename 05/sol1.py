
with open("input.txt","r") as fp:
    stacks = [ [] for i in range(9)]
    print(stacks)
    while True:
        x = fp.readline().rstrip()
        print(x)
        if x[0:2] == ' 1':
            break
        for i in range(0,len(x),4):
            if x[i] != ' ':
                stacks[int((i/4))].append(x[i+1:i+2])
    for i in range(len(stacks)):
        stacks[i].reverse()
    fp.readline().rstrip()
    while True:
        x = fp.readline().rstrip()
        if not x: break
        mov = int(x.split(' ')[1])
        src = int(x.split(' ')[3])-1
        dest = int(x.split(' ')[5])-1
        new = stacks[src][:-mov]
        move = stacks[src][-mov:]
        move.reverse()
        stacks[dest].extend(move)
        stacks[src]=new
    for i in range(len(stacks)):
        print(stacks[i][-1], end='')