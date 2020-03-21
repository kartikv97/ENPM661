import math
from test_environment import *
import time
import  numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import cv2
import glob

nodeList = []
parentList = []
childList = []
costList = []
nodeLIST = []
ExploredNodeList = []
ExploredParentNodeList = []
ExploredChildNodeList = []

flag= False
height = 200
# Node declaration
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




def generateApproxCoordinates(node):

    for i in range(12):
        if i*30<= int(node.angle)<= i*30 +30:
            if i*30<= node.angle <i*30 +15:
                new_angle = i*30
                break
            else:
                new_angle = i*30 + 30
                break

    if int(node.x) <= node.x < int(node.x) + 0.25:
        new_x = int(node.x)
    elif int(node.x) + 0.25 <= node.x < int(node.x) + 0.5:
        new_x = int(node.x) + 0.5
    elif int(node.x) + 0.5 <= node.x < int(node.x) + 0.75:
        new_x = int(node.x) + 0.5
    else:
        new_x = int(node.x) + 1
    if int(node.y)<= node.y <int(node.y)+0.25:
        new_y = int(node.y)
    elif int(node.y) + 0.25<= node.y <int(node.y)+0.5:
        new_y = int(node.y) + 0.5
    elif int(node.y) + 0.5<= node.y <int(node.y)+0.75:
        new_y = int(node.y) + 0.5
    else:
        new_y = int(node.y) + 1

    return new_x , new_y , new_angle

########################################################################################################################

Visited_Nodes_List = [[[0 for k in range(12)] for j in range(400)] for i in range (600)]

########################################################################################################################
def isNodeVisited(node):

    new_x, new_y, new_angle = generateApproxCoordinates(node)
    if new_angle == 0:
        new_angle = int(1)
    else:
        new_angle = int( 360 / new_angle )
    if Visited_Nodes_List[int(new_x*2)-1][int(new_y*2)-1][new_angle-1] == 1:
        return False
    else:
        return True

# Defining the action Space.
def firstAction(node,angle):
    # print("FIRST ACTION:::::::::::::::::::::::")
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle))
    newNode.angle = angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node

    if isNodeVisited(newNode) == False:
        return False, node

    else:

        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
        newNode.angle = angle
        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:

            index = childList.index((newNode.x,newNode.y))

            if costList[index] > newNode.totalCost:
                costList[index] = newNode.totalCost
                parentList[index] = newNode.parent
                nodeList.sort()

    return True, newNode

def secondAction(node,angle):
    # print("SECOND ACTION:::::::::::::::::::::::")
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle + 30))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle + 30))
    newNode.angle = angle + 30
    if newNode.angle > 360:
        newNode.angle = newNode.angle - 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node

    if isNodeVisited(newNode) == False:
        return False, node

    else:

        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)

        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:
            new_x, new_y, new_angle = generateApproxCoordinates(node)
            index = childList.index((newNode.x,newNode.y))

            if costList[index] > newNode.totalCost:
                costList[index] = newNode.totalCost
                parentList[index] = newNode.parent
                nodeList.sort()

    return True, newNode

def thirdAction(node,angle):
    # print("THIRD ACTION:::::::::::::::::::::::")
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle + 60))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle + 60))
    newNode.angle = angle + 60
    if newNode.angle > 360:
        newNode.angle = newNode.angle - 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node

    if isNodeVisited(newNode) == False:
        # print("notVVVV")
        return False, node

    else:

        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
        # newNode.angle = angle + 60
        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:

            index = childList.index((newNode.x,newNode.y))

            if costList[index] > newNode.totalCost:
                costList[index] = newNode.totalCost
                parentList[index] = newNode.parent
                nodeList.sort()

    return True, newNode

def fourthAction(node,angle):
    # print("FOURTH ACTION:::::::::::::::::::::::")
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle - 30))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle - 30))
    newNode.angle = angle - 30
    if newNode.angle < 0:
        newNode.angle = newNode.angle + 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    if isNodeVisited(newNode)== False:
        return False, node

    else:

        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x,node.y)

        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:

            index = childList.index((newNode.x,newNode.y))

            if costList[index] > newNode.totalCost:
                costList[index] = newNode.totalCost
                parentList[index] = newNode.parent
                nodeList.sort()

    return True, newNode

def fifthAction(node,angle):
    # print("FIFTH ACTION:::::::::::::::::::::::")
    newNode = Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle - 60))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle - 60))
    newNode.angle = angle - 60
    if newNode.angle < 0:
        newNode.angle = newNode.angle + 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    if check_Obstacle(node.x, node.y):
        return False, node
    if isNodeVisited(newNode) == False:
        return False, node
    else:
        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x,node.y)

        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:
            index = childList.index((newNode.x,newNode.y))

            if costList[index] > newNode.totalCost:
                costList[index] = newNode.totalCost
                parentList[index] = newNode.parent
                nodeList.sort()

    return True, newNode


