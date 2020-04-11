
import time
from matplotlib.animation import FuncAnimation
import cv2
import glob
from ActionSpace import *
from utils import*
import init as st
from map import *
from How_to_plot_curve import *
from matplotlib.patches import Rectangle





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
            # print("ADDED New Node:", newNode.x,newNode.y, newNode.angle)
            # print("visited list location:",int(new_x * 2) - 1, int(new_y * 2) - 1, new_angle - 1)
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
                        # st.ExploredParentNodeList.append((newNode.x,newNode.y))
                        st.parentAngleList.append(newNode.parentAngle)
                        # st.ExploredNodeList.append((newNode.x, newNode.y))
                        # st.ExploredNodeAngleList.append(newNode.parentAngle)
                        # st.ExploredNodeActionList.append(newNode.RPM)
                        # st.test.append(newNode.angle)
                        break
                    else:
                        # print("NEW node "+str(cnt)+":", newNode.x, newNode.y, newNode.angle, newNode.cTc, newNode.cTg, newNode.totalCost)
                        addNode(newNode)
            if goal_flag == True:
                break


            count += 1
            print(len(st.nodeList))
            popped = st.nodeList.pop(0)
            # print("popped node:", popped.x, popped.y)
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

node = st.Node(int(start[0]), int(start[1]), calcEuclideanDist(start[0],start[1],goal),0,calcEuclideanDist(start[0],start[1],goal), (0, 0),angle, 0 , 0 , 0)

start_time = time.time()

print("Entered goal :",goal[0], goal[1])
# Check if the input goal lies within the obstacle space.
if check_Obstacle(goal[0], goal[1]):
    print("Goal cannot be reached")
