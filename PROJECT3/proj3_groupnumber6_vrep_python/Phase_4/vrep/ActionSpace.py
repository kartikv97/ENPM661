

from utils import *
import init as st
import numpy as np
import math
from map import *


def Action(ur,ul,node,goal):

    t=0
    dt = 0.1
    r = 0.038
    L = 0.3175
    dx=node.x
    dy=node.y
    d_theta =np.deg2rad(node.angle)

    while t <1:
        t = t + dt
        dx += (r / 2) * (ul + ur) * np.cos(d_theta) * dt
        dy += (r / 2) * (ul + ur) * np.sin(d_theta) * dt
        d_theta += (r / L) * (ur - ul) * dt
        if check_Obstacle(dx, dy):
            return False, node
    d_theta = np.rad2deg(d_theta)

    newNode = st.Node(0, 0, math.inf, math.inf, math.inf, (0, 0), math.inf, math.inf, math.inf, math.inf)
    newNode.x = dx
    newNode.y = dy
    newNode.angle = d_theta
    newNode.RPM = (ul,ur)
    for i in range(1,13):
        if newNode.angle > 360*i:
            newNode.angle = newNode.angle - 360*(i+1)
        elif newNode.angle < -360*i:
            newNode.angle = newNode.angle + 360*(i+1)
        elif -360 < newNode.angle < 0:
            newNode.angle = newNode.angle + 360
        else:
            newNode.angle = newNode.angle



    if newNode.x < -5 or newNode.x > 5 or newNode.y < -5 or newNode.y > 5  :
        return False, node

    if isNodeVisited(newNode) == False:
        return False, node

    else:

        newNode.cTc = node.cTc + np.sqrt(np.power(node.x - dx, 2)+np.power(node.y-dy, 2))
        newNode.cTg = calcEuclideanDist(newNode.x,newNode.y,goal)
        newNode.totalCost = newNode.cTc + newNode.cTg
        newNode.parent = (node.x, node.y)
        newNode.parentAngle = node.angle

    return True, newNode


# Function to check if Goal is reached.
def goalReached(newNode, goal):
    if (newNode.x - goal[0]) ** 2 + (newNode.y - goal[1]) ** 2 <= (0.45) ** 2:

        new_x, new_y, new_angle = generateApproxCoordinates(newNode)
        new_angle = int((new_angle * 72) / 360)

        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle] == 0:
            st.parentList.append(newNode.parent)
            st.parentAngleList.append(newNode.parentAngle)
            st.childList.append((newNode.x, newNode.y))
            st.ActionList.append(newNode.RPM)
            st.costList.append(newNode.totalCost)
            st.nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle] = 1

        else:

            index = st.childList.index((newNode.x, newNode.y))

            if st.costList[index] > newNode.totalCost:
                st.costList[index] = newNode.totalCost
                st.parentList[index] = newNode.parent
                st.parentAngleList[index]=newNode.parentAngle


        print('**************************   GOAL REACHED  *******************************')
        print('Cost took to reach the goal is: ' + str(newNode.totalCost))
        return True
    return False




