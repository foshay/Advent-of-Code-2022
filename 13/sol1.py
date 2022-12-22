def main():
    with open("test.txt","r") as fp:
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
            if(compare(a,b)): 
                print(a,b,'lgtm')
                total+=index
            else:
                print(a,b,'wrong')
            index+=1
    print(total)
def compare(a,b):
    #print(a,'\n',b)
    for i in range(len(a)):
        if i >= len(b):
            #print("right ran out of items, wrong order")
            return False
        if type(a[i]) == list or type(b[i]) == list:
            if type(a[i]) == int: a[i] = [a[i]]
            if type(b[i]) == int: b[i] = [b[i]]
            #print('recursing',a[i],b[i])
        #print(type(a),type(b))
        if a[i] > b[i]:
            #print('left bigger than right',a[i],b[i])
            return False
        #print(a[i],b[i])
    #print("lgtm")
    return True
if __name__=="__main__":
    main()