else:
    aStar(node, goal, rpm1, rpm2)
    try:
        print("Exploring nodes...")
        # ExploredNodeList =aStar(node, goal, rpm1, rpm2)
    except:
        # Print the following if the goal cannot be reached since no path is available
        print("The radius and clearance is too Big!! Goal cannot be reached !!")
        flag= True

    if flag is False:
        print("Backtracking...")
        nodepath, actionPath, angleList = backTracking(st.parentList, st.childList, st.ActionList, st.parentAngleList, st.test)

        nodepath.pop(0)
        # print("nodepath:",nodepath)
        # print("actionpath:", actionPath)
        # print("angleList:", angleList)
        #
        # print("length nodepath:", len(nodepath))
        # print("length actionpath:", len(actionPath))
        # print("length angleList:", len(angleList))
        #
        print("ExploredNodeList:", st.ExploredNodeList)
        # print("ExploredNodeActionList:", st.ExploredNodeActionList)
        # print("ExploredNodeAngleList:", st.ExploredNodeAngleList)
        # print("ExploredParentNodeList:", st.ExploredParentNodeList)
        # print("length ExploredNodeList:", len(st.ExploredNodeList))
        # print("length ExploredNodeAngleList:", len(st.ExploredNodeAngleList))
        # print("length ExploredNodeActionList:", len(st.ExploredNodeActionList))
        # print("length ExploredParentNodeList:", len(st.ExploredParentNodeList))

    simulation = False

    end_time = time.time()
    print("Total time taken", end_time - start_time)
    if flag is False:
        # for pixel in nodepath:
        #     print(pixel[0], pixel[1])
        #     draw_Optimal_Nodes(pixel[0], pixel[1])
        fig = plt.figure()
        fig.set_dpi(100)
        fig.set_size_inches(5, 5)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        axis = fig.add_subplot(xlim=(-5, 5), ylim=(-5, 5))

        xdata, ydata = [], []
        x_data, y_data = [], []
        lns, = plt.plot([], [], '.',color='brown', markersize=0.1)
        ln, = plt.plot([], [], 'k.', markersize=0.5)


        # def init():
        #     ax.set_xlim(0, 300)
        #     ax.set_ylim(0, 200)
        #     return lns,  #ln,
        #
        #
        # def update(frame):
        #
        #     if frame < len(1,ExploredNodeList):
        #
        #         xdata.append(ExploredNodeList[frame][0])
        #         ydata.append(ExploredNodeList[frame][1])
        #         lns.set_data(xdata, ydata)
        #     if frame > len(ExploredNodeList):
        #         # frame =0
        #         # if frame < len(nodepath):
        #         x_data.append(nodepath[frame-len(ExploredNodeList)][0])
        #         y_data.append(nodepath[frame-len(ExploredNodeList)][1])
        #         ln.set_data(x_data, y_data)
        #
        #
        #     return  lns, #ln,

        def init1():
            axis.set_xlim(-5, 5)
            axis.set_ylim(-5, 5)
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
            out = cv2.VideoWriter('Output_video2.avi', fourcc, 20.0, (550, 543))
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



        circle1 = plt.Circle((coords_Circle1[1]), coords_Circle1[0], fc=None)
        circle2 = plt.Circle((coords_Circle2[1]), coords_Circle2[0], fc=None)
        circle3 = plt.Circle((coords_Circle3[1]), coords_Circle3[0], fc=None)
        circle4 = plt.Circle((coords_Circle4[1]), coords_Circle4[0], fc=None)
        square1 = plt.Polygon(coords_square1)
        square2 = plt.Polygon(coords_square2)
        square3 = plt.Polygon(coords_square3)
        # square4 = plt.Polygon(coords_square4)
        # square5 = plt.Polygon(coords_square5)
        obstacles = [circle1, circle2, circle3, circle4, square1, square2, square3]

        for obstacle in obstacles:
            plt.gca().add_patch(obstacle)



        # plt.show()

        # fig = plt.figure()
        # fig.set_dpi(100)
        # fig.set_size_inches(8.5, 6)
        # ax = plt.axes(xlim=(0, 300), ylim=(0, 200))
        # xdata, ydata = [], []
        # x_data, y_data = [], []
        # lns, = plt.plot([], [], 'ro', markersize=0.1)
        # ln, = plt.plot([], [], 'g+', markersize=0.1)


        def init():
            axis.set_xlim(-5, 5)
            axis.set_ylim(-5, 5)
            return lns, ln,

        # cmmented by kushagra agrawal************************
        def update(frame):
            # print(frame)
            # print("x:", frame[0])
            if frame < len(st.ExploredNodeList):
                for node in st.ExploredNodeList:
                    xdata.append(node[0])
                    ydata.append(node[1])
                    lns.set_data(xdata, ydata)
            if frame < len(nodepath):
                for pixel in nodepath:
                    x_data.append(pixel[0])
                    y_data.append(pixel[1])
                    ln.set_data(x_data, y_data)
            return lns, ln,                    #****************



        # def update(frame):
        #     # print(frame)
        #     # print("x:", frame[0])
        #     for expnode in range(1, len(st.ExploredNodeList)):
        #         parent_x = st.ExploredParentNodeList[expnode][0]
        #         parent_y = st.ExploredParentNodeList[expnode][1]
        #         node_x = st.ExploredNodeList[expnode][0]
        #         node_y = st.ExploredNodeList[expnode][1]
        #         plt.quiver(parent_x, parent_y, node_x - parent_x , node_y-parent_y , units='xy', scale=1, color='orange')
        #         # for pathnode in nodepath:
        #         #     plt.quiver(nodepath[pathnode][0], nodepath[pathnode][1],nodepath[pathnode + 1][0] - nodepath[pathnode][0],nodepath[pathnode + 1][0] - nodepath[pathnode][0], units='xy', scale=1, color='black')


        # ani = FuncAnimation(fig, update, frames=childList,
        # init_func=init, interval = 2,blit=True,repeat = False)
        # ani = FuncAnimation(fig, update, frames=len(st.ExploredNodeList) + len(nodepath),
        #                     init_func=init, interval=0.1, blit=True, repeat=True)
        # for pathnode in range(len(nodepath)):
        #     if pathnode>len(nodepath)-2:
        #         break
        #     # print(nodepath[pathnode][0])
        #     plt.quiver(nodepath[pathnode][0], nodepath[pathnode][1],nodepath[pathnode + 1][0] - nodepath[pathnode][0],nodepath[pathnode + 1][0] - nodepath[pathnode][0], units='xy', scale=1, color='black')

        # for node_path in nodepath:
        # #     # print("ExploredNode:",ExploredNode)
        #     plt.scatter(node_path[0], node_path[1], s=1, color='b')
        #
        # for ExploredNode in ExploredNodeList:
        # #     # print("ExploredNode:",ExploredNode)
        #     plt.scatter(ExploredNode[0], ExploredNode[1], s=1, color='r')

        # count = 0
        # for expnode in range(1,len(st.ExploredNodeList)):
        #     try:
        #         parent_x = ExploredParentNodeList[expnode*10][0]
        #         parent_y = ExploredParentNodeList[expnode*10][1]
        #         node_x = ExploredNodeList[expnode*10][0]
        #         node_y = ExploredNodeList[expnode*10][1]
        #         plt.quiver(parent_x, parent_y, node_x - parent_x , node_y-parent_y , units='xy', scale=1, color='orange')
        #         if 0<=count<10:
        #             plt.savefig(r"./Node/0000000"+str(count)+".png",bbox_inches='tight')
        #         if 10<=count<100:
        #             plt.savefig(r"./Node/000000"+str(count)+".png",bbox_inches='tight')
        #         if 100 <= count < 1000:
        #             plt.savefig(r"./Node/00000"+str(count)+".png",bbox_inches='tight')
        #         if 1000<=count<10000:
        #             plt.savefig(r"./Node/0000"+str(count)+".png",bbox_inches='tight')
        #         if 10000<=count<100000:
        #             plt.savefig(r"./Node/000"+str(count)+".png",bbox_inches='tight')
        #         if 100000 <= count < 1000000:
        #             plt.savefig(r"./Node/00"+str(count)+".png",bbox_inches='tight')
        #
        #         count = count+1
        #     except:
        #         break
        # # count = 0
        # for pathnode in range(1,len(nodepath)):
        #     if pathnode >= len(nodepath) - 1:
        #         break
        #     plt.quiver(nodepath[pathnode][0], nodepath[pathnode][1], nodepath[pathnode + 1][0] - nodepath[pathnode][0],
        #                nodepath[pathnode + 1][0] - nodepath[pathnode][0], units='xy', scale=1,
        #                color='black')
        #     if 0 <= count < 10:
        #         plt.savefig(r"./Node/0000000" + str(count) + ".png", bbox_inches='tight')
        #     if 10 <= count < 100:
        #         plt.savefig(r"./Node/000000" + str(count) + ".png", bbox_inches='tight')
        #     if 100 <= count < 1000:
        #         plt.savefig(r"./Node/00000" + str(count) + ".png", bbox_inches='tight')
        #     if 1000 <= count < 10000:
        #         plt.savefig(r"./Node/0000" + str(count) + ".png", bbox_inches='tight')
        #     if 10000 <= count < 100000:
        #         plt.savefig(r"./Node/000" + str(count) + ".png", bbox_inches='tight')
        #     if 100000 <= count < 1000000:
        #         plt.savefig(r"./Node/00" + str(count) + ".png", bbox_inches='tight')
        #     count = count + 1

        # load_Images()

        # ani = FuncAnimation(fig, update, frames=len(ExploredNodeList) + 1,
        #                     init_func=init, interval=2, blit=True, repeat=True)

        ###########################################################################################3

        for node in st.ExploredNodeList:
            xdata.append(node[0])
            ydata.append(node[1])
            # lns.set_data(xdata, ydata)
        p1 = plt.plot([xdata], [ydata], '.', color='brown', markersize=1, label='Explored Nodes')

        for pixel in nodepath:
            x_data.append(pixel[0])
            y_data.append(pixel[1])
            # ln.set_data(x_data, y_data)
        p2 = plt.plot([x_data], [y_data], 'k.', markersize=1, label='Optimal Path Nodes')


        ######################################################################
        p3 = plt.Circle((goal[0], goal[1]), 0.45, color='green',fc=None, label= 'Goal Area')

        p4 = plt.plot(start[0],start[1], color='cyan', marker='o', markersize=1, label="Start Node")
        p5 = plt.plot(goal[0], goal[1], color='cyan', marker='o', markersize=1, label = 'Goal Node')
        plt.grid()

        plot(st.ExploredParentNodeList,st.ExploredNodeAngleList,st.ExploredNodeActionList, actionPath, angleList,'Explored')
        plot(st.ExploredParentNodeList,st.ExploredNodeAngleList,st.ExploredNodeActionList, actionPath, angleList,'Optimal')
        # plt.set_aspect('equal')
        plt.xlim(-7, 7)
        plt.ylim(-7, 7)
        plt.gca().add_patch(Rectangle((-5., -5.), 10., 10., fill=None))
        plt.gca().add_patch(Rectangle((-5.1, -5.1), 10.2, 10.2, fill=None))
        plt.axis([-7,7,-7 ,7])



        # count = 0
        # for expnode in range(1,len(st.ExploredNodeList)):
        #     try:
        #         parent_x = ExploredParentNodeList[expnode*10][0]
        #         parent_y = ExploredParentNodeList[expnode*10][1]
        #         node_x = ExploredNodeList[expnode*10][0]
        #         node_y = ExploredNodeList[expnode*10][1]
        #         plt.quiver(parent_x, parent_y, node_x - parent_x , node_y-parent_y , units='xy', scale=1, color='orange')
        #
        #
        #             # lns.set_data(xdata, ydata)
        #
        #
        #         if 0<=count<10:
        #             plt.savefig(r"./Node/0000000"+str(count)+".png",bbox_inches='tight')
        #         if 10<=count<100:
        #             plt.savefig(r"./Node/000000"+str(count)+".png",bbox_inches='tight')
        #         if 100 <= count < 1000:
        #             plt.savefig(r"./Node/00000"+str(count)+".png",bbox_inches='tight')
        #         if 1000<=count<10000:
        #             plt.savefig(r"./Node/0000"+str(count)+".png",bbox_inches='tight')
        #         if 10000<=count<100000:
        #             plt.savefig(r"./Node/000"+str(count)+".png",bbox_inches='tight')
        #         if 100000 <= count < 1000000:
        #             plt.savefig(r"./Node/00"+str(count)+".png",bbox_inches='tight')
        #
        #         count = count+1
        #     except:
        #         break

        print("len explored:",len(st.ExploredNodeList))
        print("len optimal:", len(nodepath))

        # node_count = 0
        # for node in st.ExploredNodeList:
        #     # xdata.append(node[0])
        #     # ydata.append(node[0])
        #     try:
        #         p1 = plt.plot(node[0], node[1], '.', color='brown', markersize=1, label='Explored Nodes')
        #         plot([st.ExploredParentNodeList[node_count]],[st.ExploredNodeAngleList[node_count]],[st.ExploredNodeActionList[node_count]], [actionPath[0]], [angleList[0]],'Explored')
        #     except:
        #         break
        #     node_count = node_count +1



#####################################################################
        # node_count = 0
        # for node in nodepath:
        #     # xdata.append(node[0])
        #     # ydata.append(node[0])
        #     # try:
        #     p1 = plt.plot(node[0], node[1], 'k.', markersize=1, label='Optimal Path Nodes')
        # # plot(st.ExploredParentNodeList, [st.ExploredNodeAngleList[0]],
        # #      st.ExploredNodeActionList[0]], [actionPath[node_count]], [angleList[node_count]], 'Optimal')
        #     # except:
        #     #     break
        #     # node_count = node_count + 1
        # plot(st.ExploredParentNodeList,st.ExploredNodeAngleList,st.ExploredNodeActionList, actionPath, angleList,'Optimal')









        plt.show()
        plt.close()




















