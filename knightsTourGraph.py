class Vertex:
    def __init__(self,key):
        self.id = key #typically a string
        self.connectedTo = {} #keys will be the vertices it is pointing to and the value is the weight
        self.color = 'white'
        
    def setColor(self,color):
        self.color = color
        
    def getColor(self):
        return self.color
        
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connected to: ' + str ([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    

class Graph: #ADT = abstract data type
    def __init__(self):
        self.vertList = {} #objects are listed as values
        self.numVertices = 0
    
    def addVertex(self,key):
        #adds instance of Vertext to graph
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
         
    def addEdge(self,fromVert, toVert, weight=0):
        #adds a directed connection between fromVert to toVert to the graph with weight
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight)
    
    def getVertex(self,vertKey):
        #finds Vertex in graph with name: vertKey
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None
        
    def getVertices(self):
        #returns a list of all the vertex keys in the Graph
        return self.vertList.keys()


def buildKtGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row,col,bdSize)
            newPositions = genLegalMoves(row,col,bdSize)
            for each in newPositions:
                nId = posToNodeId(each[0],each[1],bdSize)
                ktGraph.addEdge(nodeId,nId)
    return ktGraph

def posToNodeId(row,col,bdSize):
    return (row * bdSize) + col

def genLegalMoves(x,y,bdSize):
    newMoves= []
    moveSet = [(-1,2),(-1,-2),(-2,-1),(-2,1),(1,2),(1,-2),(2,1),(2,-1)]
    
    for i in moveSet:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
    
def knightTour(n,path,u,limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
        pathList = []
        for each in path:
            pathList.append(each.getId())
        print(pathList)
    return done

newKt = buildKtGraph(5)

knightTour(1,[],newKt.getVertex(9),25)


