key = ['.','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
with open("input.txt","r") as fp:
    total = 0
    lines = fp.read().splitlines()
    #for i in range(len(key)):
    #    print(i, key[i])
    for x in lines:
        a = x[:int(len(x)/2)]
        b = x[int(len(x)/2):]
        for i in b:
            if i in a:
                print(i)
                total += key.index(i)
                break
print(total)