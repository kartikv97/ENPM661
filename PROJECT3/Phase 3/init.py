
class Node:
    def __init__(self, x, y, totalCost, cTc, cTg, parent, angle, listLocX, listLocY, listAngle):
        self.x = x
        self.y = y
        self.totalCost = totalCost
        self.cTc = cTc
        self.cTg = cTg
        self.parent = parent
        self.angle = angle
        self.listLocX = listLocX
        self.listLocY = listLocY
        self.listAngle = listAngle

    def __lt__(self, other):
        return  self.totalCost < other.totalCost

def init():
    global nodeList, parentList, childList, costList, nodeLIST, ExploredNodeList ,ExploredParentNodeList ,ExploredChildNodeList ,masterList
    nodeList = []
    parentList = []
    childList = []
    costList = []
    nodeLIST = []
    ExploredNodeList = []
    ExploredParentNodeList = []
    ExploredChildNodeList = []
    masterList = []