# Function to calculate Euclidean Distance between current node and the goal node.
def calcEuclideanDist(curr_coordinate_x, curr_coordinate_y):
    cTg = np.sqrt((curr_coordinate_x-goal[0])**2 + (curr_coordinate_y-goal[1])**2 )*2    #### Added Weight parameter.
    # cTg = abs(goal[0]-curr_coordinate_x)+abs(goal[1]-curr_coordinate_y)                                      # MANHATTAN DISTANCE FORMULA
    return cTg



# Function to Backtrack from the Goal Node to Start Node
def backTracking(parent, child):

    # starting from the last parent node
    parentnode = parent[len(parent) - 1]
    childnode = child[len(child) - 1]
    nodePath = []
    nodePath.append(childnode)
    nodePath.append(parentnode)
    while parentnode != (0, 0):
        if parentnode in child:
            index = child.index(parentnode)
            parentnode = parent[index]
            nodePath.append(parentnode)
    nodePath = nodePath[::-1]

    return nodePath

# Function to check if Goal is reached.
def goalReached(newNode, goal):

    if (newNode.x - goal[0]) ** 2 + (newNode.y - goal[1]) ** 2 <= (1.5 ) ** 2:
        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            parentList.append(newNode.parent)
            childList.append((newNode.x,newNode.y))
            costList.append(newNode.totalCost)
            nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            nodeList.sort()
        else:

            index = childList.index((newNode.x,newNode.y))

            if costList[index] > node.totalCost:
                costList[index] = node.totalCost
                parentList[index] = node.parent
                nodeList.sort()

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
        new_x, new_y, new_angle = generateApproxCoordinates(node)
        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
        while True:
            status, newNode = firstAction(node,node.angle)
            if status:
                if goalReached(newNode, goal):
                    parentList.append(newNode.parent)
                    break

            status, newNode = secondAction(node,node.angle)
            if status:
                if goalReached(newNode, goal):
                    parentList.append(newNode.parent)
                    break

            status, newNode = thirdAction(node,node.angle)
            if status:
                if goalReached(newNode, goal):
                    parentList.append(newNode.parent)
                    break

            status, newNode = fourthAction(node,node.angle)
            if status:
                if goalReached(newNode, goal):
                    parentList.append(newNode.parent)
                    break

            status, newNode = fifthAction(node,node.angle)
            if status:
                if goalReached(newNode, goal):
                    parentList.append(newNode.parent)
                    break

            count += 1

            popped = nodeList.pop(0)
            node = nodeList[0]
            if check_Obstacle(node.x, node.y):
                node = popped
                nodeList.pop(1)

            new_x, new_y, new_angle = generateApproxCoordinates(node)
            if new_angle == 0:
                new_angle = int(1)
            else:
                new_angle = int(360 / new_angle)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            ExploredNodeList.append((node.x, node.y))

            ExploredParentNodeList.append(node.parent)

    return ExploredNodeList

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
while True:
    if check_Obstacle(start[0], start[1]):
        print("Start inside the obstacle:")
        start = get_User_Input("Start Node")
    else:
        break
end = get_User_Input("Goal Node")
goal = (int(end[0]), int(end[1]))

step_flag = False
angle_flag = False
while True:
    try:
        stepSize = int(input("Enter the step size in range 1-10: "))

        if stepSize< 1 or stepSize>10:
            print("Step Size Out of Bounds!!")
            step_flag = True
            continue
        angle = int(input("Enter the start angle in degrees: "))
        if angle <-360 or angle >360:
            print("Angle Out of Bounds!!")
            angle_flag = True
            continue
        else:
            break
    except:
        if step_flag is True:
            print("Enter a valid integer in range 1-10.")
        if angle_flag is True:
            print("Enter a valid angle in range -360 to 360 degrees")

node = Node(int(start[0]), int(start[1]), calcEuclideanDist(start[0],start[1]),0,calcEuclideanDist(start[0],start[1]), (0, 0),angle, 0 , 0 , 0)

start_time = time.time()


# Check if the input goal lies within the obstacle space.
if check_Obstacle(goal[0], goal[1]):
    print("Goal cannot be reached")
