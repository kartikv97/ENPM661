
import time
import cv2
import glob
from ActionSpace import *
from utils import*
import init as st
from map import *
from How_to_plot_curve import *
from matplotlib.patches import Rectangle, Circle





flag= False
height = 200


def addNode(newNode):
    if check_Obstacle(newNode.x, newNode.y):
        return
    else:
        new_x, new_y, new_angle = generateApproxCoordinates(newNode)

        new_angle = int((new_angle * 72)/360)

        if Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle] == 0:
            st.parentList.append(newNode.parent)
            st.parentAngleList.append(newNode.parentAngle)
            st.childList.append((newNode.x, newNode.y))
            st.ActionList.append(newNode.RPM)
            st.AngleList.append(newNode.angle)
            st.costList.append(newNode.totalCost)
            st.nodeList.append(newNode)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle] = 1
            st.nodeList.sort()
        else:

            index = st.childList.index((newNode.x, newNode.y))

            if st.costList[index] > newNode.totalCost:
                st.costList[index] = newNode.totalCost
                st.parentList[index] = newNode.parent
                st.parentAngleList[index]= newNode.parentAngle
                st.nodeList.sort()



# Main aStar algorithm
def aStar(node, goal, rpm1, rpm2):
    count = 0
    state = False

    if goalReached(node, goal):
        return
    if check_Obstacle(node.x, node.y) and check_Obstacle(goal[0], goal[1]):
        return
    else:
        st.nodeList.append(node)
        st.parentList.append((0, 0))
        st.parentAngleList.append(0)
        st.childList.append((node.x, node.y))
        st.ActionList.append((0,0))
        st.AngleList.append(node.angle)
        st.costList.append(0)

        new_x, new_y, new_angle = generateApproxCoordinates(node)


        new_angle = int((new_angle * 72)/360)


        Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle ] = 1

        Action_space = [(0, rpm1), (rpm1, 0), (rpm1, rpm1), (0, rpm2), (rpm2, 0), (rpm2, rpm2), (rpm1, rpm2), (rpm2, rpm1)]

        goal_flag = False
        while True:
            cnt = 0
            for action in Action_space:
                cnt = cnt+1
                status, newNode = Action( action[0],action[1] , node, goal)
                if status:
                    if goalReached(newNode, goal):
                        goal_flag = True
                        st.parentList.append(newNode.parent)
                        st.parentAngleList.append(newNode.parentAngle)

                        break
                    else:
                        addNode(newNode)
            if goal_flag == True:
                break


            count += 1
            print(len(st.nodeList))
            popped = st.nodeList.pop(0)

            node = st.nodeList[0]
            print("current node:", node.x, node.y , node.angle, node.cTc, node.cTg,node.totalCost)
            if check_Obstacle(node.x, node.y):
                node = popped
                st.nodeList.pop(1)

            new_x, new_y, new_angle = generateApproxCoordinates(node)

            new_angle = int((new_angle * 72)/360)
            Visited_Nodes_List[int(new_x * 2) - 1][int(new_y * 2) - 1][new_angle ] = 1
            st.ExploredNodeList.append((node.x, node.y))
            st.ExploredNodeAngleList.append(node.parentAngle)
            st.ExploredNodeActionList.append(node.RPM)

            st.ExploredParentNodeList.append(node.parent)

    return st.ExploredNodeList


# Getting inputs from the user
simulation = False

st.init()
rpm_flag = False
while rpm_flag == False:
    try:
        rpm1, rpm2 =  input("Enter Left wheel and Right wheel RPM(values seperated by space):").split()
        rpm1, rpm2 = int(rpm1), int(rpm2)

        start = get_User_Input("Start Node")
        end = get_User_Input("Goal Node")
        rpm_flag = True
    except:
        pass

while True:
    if check_Obstacle(start[0], start[1]):
        print("Start inside the obstacle:")
        start = get_User_Input("Start Node")
    else:
        break

goal = (float(end[0]), float(end[1]))

step_flag = False
angle_flag = False
while True:
    try:
        angle = int(input("Enter the start angle in degrees: "))
        if angle <-360 or angle >360:
            print("Angle Out of Bounds!!")
            angle_flag = True
            continue
        else:
            break
    except:
        if angle_flag is True:
            print("Enter a valid angle in range -360 to 360 degrees")

node = st.Node(int(start[0]), int(start[1]), calcEuclideanDist(start[0],start[1],goal),0,calcEuclideanDist(start[0],start[1],goal), (0, 0),angle, 0 , 0 , 0)

start_time = time.time()

print("Entered goal :",goal[0], goal[1])

# Check if the input goal lies within the obstacle space.
if check_Obstacle(goal[0], goal[1]):
    print("Goal cannot be reached")
