
import numpy as np

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

    return final_input

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

# Function to calculate Euclidean Distance between current node and the goal node.
def calcEuclideanDist(curr_coordinate_x, curr_coordinate_y,goal):
    cTg = np.sqrt((curr_coordinate_x-goal[0])**2 + (curr_coordinate_y-goal[1])**2 )
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
