
import numpy as np
import time
import os

initial_node = np.array( [[8, 6, 7],
       [2, 5, 4],
       [3, 0, 1]])


# initial_node = [1,3,0,5,2,6,4,7,8]

# initial_node = np.array([[1,2,3],[5,4,6],[8,7,0]])
# initial_node_mat = np.array([[1,2,3],[5,4,6],[8,7,0]])
initial_node_mat= initial_node.flatten()
# initial_node = np.array([[7,2,3],[1,0,6],[5,8,4]])
# initial_node_matrix = np.array([[1,2,3],[5,4,6],[8,7,0]])
initial_node_matrix = initial_node.copy()
def is_Node_Solvable(node):
    node_list = np.reshape(node, 9)
    counter_states = 0
    for i in range(9):
        if not node_list[i] == 0:
            check_elem = node_list[i]
            for x in range(i + 1, 9):
                if check_elem < node_list[x] or node_list[x] == 0:
                    continue
                else:
                    counter_states += 1
    if counter_states % 2 == 0:
        print("The entered puzzle is solvable, finding optimal solution now.")
        return True
    else:
        print("The entered puzzle is insolvable. \nExiting the game!!. \nBye Bye!!")
        exit(0)
# def Get_User_Input():
#     print("Enter the values of input node in the range [0-8] without repetition :\n")
#     flag = False
#     final_input = np.zeros(9)
#     while flag is False:
#         for i in range (9):
#             input_val = (input("Enter number " + str(i+1) +" : "))
#             if len(input_val) is 0:
#                 print("You need to enter a value in range [0-8]. Don't leave a number blank!!!")
#                 flag = False
#                 break
#             if int(input_val)<0 or int(input_val)>8:
#                 flag = False
#                 print("Entered input is out of bounds. Please enter a valid input!!")
#                 break
#             else:
#                 flag =True
#                 final_input[i] = np.array(int(input_val))
#     return final_input #np.reshape(final_input,(3,3))
# inp = False
# while inp is False:
#     initial_node = Get_User_Input()
#     initial_node_mat = initial_node.copy()
#     inp = is_Node_Solvable(initial_node)

# Current_Node = initial_node.copy()
def Convert_mat_to_num(a,b,c,d,e,f,g,h,i):
    number= a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i
    return  number
Visited_Nodes_List = []
initial_node_list = initial_node.flatten()
num_initial = Convert_mat_to_num(initial_node_list[0],initial_node_list[1],initial_node_list[2],initial_node_list[3],initial_node_list[4],initial_node_list[5]
                          ,initial_node_list[6],initial_node_list[7],initial_node_list[8])
Visited_Nodes_List.append(num_initial)
Goal_Node = 123456780
Goal_Node_Mat= np.array([1,2,3,4,5,6,7,8,0])
Queue = []
Parent_Node = []
Child_Node = []
Parent_dict = {}
Child_dict = {}
test_child_dict = {}
FinalNodeList =[]
node_info = []
# print(len(initial_node[0]))
def Find_Blank_Space(node):
    # row,col = np.shape(node)
    # print(row)

    for i in range(len(node)):
        # for j in range (col):
        if node[i] == 0:
            return i
                # break


            # print(initial_node[i][j])
    #return i, j
# i,j = Find_Blank_Space(initial_node)
# print('i',i)
# print('j',j)
def swap (a, b):
    return b,a

def Move_Node_Up (Local_Current_Node,Queue,iter):
    Current_Node= Local_Current_Node.copy()
    Goal_Reached=False
    x = Local_Current_Node.flatten().copy()
    i = Find_Blank_Space(x)
    if i == 0 or i ==1 or i==2:
        return Current_Node,Goal_Reached
    else:
        print('Moving Up')
        # Local_Current_Node[i][j],Local_Current_Node[i-1][j] = swap(Local_Current_Node[i][j],Local_Current_Node[i-1][j])
        # print(Current_Node)

        x[i],x[i-3]= swap(x[i],x[i-3])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                  x[3], x[4], x[5]
                                  , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:

            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(x)
            Queue.append(x)
            Child_dict.update({iter: [x]})
            node_info.append(iter)
            temp_child_list.append(x)
        else:
            x[i],x[i-3]= swap(x[i],x[i-3])
            print('Node visited')
    return Current_Node,Goal_Reached#, Child_Node

