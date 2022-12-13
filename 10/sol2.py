#Originally ' ' was '.' but the output was awful to look at.

def main():
    interest = [0,1,2]
    signals = ''
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        cycle = 1
        regX = 1
        for x in lines:
            #if cycle >= 10:
                #print(cycle,regX,interest)
                #break
            if x == 'noop':
                if (cycle-1)%40 in interest:
                    #print('#',cycle,regX,interest)
                    signals+='#'
                else:
                    #print('.',cycle,regX,interest)
                    signals+=' '
                cycle+=1
            else:
                val = int(x.split(' ')[1])
                for i in range(2):
                    if (cycle-1)%40 in interest:
                        #print('#',cycle,regX,interest)
                        signals+='#'
                    else:
                        #print('.',cycle,regX,interest)
                        signals+=' '
                    cycle+=1
                regX+=val
                interest = [regX-1,regX,regX+1]
        print(signals[0:40])
        print(signals[40:80])
        print(signals[80:120])
        print(signals[120:160])
        print(signals[160:200])
        print(signals[200:240])
if __name__=="__main__":
    main()