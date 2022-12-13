def main():
    interest = [20,60,100,140,180,220]
    signals = []
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        cycle = 1
        regX = 1
        for x in lines:

            if x == 'noop':
                if cycle in interest:
                    signals.append(regX*cycle)
                cycle+=1
            else:
                val = int(x.split(' ')[1])
                for i in range(2):
                    if cycle in interest:
                        signals.append(regX*cycle)
                    cycle+=1
                regX+=val
        print(sum(signals))
if __name__=="__main__":
    main()