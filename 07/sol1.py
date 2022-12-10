

def main():
    deep = 0
    root = node(None,'/')
    cwd = root
    lineNum = 0
    with open("input.txt","r") as fp:
        x = fp.readline().rstrip()
        lineNum+=1
        while True:
            #print(len(root.getNodeNames()))
            #print('-'*deep,x,'lineNum:',lineNum,'CWD:',cwd.getName())
            if x == '':
                break
            if x[0] == '$' and x.split(' ')[1] == "cd":
                #print('command', x.split(' ')[1])
                #print('change dir',x)
                if x.split(' ')[2] == '/':
                    #print(' CDing to root')
                    cwd = root
                    deep = 0
                    #print('-'*deep,cwd.getName())
                    #map = ['/']
                elif x.split(' ')[2] == '..':
                    #print(' ../', map[-1], end='')
                    #map.pop()
                    #cwd.getParent().addValue(int(cwd.getValue()))
                    cwd = cwd.getParent()
                    deep-=1
                    #print('-'*deep,cwd.getName())
                    #print(' ->', map[-1])
                else:
                    #print(' CD: ../'+ map[-1]+'/' +x.split(' ')[2])
                    #map.append(x.split(' ')[2])
                    cwd = cwd.getNodes()[x.split(' ')[2]]
                    deep+=1
                    #print('-'*deep,cwd.getName())
                x = fp.readline().rstrip()
                lineNum+=1
            else:
                cwdListed = cwd.getListed()
                #print('SEEN?',cwdListed,x,cwd.getName())
                #if cwdListed: 
                    #print('---------------------------------------------------------')
                #    nodeList = cwd.getNodes()
                #    for i in nodeList:
                #        print(nodeList[i].getName())
                    #print('---------------------------------------------------------')
                while True:
                    x = fp.readline().rstrip()
                    lineNum+=1
                    if x == '' or x[0] == '$':
                        #print('setting listed',cwd.getName())
                        cwd.setListed()
                        break
                    #elif cwdListed == 1:
                    #    print('already LSd this',x)
                    #    pass
                    elif x.split(' ')[0] == 'dir':
                        if x.split(' ')[0] not in cwd.getNodes():
                            #print('adding node to',cwd.getName(), 'current count', str(len(cwd.getNodeNames())))
                            newNode = node(cwd, x.split(' ')[1])
                            #print('newNode count', str(len(newNode.getNodeNames())))
                            cwd.addNode(newNode, x.split(' ')[1])
                        #print(x)
                    else:
                        #print("FILE",x)
                        #print('-'*(deep+1)+'>',x.split(' ')[1])
                        cwd.addValue(int(x.split(' ')[0]))
    
    print('Root dirs:')
    allRootDirDic = root.getNodes()
    for k in root.getNodes():
        print(allRootDirDic[k].getName())
    print('All dirs:')
    for i in root.getAllNodes()[0]:
        print('-',i)
    root.setAllValues()
    print("----------------------------------------")
    for i in root.getAllNodes()[0]:
        print('-',i)
    print("----------------------------------------")
    print(root.findNodes())

class node:
    nodes={}
    nodeNames=[]
    value=0
    listed=0
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.nodes={}
        self.nodeNames=[]
        self.value=0
        self.listed=0
    def addNode(self, node, nodeName):
        self.nodes[nodeName] = node
        self.nodeNames.append(nodeName)
    def setListed(self):
        self.listed = 1
    def getListed(self):
        return self.listed
    def getParent(self):
        return self.parent
    def addValue(self, val):
        self.value += val
    def getValue(self):
        return self.value
    def getValues(self):
        if len(self.nodes)==0:
            return self.value
        else:
            sum = 0
            for i in self.nodes:
                sum+=self.nodes[i].getValues()
            return sum+self.value
    def getName(self):
        return self.name
    def setParent(self, parent):
        self.parent = parent
    def getNodes(self):
        return self.nodes
    def getAllNodes(self):
        if self.nodes:
            nodeList = [self.name+" "+str(self.value)]
            for i in self.nodes:
                nodeList.append(self.nodes[i].getAllNodes())
            return [nodeList]
        else:
            return [self.name+" "+str(self.value)]
    def setAllValues(self):
        if self.nodes:
            addVal = 0
            for i in self.nodes:
                addVal += self.nodes[i].setAllValues()
            self.value+=addVal
            return self.value
        else:
            return self.value
    def findNodes(self):
        if self.nodes:
            val = 0
            if self.value <= 100000:
                #print(str(self.value))
                val = self.value
            for i in self.nodes:
                val+=(self.nodes[i].findNodes())
            #print("val",val)
            return val
        else:
            if self.value <= 100000:
                #print(str(self.value))
                return self.value
            else:
                return 0
    def getNodeNames(self):
        return self.nodeNames

if __name__=="__main__":
    main()