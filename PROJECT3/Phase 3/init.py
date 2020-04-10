
class Node:
    def __init__(self, x, y, totalCost, cTc, cTg, parent, angle, rpm, rpm2, listAngle):
        self.x = x
        self.y = y
        self.totalCost = totalCost
        self.cTc = cTc
        self.cTg = cTg
        self.parent = parent
        self.angle = angle
        self.RPM = rpm
        self.rpm2 = rpm2
        self.listAngle = listAngle

    def __lt__(self, other):
        return  self.totalCost < other.totalCost

def init():
    global nodeList, parentList, childList, costList, nodeLIST, ExploredNodeList ,ExploredParentNodeList ,ExploredChildNodeList ,masterList, ActionList, AngleList
    nodeList = []
    parentList = []
    childList = []
    costList = []
    nodeLIST = []
    ExploredNodeList = []
    ExploredParentNodeList = []
    ExploredChildNodeList = []
    masterList = []
    ActionList = []
    AngleList = []
