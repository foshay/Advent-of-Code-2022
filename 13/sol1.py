def main():
    with open("input.txt","r") as fp:
        total = 0
        index = 1
        while True:
            a = fp.readline().rstrip()
            b = fp.readline().rstrip()
            _ = fp.readline().rstrip()
            if a == '':
                break
            a = eval(a)
            b = eval(b)
            #print(a,b)
            print("Compare",a,'\/',b)
            if(compare(a,b)==1): 
                print(a,b,'lgtm')
                total+=index
            else:
                print(a,b,'wrong')
            index+=1
    print(total)
def compare(a,b):
    #print(a,'\n',b)
    for i in range(len(a)):
        if i>= len(b):
            return -1
        if type(a[i]) == int and type(b[i]) == int:
            if a[i] > b[i]:
                print('int and int, WRONG',a[i],b[i])
                return -1
            elif a[i] < b[i]:
                print('int and int, RIGHT',a[i],b[i])
                return 1
        elif type(a[i]) == list and type(b[i]) == list:
            print('list and list',a[i],b[i])
            res = compare(a[i],b[i])
            if res == -1:
                return -1
            elif res == 1:
                return 1
            if len(a[i]) < len(b[i]):
                print('left len less than right len', len(a[i]),len(b[i]))
                return 1
        elif type(a[i]) == int or type(b[i]) == int:
            print('list and int',a[i],b[i])
            if type(a[i]) == int: a[i] = [a[i]]
            else: b[i] = [b[i]]
            print('converted',a[i],b[i])
            res = compare(a[i],b[i])
            if res == -1:
                return -1
            elif res == 1:
                return 1
            if len(a[i]) < len(b[i]):
                return 1
        #if a[i] > b[i]:
        #    print('Right side is smaller, so inputs are in wrong order',a[i],b[i])
        #    return False
        #print('Compare',a[i],'lte',b[i])
        #if i+1 >= len(b):
        #    print("right ran out of items, wrong order")
        #    return False
    #print("lgtm")
    if len(a) < len(b):
        return 1
    print('lists same len',a,b)
    return 0
if __name__=="__main__":
    main()