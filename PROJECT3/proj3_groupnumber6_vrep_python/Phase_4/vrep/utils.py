
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
                if float(input_val)<-5 or float(input_val)>5:
                    flag = False
                    print("Entered input is out of bounds. Please enter a valid input!!")
                    break
                else:
                    flag =True
                    final_input[count] = np.array(float(input_val))
            if a == "Y":
                if float(input_val)<-5 or float(input_val)>5:
                    flag = False
                    print("Entered input is out of bounds. Please enter a valid input!!")
                    break
                else:
                    flag =True
                    final_input[count] = np.array(float(input_val))
            count = count+1

    return final_input

def generateApproxCoordinates(node):
    angle_threshold_resolution = 5

    for i in range(int(360 / angle_threshold_resolution)):
        if i * angle_threshold_resolution <= int(node.angle)<= i*angle_threshold_resolution + angle_threshold_resolution:
            if i *angle_threshold_resolution <= node.angle < i*angle_threshold_resolution + angle_threshold_resolution/2:
                new_angle = i * angle_threshold_resolution
                break
            else:
                new_angle = i*angle_threshold_resolution + angle_threshold_resolution
                break
    scale = 100

    if int(node.x*scale +5*scale) <= node.x*scale +5*scale < int(node.x*scale +5*scale) + 0.25:
        new_x = int(node.x*scale+5*scale)
    elif int(node.x*scale+5*scale) + 0.25 <= node.x*scale+5*scale < int(node.x*scale+5*scale) + 0.5:
        new_x = int(node.x*scale+5*scale) + 0.5
    elif int(node.x*scale+5*scale) + 0.5 <= node.x*scale +5*scale < int(node.x*scale+5*scale) + 0.75:
        new_x = int(node.x*scale+5*scale) + 0.5
    else:
        new_x = int(node.x*scale+5*scale) + 1
    if int(node.y*scale+5*scale)<= node.y*scale+5*scale <int(node.y*scale+5*scale)+0.25:
        new_y = int(node.y*scale+5*scale)
    elif int(node.y*scale+5*scale) + 0.25<= node.y*scale+5*scale <int(node.y*scale+5*scale)+0.5:
        new_y = int(node.y*scale+5*scale) + 0.5
    elif int(node.y*scale+5*scale) + 0.5<= node.y*scale+5*scale <int(node.y*scale+5*scale)+0.75:
        new_y = int(node.y*scale+5*scale) + 0.5
    else:
        new_y = int(node.y*scale+5*scale) + 1

    return new_x , new_y , new_angle



########################################################################################################################

Visited_Nodes_List = [[[0 for k in range(73)] for j in range(2000)] for i in range (2000)]

########################################################################################################################
def isNodeVisited(node):

    new_x, new_y, new_angle = generateApproxCoordinates(node)

    new_angle = int((new_angle * 72)/360)
    try:
        if Visited_Nodes_List[int(new_x*2)-1][int(new_y*2)-1][new_angle] == 1:
            return False
        else:
            return True
    except:
        print("ERROR:", node.x, node.y, node.angle, new_x, new_y, new_angle)

# Function to calculate Euclidean Distance between current node and the goal node.
def calcEuclideanDist(curr_coordinate_x, curr_coordinate_y,goal):
    cTg = np.sqrt((curr_coordinate_x- goal[0])**2 + (curr_coordinate_y- goal[1])**2 )
    # cTg = abs(goal[0]-curr_coordinate_x)+abs(goal[1]-curr_coordinate_y)                                      # MANHATTAN DISTANCE FORMULA
    return cTg


# Function to Backtrack from the Goal Node to Start Node
def backTracking(parent, child, actions, angles, ang):


    # starting from the last parent node
    parentnode = parent[len(parent) - 1]
    childnode = child[len(child) - 1]
    action_node = actions[len(actions)-1]
    angle_node = angles[len(angles)-1]
    nodePath = []
    actionPath =[]
    angleList = []

    nodePath.append(childnode)
    actionPath.append(action_node)



    ind = child.index(parentnode)
    actionPath.append(actions[ind])
    angleList.append(angle_node)
    nodePath.append(parentnode)
    while parentnode != (0, 0):
        if parentnode in child:
            index = child.index(parentnode)
            parentnode = parent[index]
            nodePath.append(parentnode)
            actionPath.append(actions[index])
            angleList.append(angles[index])

    actionPath = actionPath[::-1]
    nodePath = nodePath[::-1]
    angleList = angleList[::-1]

    return nodePath,actionPath,angleList
