key = ['.','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open("input.txt","r") as fp:
    total = 0
    while True:
        a = fp.readline().rstrip()
        b = fp.readline().rstrip()
        c = fp.readline().rstrip()
        dic = []
        for i in a:
            if i in b:
                dic.append(i)
        for i in c:
            if i in dic:
                total += key.index(i)
                break
        if not a or not b or not c: break
        print(a,b,c)
print(total)