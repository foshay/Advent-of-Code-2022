def main():
    valves = {}
    fileName = "test.txt"
    timeLimit = 30
    moveTime = 1
    #Flow starts after the minute has passed in which the valve was opened
    openTime = 1
    with open(fileName,"r") as fp:
        lines = fp.read().splitlines()
        for l in lines:
            valves[l.split(' ')[1]] = Valve(l.split(' ')[1], l.split(';')[0].split('=')[-1])
    with open(fileName, "r") as fp:
        lines = fp.read().splitlines()
        for l in lines:
            for i in l.split(' ')[9:]:
                valves[l.split(' ')[1]].addConnection(valves[i[0:2]])
    for i in valves:
        valves[i].printInfo()
#Thoughts:
# A Valves flow value is related to when it was opened as flow * timeRemain.
# To open the valve you are standing at it takes 1 minute so you would calculate flow value as (timeRemain-1*0-1)*flow
# To open a connected valve it's flow value would be (timeRemain-1*1-1)*flow 1 distance moved + 1 minute to open
# Generalizing this to assess the flow value of any closed valve we would do (timeRemain-1*DistanceMoved-1)*flow 
#   with DistanceMoved being how many valves we had to traverse.
# We could use a dictionary to calculate the flow values for each valve at each time period.
# Here is an example of calculating a flow rate of a far valve at timeRemain 30:
#   Example: Valve HH with flow 22. To get to valve HH we need to do AA(Start) -> DD -> EE -> FF -> GG -> HH. This would take 5 minutes
#   to get to HH setting it's initial flow value to (30-5-1)*22 = 528
class Valve:
    name = ''
    flow = 0
    connections = []
    def __init__(self, name, flow):
        self.name = name
        self.flow = flow
        self.connections = []
    def addConnection(self, conn):
        self.connections.append(conn)
    def printInfo(self):
        print("Main Valve: ",end='')
        print("Name",self.name,"| Flow",self.flow)
        print("Connected Valves:")
        for i in self.connections:
            i.printBasicInfo()
    def printBasicInfo(self):
        print("\tName",self.name,"| Flow",self.flow)
    

if __name__=="__main__":
    main()