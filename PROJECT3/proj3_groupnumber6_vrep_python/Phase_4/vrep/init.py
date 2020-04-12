
class Node:
    def __init__(self, x, y, totalCost, cTc, cTg, parent, angle, rpm, parentAngle, listAngle):
        self.x = x
        self.y = y
        self.totalCost = totalCost
        self.cTc = cTc
        self.cTg = cTg
        self.parent = parent
        self.angle = angle
        self.RPM = rpm
        self.parentAngle = parentAngle
        self.listAngle = listAngle

    def __lt__(self, other):
        return  self.totalCost < other.totalCost

def init():
    global nodeList, parentList, childList, costList, nodeLIST, ExploredNodeList ,ExploredParentNodeList ,ExploredChildNodeList ,masterList, ActionList, AngleList, parentAngleList,ExploredNodeAngleList,ExploredNodeActionList,test
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
    parentAngleList = []
    ExploredNodeAngleList = []
    ExploredNodeActionList = []
    test=[]