else:
    # aStar(node, goal, rpm1, rpm2)
    try:
        print("Exploring nodes...")
        ExploredNodeList =aStar(node, goal, rpm1, rpm2)
    except:
        # Print the following if the goal cannot be reached since no path is available
        print("The radius and clearance is too Big!! Goal cannot be reached !!")
        flag= True

    if flag is False:
        print("Backtracking...")
        nodepath, actionPath, angleList = backTracking(st.parentList, st.childList, st.ActionList, st.parentAngleList, st.test)

        nodepath.pop(0)

    simulation = False

    end_time = time.time()

    print("Total time taken", end_time - start_time)


    if flag is False:

        def generateVideo():
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('Output_video.avi', fourcc, 10.0, (550, 543))
            filenames = [f for f in glob.iglob("Node/*")]
            filenames.sort()
            for filename in filenames:
                img = cv2.imread(filename)
                print(filename)
                out.write(img)




        ################################# Generate the map objects #####################################

        circle1 = plt.Circle((coords_Circle1[1]), coords_Circle1[0], fc=None)
        circle2 = plt.Circle((coords_Circle2[1]), coords_Circle2[0], fc=None)
        circle3 = plt.Circle((coords_Circle3[1]), coords_Circle3[0], fc=None)
        circle4 = plt.Circle((coords_Circle4[1]), coords_Circle4[0], fc=None)
        square1 = plt.Polygon(coords_square1)
        square2 = plt.Polygon(coords_square2)
        square3 = plt.Polygon(coords_square3)

        obstacles = [circle1, circle2, circle3, circle4, square1, square2, square3]

        for obstacle in obstacles:
            plt.gca().add_patch(obstacle)

        plt.gca().add_patch(Circle((goal[0], goal[1]), 0.45,color='green', fill=None))

        p4 = plt.plot(start[0],start[1], color='cyan', marker='o', markersize=1, label="Start Node")
        p5 = plt.plot(goal[0], goal[1], color='cyan', marker='o', markersize=1, label = 'Goal Node')
        plt.grid()


        plt.xlim(-7, 7)
        plt.ylim(-7, 7)
        plt.gca().add_patch(Rectangle((-5., -5.), 10., 10., fill=None))
        plt.gca().add_patch(Rectangle((-5.1, -5.1), 10.2, 10.2, fill=None))
        plt.axis([-7,7,-7 ,7])

        # print("len explored:",len(st.ExploredNodeList))
        # print("len optimal:", len(nodepath))

        ################################ Plot the output #####################################
        frame_rate = 1

        node_count = 0
        for node in st.ExploredNodeList:
            try:
                p1 = plt.plot(node[0], node[1], '.', color='brown', markersize=1, label='Explored Nodes')
                plot([st.ExploredParentNodeList[node_count*frame_rate]],[st.ExploredNodeAngleList[node_count*frame_rate]],[st.ExploredNodeActionList[node_count*frame_rate]], [actionPath[0]], [angleList[0]],'Explored')
            except:
                break
            node_count = node_count +1




        node_count = 0
        for node in nodepath:
            p1 = plt.plot(node[0], node[1], 'k.', markersize=1, label='Optimal Path Nodes')

        plot(st.ExploredParentNodeList,st.ExploredNodeAngleList,st.ExploredNodeActionList, actionPath, angleList,'Optimal')

        # Uncomment following line to generate video.
        # generateVideo()

        plt.show()
        plt.close()



print("****************************** Starting Vrep Simulation **********************************")

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')

    time = 0
#retrieve motor  handles
    errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,'wheel_left_joint',vrep.simx_opmode_blocking)
    errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,'wheel_right_joint',vrep.simx_opmode_blocking)
    r, signalValue = vrep.simxGetFloatSignal(clientID, 'Turtlebot2_simulation_time', vrep.simx_opmode_streaming)

    path_speeds= actionPath

    for k in path_speeds:
        time = 0
        err_code1 = 1
        err_code2 = 2
        #print(type(k[0]))
        while(err_code1 != 0 and err_code2 != 0):
            err_code1 = vrep.simxSetJointTargetVelocity(clientID, left_motor_handle, k[0], vrep.simx_opmode_streaming)
            #print(err_code1)

            err_code2 = vrep.simxSetJointTargetVelocity(clientID, right_motor_handle, k[1], vrep.simx_opmode_streaming)
            #print(err_code2)

        r, signalValue = vrep.simxGetFloatSignal(clientID, 'Turtlebot2_simulation_time', vrep.simx_opmode_buffer)

        simulation_runtime_per_action = 1.14

        while(time<simulation_runtime_per_action):

            r, signalValue2 = vrep.simxGetFloatSignal(clientID, 'Turtlebot2_simulation_time', vrep.simx_opmode_buffer)

            time = signalValue2 - signalValue

    errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle,0, vrep.simx_opmode_streaming)
    errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle,0, vrep.simx_opmode_streaming)

    # Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    vrep.simxGetPingTime(clientID)

    # Now close the connection to V-REP:
    vrep.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')


