def Move_Node_Down (Local_Current_Node,Queue,iter):
    Current_Node =Local_Current_Node.copy()
    Goal_Reached =False
    x = Local_Current_Node.flatten().copy()
    i= Find_Blank_Space(x)
    print("i",i)
    if i == 6 or i ==7 or i==8:
        return Current_Node,Goal_Reached
    else:
        print('Moving Down')
        # Local_Current_Node[i][j],Local_Current_Node[i+1][j] = swap(Local_Current_Node[i][j],Local_Current_Node[i+1][j])
        # num = Convert_mat_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
        #                           Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
        #                           , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        x = Local_Current_Node.flatten()
        x[i], x[i + 3] = swap(x[i], x[i + 3])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(x)
            Child_dict.update({iter: [x]})
            node_info.append(iter)
            temp_child_list.append(x)
            Queue.append(x)
        else:
            x[i], x[i + 3] = swap(x[i], x[i + 3])
            print('Node visited')
    return Current_Node, Goal_Reached#, Child_Node

def Move_Node_Left (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()
    Goal_Reached = False
    x = Local_Current_Node.flatten().copy()
    i = Find_Blank_Space(x)
    if i == 0 or i==3 or i==6:
        return Current_Node,Goal_Reached
    else:
        print('Moving Left')
        # Local_Current_Node[i][j],Local_Current_Node[i][j-1] = swap(Local_Current_Node[i][j],Local_Current_Node[i][j-1])
        # num = Convert_mat_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
        #                           Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
        #                           , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        # x = Local_Current_Node.flatten()
        x[i], x[i - 1] = swap(x[i], x[i - 1])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(x)
            temp_child_list.append(x)
            Child_dict.update({iter: [x]})
            node_info.append(iter)
            Queue.append(x)
        else:
            x[i], x[i - 1] = swap(x[i], x[i - 1])
            print('Node visited')
    return Current_Node, Goal_Reached#, Child_Node

def Move_Node_Right (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()

    Goal_Reached =False
    x = Local_Current_Node.flatten().copy()
    i = Find_Blank_Space(x)
    if i == 2 or i==5 or i==8:
        return Current_Node, Goal_Reached
    else:
        print('Moving right')
        # Local_Current_Node[i][j],Local_Current_Node[i][j+1] = swap(Local_Current_Node[i][j],Local_Current_Node[i][j+1])
        # num = Convert_mat_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
        #                           Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
        #                           , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        # x = Local_Current_Node.flatten()
        x[i], x[i + 1] = swap(x[i], x[i + 1])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num",num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(x)
            temp_child_list.append(x)
            Child_dict.update({iter: [x]})
            node_info.append(x)
            Queue.append(x)
        else:
            x[i], x[i + 1] = swap(x[i], x[i + 1])
            print('Node visited')
    return Current_Node,Goal_Reached#, Child_Node



# print (initial_node)

def is_Node_Visited(node):
    # print("Visited list",Visited_Nodes_List)
    # print("node:",node)
    for i in Visited_Nodes_List[::-1]:
        if node == i:
            print("################################################################")
            return True

    return False

def is_Goal_Reached(node):
    print("num:",node)
    print("Goal",Goal_Node)
    if node == Goal_Node:
        print("Goal Reached",node)
        return  True
    else:
        return False

def Update_Current_Node(Queue,iter):
    print("#####################")
    var= Queue.pop(0)
    Parent_dict.update({iter:var})
    Parent_Node.append(var)
    Current_Node = (var).copy()
    return Current_Node, Queue#, Parent_Node, Parent_dict
# for i in range(5):


# num = Convert_mat_to_num(initial_node[0][0],initial_node[0][1],initial_node[0][2],initial_node[1][0],initial_node[1][1],initial_node[1][2]
#                          ,initial_node[2][0],initial_node[2][1],initial_node[2][2])
# print(num)



print("start node",initial_node)
Queue.append(initial_node)
Updated_Current_Node = initial_node.copy()
start_time= time.time()
level =0
iter_child= 0
iter_parent= 0
while Queue:
    temp_child_list = []
    Updated_Current_Node,Queue = Update_Current_Node(Queue,iter_parent)
    print("Updated Current Node: ", Updated_Current_Node)


    Updated_Current_Node,Goal_Reached=Move_Node_Down(Updated_Current_Node,Queue,iter_parent)
    print("Current Node: ", Updated_Current_Node)
    # print("Queue", Queue)
    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node, Goal_Reached = Move_Node_Up(Updated_Current_Node, Queue,iter_parent)
    print("Current Node: ", Updated_Current_Node)
    # print("Queue", Queue)
    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node, Goal_Reached = Move_Node_Left(Updated_Current_Node, Queue,iter_parent)
    print("Current Node: ", Updated_Current_Node)
    # print("Queue",Queue)
    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node,Goal_Reached=Move_Node_Right(Updated_Current_Node,Queue,iter_parent)
    print("Current Node: ", Updated_Current_Node)
    # print("Queue", Queue)
    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break
    test_child_dict.update({iter_parent:temp_child_list})
    level = level + 1
    iter_parent = iter_parent +1
    print('@#$$$$$$$$$$$$$$$$$$$$$################$4@$@@$$@@$@$44@$@%@252level:',level)
    print('@#$$$$$$$$$$$$$$$$$$$$$################$4@$@@$$@@$@$44@$@%@252level:', iter_parent)
    # if iter_parent >=10000:
    #     break
# print('Child Node :', Child_Node)
# print('Parent Node:', Parent_Node)
# print('parent dict:',Parent_dict)
# print('child dict:',Child_dict)
# if os.path.exists("Parent_Node_info.txt"):
#     os.remove("Parent_Node_info.txt")
# f = open("Parent_Node_info.txt", "a")
# f.write(str(Parent_dict)+"\n")
# f.close()
# if os.path.exists("Child_Node_info.txt"):
#     os.remove("Child_Node_info.txt")
# f = open("Child_Node_info.txt", "a")
# f.write(str(Child_dict)+"\n")
# f.close()
# if os.path.exists("ttChild_Node_info.txt"):
#     os.remove("ttChild_Node_info.txt")
# f = open("ttChild_Node_info.txt", "a")
# f.write(str(test_child_dict)+"\n")
# f.close()


def Back_Tracking(Parent_dict,test_child_dict,FinalValue,InitialValue):
    updated_val= FinalValue
    while updated_val is not InitialValue :
        val_found = False
        for key,val in test_child_dict.items():
            # print("ALL_val",val)
            for v in val:
                if np.array_equal(updated_val,v):
                    parent_key= key
                    print('KEY:::',parent_key)
                    updated_val = Parent_dict[parent_key]
                    print("UPDATE_VAL:::",updated_val)
                    FinalNodeList.append(updated_val)
                    val_found= True
                    break
            if val_found is True:
                break
        print("UPDATE_VALue::::::::::::::::", updated_val)

        if np.array_equal(updated_val,initial_node_matrix):

            break

Back_Tracking(Parent_dict,test_child_dict,Goal_Node_Mat,initial_node_mat)
FinalNodeList.reverse()
FinalNodeList.append(Goal_Node_Mat)
# if os.path.exists("Path_Node_info.txt"):
#     os.remove("Path_Node_info.txt")
# f = open("Path_Node_info.txt", "a")
# f.write(str(FinalNodeList)+"\n")
# f.close()


print('final list:',FinalNodeList)

print("No of Steps :",len(FinalNodeList))

def Generate_Text_Files(FinalNodeList,test_child_dict,):
    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    f = open("nodePath.txt", "a")
    for i in FinalNodeList:
        for j in range(len(i.flatten())):
            x = (np.transpose(i)).flatten()
            f.write(str(int(x[j])) + " ")
        f.write("\n")
    f.close()

    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")
    f = open("Nodes.txt", "a")
    # for i in range (len(test_child_dict))
    for i in range(0,len(test_child_dict)):
        for val in test_child_dict.get(i):
            # print("val",val)
            for j in range(len(val.flatten())):
                x = (np.transpose(val)).flatten()
                f.write(str(x[j] )+ " ")
            f.write("\n")
    f.close()

    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")
    f = open("NodesInfo.txt", "a")
    # for i in range (len(test_child_dict))
    # for i in range(0,len(test_child_dict)):
    count= 0
    for val in test_child_dict.keys():
        # print("val",val+1)

        # for j in range(len(val.flatten())):
        # x = (np.transpose(val)).flatten()
        f.write(str(val+1 )+ " " + str(node_info[count]) +" " +str(0))
        count = count+1
        f.write("\n")
    f.close()
Generate_Text_Files(FinalNodeList,test_child_dict)
end_time = time.time()
total_time =  end_time -start_time
print('Total Time:',total_time)




    # print(Current_Node)
#
# Move_Node_Up(Current_Node)
# # Move_Node_Up()
# # cn=Move_Node_Left(cn)
# Move_Node_Left(Current_Node)
# # # Move_Node_Right()
# # cn=Move_Node_Down(cn)
# # cn=Move_Node_Right(cn)