else:
    # aStar(node, goal)
    try:
        print("Exploring nodes...")
        ExploredNodeList =aStar(node, goal)
    except:
        # Print the following if the goal cannot be reached since no path is available
        print("The radius and clearance is too Big!! Goal cannot be reached !!")
        flag= True

    if flag is False:
        print("Backtracking...")
        nodepath = backTracking(parentList, childList)

    simulation = False

    end_time = time.time()
    print("Total time taken", end_time - start_time)
    if flag is False:
        # for pixel in nodepath:
        #     print(pixel[0], pixel[1])
        #     draw_Optimal_Nodes(pixel[0], pixel[1])
        fig = plt.figure()
        fig.set_dpi(100)
        fig.set_size_inches(8.5, 6)
        ax = plt.axes(xlim=(0, 300), ylim=(0, 200))
        xdata, ydata = [], []
        x_data, y_data = [], []
        lns, = plt.plot([], [], 'ro', markersize=1)
        ln, = plt.plot([], [], 'g+', markersize=1)


        def init():
            ax.set_xlim(0, 300)
            ax.set_ylim(0, 200)
            return lns,  #ln,


        def update(frame):

            if frame < len(1,ExploredNodeList):

                xdata.append(ExploredNodeList[frame][0])
                ydata.append(ExploredNodeList[frame][1])
                lns.set_data(xdata, ydata)
            if frame > len(ExploredNodeList):
                # frame =0
                # if frame < len(nodepath):
                x_data.append(nodepath[frame-len(ExploredNodeList)][0])
                y_data.append(nodepath[frame-len(ExploredNodeList)][1])
                ln.set_data(x_data, y_data)


            return  lns, #ln,

        def init1():
            ax.set_xlim(0, 300)
            ax.set_ylim(0, 200)
            return  ln,


        def update1(frame):


            if frame < len(nodepath):
                x_data.append(nodepath[frame][0])
                y_data.append(nodepath[frame][1])
                ln.set_data(x_data, y_data)
            return  ln,


        def load_Images():
            original = []
            title = []
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('Output_video2.avi', fourcc, 20.0, (728, 511))
            filenames = [f for f in glob.iglob("Node/*")]
            filenames.sort()
            for filename in filenames:
                img = cv2.imread(filename)
                print(filename)
                out.write(img)
                original.append(img)
            time.sleep(1)
            length = len(original)
            # print('Updated Images')
            # return original#, title, length


        goalNode = plt.scatter(goal[0], goal[1], s=10, color='g'),
        circle = plt.Circle((coord_circle[1]), coord_circle[0], fc=None)
        rectangle = plt.Polygon(coord_rectangle)
        rhombus = plt.Polygon(coord_rhombus)
        polygon = plt.Polygon(coord_polygon)
        ellipse = Ellipse((coord_ellipse[1]), coord_ellipse[0][0], coord_ellipse[0][1], 0)
        obstacles = [circle, rectangle, rhombus, polygon, ellipse]
        for obstacle in obstacles:
            plt.gca().add_patch(obstacle)
        count = 0
        for expnode in range(1,len(ExploredNodeList)):
            try:
                parent_x = ExploredParentNodeList[expnode*10][0]
                parent_y = ExploredParentNodeList[expnode*10][1]
                node_x = ExploredNodeList[expnode*10][0]
                node_y = ExploredNodeList[expnode*10][1]
                plt.quiver(parent_x, parent_y, node_x - parent_x , node_y-parent_y , units='xy', scale=1, color='orange')
                if 0<=count<10:
                    plt.savefig(r"./Node/0000000"+str(count)+".png",bbox_inches='tight')
                if 10<=count<100:
                    plt.savefig(r"./Node/000000"+str(count)+".png",bbox_inches='tight')
                if 100 <= count < 1000:
                    plt.savefig(r"./Node/00000"+str(count)+".png",bbox_inches='tight')
                if 1000<=count<10000:
                    plt.savefig(r"./Node/0000"+str(count)+".png",bbox_inches='tight')
                if 10000<=count<100000:
                    plt.savefig(r"./Node/000"+str(count)+".png",bbox_inches='tight')
                if 100000 <= count < 1000000:
                    plt.savefig(r"./Node/00"+str(count)+".png",bbox_inches='tight')

                count = count+1
            except:
                break
        # count = 0
        for pathnode in range(1,len(nodepath)):
            if pathnode >= len(nodepath) - 1:
                break
            plt.quiver(nodepath[pathnode][0], nodepath[pathnode][1], nodepath[pathnode + 1][0] - nodepath[pathnode][0],
                       nodepath[pathnode + 1][0] - nodepath[pathnode][0], units='xy', scale=1,
                       color='black')
            if 0 <= count < 10:
                plt.savefig(r"./Node/0000000" + str(count) + ".png", bbox_inches='tight')
            if 10 <= count < 100:
                plt.savefig(r"./Node/000000" + str(count) + ".png", bbox_inches='tight')
            if 100 <= count < 1000:
                plt.savefig(r"./Node/00000" + str(count) + ".png", bbox_inches='tight')
            if 1000 <= count < 10000:
                plt.savefig(r"./Node/0000" + str(count) + ".png", bbox_inches='tight')
            if 10000 <= count < 100000:
                plt.savefig(r"./Node/000" + str(count) + ".png", bbox_inches='tight')
            if 100000 <= count < 1000000:
                plt.savefig(r"./Node/00" + str(count) + ".png", bbox_inches='tight')
            count = count + 1

        load_Images()

        # ani = FuncAnimation(fig, update, frames=len(ExploredNodeList) + 1,
        #                     init_func=init, interval=2, blit=True, repeat=True)

        plt.show()








