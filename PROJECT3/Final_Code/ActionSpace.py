
from test_environment import *
from utils import *
import init as st



def firstAction(node,angle,stepSize,goal):

    # print("FIRST ACTION:::::::::::::::::::::::")
    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle))
    newNode.angle = angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node

    # if check_Obstacle(node.x, node.y):
    #     return False, node

    if isNodeVisited(newNode) == False:
        return False, node

    else:


        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
        newNode.angle = angle


    return True, newNode

def secondAction(node,angle,stepSize,goal):

    # print("SECOND ACTION:::::::::::::::::::::::")
    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle + 30))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle + 30))
    newNode.angle = angle + 30
    if newNode.angle > 360:
        newNode.angle = newNode.angle - 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node

    # if check_Obstacle(node.x, node.y):
    #     return False, node
    if isNodeVisited(newNode) == False:
        return False, node

    else:


        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)



    return True, newNode

def thirdAction(node,angle,stepSize,goal):

    # print("THIRD ACTION:::::::::::::::::::::::")
    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle + 60))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle + 60))
    newNode.angle = angle + 60
    if newNode.angle > 360:
        newNode.angle = newNode.angle - 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    # if check_Obstacle(node.x, node.y):
    #     return False, node

    if isNodeVisited(newNode) == False:
        return False, node

    else:


        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)


    return True, newNode

def fourthAction(node,angle,stepSize,goal):

    # print("FOURTH ACTION:::::::::::::::::::::::")
    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle - 30))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle - 30))
    newNode.angle = angle - 30
    if newNode.angle < 0:
        newNode.angle = newNode.angle + 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    # if check_Obstacle(node.x, node.y):
    #     return False, node

    if isNodeVisited(newNode)== False:
        return False, node

    else:


        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x,node.y)



    return True, newNode

def fifthAction(node,angle,stepSize,goal):

    # print("FIFTH ACTION:::::::::::::::::::::::")
    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0),math.inf,math.inf,math.inf,math.inf)
    newNode.x = node.x + stepSize * np.cos(np.deg2rad(angle - 60))
    newNode.y = node.y + stepSize * np.sin(np.deg2rad(angle - 60))
    newNode.angle = angle - 60
    if newNode.angle < 0:
        newNode.angle = newNode.angle + 360
    else:
        newNode.angle = newNode.angle
    if newNode.x < 0 or newNode.x > 300 or newNode.y < 0 or newNode.y > 200  :
        return False, node
    # if check_Obstacle(node.x, node.y):
        return False, node
    if isNodeVisited(newNode) == False:
        return False, node
    else:

        newNode.cTc = node.cTc + stepSize
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x,node.y)


    return True, newNode

# Function to check if Goal is reached.
def goalReached(newNode, goal):

    if (newNode.x - goal[0]) ** 2 + (newNode.y - goal[1]) ** 2 <= (1.5 ) ** 2:
        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        if new_angle == 0:
            new_angle = int(1)
        else:
            new_angle = int(360 / new_angle)
        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] == 0:
            st.parentList.append(newNode.parent)
            st.childList.append((newNode.x,newNode.y))
            st.costList.append(newNode.totalCost)
            st.nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle - 1] = 1
            st.nodeList.sort()
        else:

            index = st.childList.index((newNode.x,newNode.y))

            if st.costList[index] > newNode.totalCost:
                st.costList[index] = newNode.totalCost
                st.parentList[index] = newNode.parent
                st.nodeList.sort()

        print('Goal Reached')
        print('Cost took to reach the goal is: ' + str(newNode.totalCost))
        return True
    return False

