def main():
    with open("input.txt","r") as fp:
        lines = fp.read().splitlines()
        for l in lines:
            print(l)
            

if __name__=="__main__":
    main()