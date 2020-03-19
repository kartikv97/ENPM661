import math
from A_star_rigid_environment import *
import time
import  numpy as np

nodeList = []
parentList = []
childList = []
costList = []

flag= False
height = 200
# Node declaration
# Setting boundary as 300x200
class Node:
    def __init__(self, x, y, totalCost, cTc, cTg, parent):
        self.x = x
        self.y = y
        self.totalCost = totalCost
        self.cTc = cTc
        self.cTg = cTg
        self.parent = parent

    def __lt__(self, other):
        return  self.totalCost < other.totalCost


# Action Space :- UP DOWN LEFT RIGHt DIAGONAL_UP DIAGONAL_DOWN DIAGONAL_LEFT DIAGONAL_RIGHT
def moveUp(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x - 1 < 0:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node

    else:
        newNode.x = node.x - 1
        newNode.y = node.y
        newNode.cTc = node.cTc + 1
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDown(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x + 1 > 299:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y
        newNode.cTc = node.cTc + 1
        newNode.cTg =  calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveLeft(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y - 1
        newNode.cTc = node.cTc + 1
        newNode.cTg =  calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveRight(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.y + 1 > 199:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x
        newNode.y = node.y + 1
        newNode.cTc = node.cTc + 1
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveUpLeft(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x - 1 < 0 or node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y - 1
        newNode.cTc = node.cTc + math.sqrt(2)
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveUpRight(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x - 1 < 0 or node.y + 1 > 199:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x - 1
        newNode.y = node.y + 1
        newNode.cTc = node.cTc + math.sqrt(2)
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDownLeft(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x + 1 > 299 or node.y - 1 < 0:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y - 1
        newNode.cTc = node.cTc + math.sqrt(2)
        newNode.cTg =  calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode


def moveDownRight(node):
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0))
    if node.x + 1 > 299 or node.y + 1 > 199:
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    else:
        newNode.x = node.x + 1
        newNode.y = node.y + 1
        newNode.cTc = node.cTc + math.sqrt(2)
        newNode.cTg =  calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
    return True, newNode

# Function to check if node is already visited
def notRedundantNode(coordinate):
    if coordinate in childList:
        return False
    return True

# Function to calculate Euclidean Distance between current node and the goal node.
def calcEuclideanDist(curr_coordinate_x, curr_coordinate_y):
    cTg = np.sqrt((curr_coordinate_x-goal[0])**2 + (curr_coordinate_y-goal[1])**2 )
    # cTg = abs(goal[0]-curr_coordinate_x)+abs(goal[1]-curr_coordinate_y)
    return cTg

# Function to update and add new nodes to the list
def addNode(node):
    if check_Obstacle(node.x, node.y):
        return
    else:
        if notRedundantNode((node.x, node.y)):
            parentList.append(node.parent)
            childList.append((node.x, node.y))
            nodeList.append(node)
            # nodeList.sort(key=lambda  node:node.totalCost)



            # draw_Explored_Nodes(childList[len(childList)-1][0], childList[len(childList)-1][1])
            costList.append(node.totalCost)
        else:
            index = childList.index((node.x, node.y))
            # if nodeList[index].cost > node.cost:
            #     nodeList[index].cost = node.cost
            #     costList[index] = node.cost

            #     nodeList[index].parent = node.parent
            if costList[index] > node.totalCost:
                costList[index] = node.totalCost
                parentList[index] = node.parent

# Function to Backtrack from the Goal Node to Start Node
def backTracking(parent, child):
    # starting from the last parent node
    parentnode = parent[len(parent) - 2]
    childnode = child[len(child) - 1]
    # print("parent:", parentnode)
    # print("child:", childnode)
    nodePath = []
    nodePath.append(childnode)
    nodePath.append(parentnode)
    while parentnode != (0, 0):
        if parentnode in child:
            index = child.index(parentnode)
            parentnode = parent[index]
            nodePath.append(parentnode)
    nodePath = nodePath[::-1]
    print("noPPPPP",nodePath)
    return nodePath

# Function to check if Goal is reached.
def goalReached(node, goal):
    if (node.x, node.y) == goal:
        addNode(node)
        print('Goal Reached')
        print('Cost took to reach the goal is: ' + str(node.totalCost))
        return True
    return False

# Main aStar algorithm
def aStar(node, goal):
    count = 0
    state = False
    if goalReached(node, goal):
        return
    if check_Obstacle(node.x, node.y) and check_Obstacle(goal[0], goal[1]):
        return
    else:
        nodeList.append(node)
        parentList.append((0, 0))
        childList.append((node.x, node.y))
        costList.append(0)
        while True:
            status, newNode = moveLeft(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveRight(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveUp(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveDown(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveUpLeft(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveUpRight(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveDownLeft(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            status, newNode = moveDownRight(node)
            if status:
                if goalReached(newNode, goal):
                    break
                else:
                    addNode(newNode)
            count += 1
            # draw_Explored_Nodes(node.x, node.y)
            print("Node_x:", nodeList[0].x)
            print("Node_y:", height- nodeList[0].y)
            print("Node_ctc:", nodeList[0].cTc)
            print("Node_ctg:", nodeList[0].cTg)
            print("Node_total cost:", nodeList[0].totalCost)
            # nodeList.sort(key=lambda node: node.totalCost)
            nodeList.sort()
            nodeList.pop(0)
            node = nodeList[0]


            # print(count)
# Function to inputs from the user.
def get_User_Input(node):
    axis = ["X", "Y"]

    flag = False
    final_input = np.zeros(2)
    while flag is False:
        count = 0
        for a in axis:
            input_val = input("\nEnter the value of " + str(node)+ " "+ str(a) + " co-ordinate:")
            if len(input_val) is 0:
                print("You need to enter a value in range [0-299]. Don't leave a number blank!!!")
                flag = False
                break
            if a == "X":
                if int(input_val)<0 or int(input_val)>299:
                    flag = False
                    print("Entered input is out of bounds. Please enter a valid input!!")
                    break
                else:
                    flag =True
                    final_input[count] = np.array(int(input_val))
            if a == "Y":
                if int(input_val)<0 or int(input_val)>199:
                    flag = False
                    print("Entered input is out of bounds. Please enter a valid input!!")
                    break
                else:
                    flag =True
                    final_input[count] = np.array(int(input_val))
            count = count+1
    return final_input #np.reshape(final_input,(3,3))

# Getting inputs from the user
simulation = False
start = get_User_Input("Start Node")
end = get_User_Input("Goal Node")
goal = (int(end[0]), height - int(end[1]))
node = Node(int(start[0]), height -int(start[1]), 0,0,calcEuclideanDist(start[0],height-start[1]), (0, 0))

start_time = time.time()
draw_Start_and_Goal_Nodes(goal[0],goal[1])
# Check if the input goal lies within the obstacle space.
if check_Obstacle(goal[0], goal[1]):
    print("Goal cannot be reached")
else:
    aStar(node, goal)
    try:
        print("Exploring nodes...")
        aStar(node, goal)
    except:
        # Print the following if the goal cannot be reached since no path is available
        print("The radius and clearance is too Big!! Goal cannot be reached !!")
        flag= True
    if flag is False:
        print("Backtracking...")
        nodepath = backTracking(parentList, childList)
        print("parent:",parentList)
        print("child:", childList)
    simulation = False

    for node in childList:
        draw_Explored_Nodes(node[0], node[1])
    if flag is False:
        for pixel in nodepath:
            print(pixel[0], pixel[1])
            draw_Optimal_Nodes(pixel[0], pixel[1])


end_time= time.time()
print("Total time taken", end_time-start_time)

# Function to close the PyGame window.
while simulation is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()