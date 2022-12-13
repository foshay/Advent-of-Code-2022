def main():
    seen = {}
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        #(x,y)
        #x+=1 right
        #y+=1 up
        head = [0,0]
        tail = [0,0]
        
        if touching(head,tail):
            seen[tuple(tail)] = True
        linear = 1
        for x in lines:
            dir,amt = x.split(' ')
            amt = int(amt)
            if dir == 'R':
                #print('right',dir,amt)
                while int(amt) > 0:
                    #print(head[0])
                    head[0]+=1
                    if linearTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 1
                    elif diagTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 0
                    else:
                        #print('not touching',head,tail)
                        tail[0]+=1
                        if linear == 0:
                            if tail[1] < head[1]:
                                tail[1]+=1
                            else:
                                tail[1]-=1
                            linear=1
                        seen[tuple(tail)]=True
                    amt-=1
                #print('end positions',head,tail)
            elif dir == 'L':
                #print('left',dir)
                while int(amt) > 0:
                    #print(head[0])
                    head[0]-=1
                    if linearTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 1
                    elif diagTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 0
                    else:
                        #print('not touching',head,tail)
                        tail[0]-=1
                        if linear == 0:
                            if tail[1] < head[1]:
                                tail[1]+=1
                            else:
                                tail[1]-=1
                            linear=1
                        seen[tuple(tail)]=True
                    amt-=1
                #print('end positions',head,tail)
            elif dir == 'U':
                #print('up',dir)
                while int(amt) > 0:
                    #print(head[0])
                    head[1]+=1
                    if linearTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 1
                    elif diagTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 0
                    else:
                        #print('not touching',head,tail)
                        tail[1]+=1
                        if linear == 0:
                            if tail[0] < head[0]:
                                tail[0]+=1
                            else:
                                tail[0]-=1
                            linear=1
                        seen[tuple(tail)]=True
                    amt-=1
                #print('end positions',head,tail)
            else:
                #print('down',dir)
                while int(amt) > 0:
                    #print(head[0])
                    head[1]-=1
                    if linearTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 1
                    elif diagTouch(head,tail):
                        #print('touching',head,tail)
                        linear = 0
                    else:
                        #print('not touching',head,tail)

                        tail[1]-=1
                        if linear == 0:
                            if tail[0] < head[0]:
                                tail[0]+=1
                            else:
                                tail[0]-=1
                            linear=1
                        seen[tuple(tail)]=True
                    amt-=1
                #print('end positions',head,tail)
        print(len(seen))
        #print(seen)
#H = (x1,y1)
#T = (x2,y2)
def touching(H,T):
    if linearTouch(H,T): return True
    return diagTouch(H,T)

def linearTouch(H,T):
    dirs = [
        [0,1], #up
        [0,-1], #down
        [-1,0], #left
        [1,0], #right
        [0,0], #same
        
    ]
    for i in dirs:
        #print(i)
        if [a+b for a, b in zip(i, T)] == H:
            return True
    return False

def diagTouch(H,T):
    dirs = [
        [-1,-1],
        [-1,1],
        [1,-1],
        [1,1]
    ]
    for i in dirs:
        #print(i)
        if [a+b for a, b in zip(i, T)] == H:
            return True
    return False
            
if __name__=="__main__":
    main()