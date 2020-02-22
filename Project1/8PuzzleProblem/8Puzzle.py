
import numpy as np
import time
import os

# initial_node = np.array( [[1, 3, 0],
#        [5, 2, 6],
#        [4, 7, 8]])
# initial_node_mat= np.array([[1, 3, 0],
#        [5, 2, 6],
#        [4, 7, 8]])


# initial_node = np.array([[1,2,3],[5,4,6],[8,7,0]])
# initial_node_mat = np.array([[1,2,3],[5,4,6],[8,7,0]])

# initial_node = np.array([[7,2,3],[1,0,6],[5,8,4]])
# initial_node_mat = np.array([[7,2,3],[1,0,6],[5,8,4]])

def Get_User_Input():
    print("Enter the values of input node in the range [0-8] without repetition :\n")
    flag = False
    final_input = np.zeros(9)
    while flag is False:
        for i in range (9):
            input_val = (input("Enter number " + str(i+1) +" : "))
            if len(input_val) is 0:
                print("You need to enter a value in range [0-8]. Don't leave a number blank!!!")
                flag = False
                break
            if int(input_val)<0 or int(input_val)>8:
                flag = False
                print("Entered input is out of bounds. Please enter a valid input!!")
                break


            else:
                flag =True
                final_input[i] = np.array(int(input_val))
    return np.reshape(final_input,(3,3))


initial_node = Get_User_Input()
initial_node_mat = initial_node.copy()
# Current_Node = initial_node.copy()
def Convert_int_to_num(a,b,c,d,e,f,g,h,i):
    number= a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i
    return  number
Visited_Nodes_List = []
num_initial = Convert_int_to_num(initial_node[0][0],initial_node[0][1],initial_node[0][2],initial_node[1][0],initial_node[1][1],initial_node[1][2]
                          ,initial_node[2][0],initial_node[2][1],initial_node[2][2])
Visited_Nodes_List.append(num_initial)
Goal_Node = 123456780
Goal_Node_Mat= np.array([[1,2,3],[4,5,6],[7,8,0]])
Queue = []
Parent_Node = []
Child_Node = []
Parent_dict = {}
Child_dict = {}
test_child_dict = {}
FinalNodeList =[]
# print(len(initial_node[0]))
def Find_Blank_Space(node):
    row,col = np.shape(node)
    # print(row)
    for i in range(row):
        for j in range (col):
            if node[i][j] == 0:
                return i, j
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
    i, j = Find_Blank_Space(Local_Current_Node)
    if i == 0:
        return Current_Node,Goal_Reached
    else:
        print('Moving Up')
        Local_Current_Node[i][j],Local_Current_Node[i-1][j] = swap(Local_Current_Node[i][j],Local_Current_Node[i-1][j])
        # print(Current_Node)
        num = Convert_int_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
                                  Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
                                  , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        if is_Node_Visited(num) == False:

            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(Local_Current_Node)
            Queue.append(Local_Current_Node)
            Child_dict.update({iter: [Local_Current_Node]})
            temp_child_list.append(Local_Current_Node)
        else:
            Local_Current_Node[i][j], Local_Current_Node[i - 1][j] = swap(Local_Current_Node[i][j], Local_Current_Node[i - 1][j])
            print('Node visited')
    return Current_Node,Goal_Reached#, Child_Node

def Move_Node_Down (Local_Current_Node,Queue,iter):
    Current_Node =Local_Current_Node.copy()
    Goal_Reached =False
    i, j = Find_Blank_Space(Local_Current_Node)
    if i == 2:
        return Current_Node,Goal_Reached
    else:
        print('Moving Down')
        Local_Current_Node[i][j],Local_Current_Node[i+1][j] = swap(Local_Current_Node[i][j],Local_Current_Node[i+1][j])
        num = Convert_int_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
                                  Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
                                  , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(Local_Current_Node)
            Child_dict.update({iter: [Local_Current_Node]})
            temp_child_list.append(Local_Current_Node)
            Queue.append(Local_Current_Node)
        else:
            Local_Current_Node[i][j], Local_Current_Node[i + 1][j] = swap(Local_Current_Node[i][j], Local_Current_Node[i + 1][j])
            print('Node visited')
    return Current_Node, Goal_Reached#, Child_Node

def Move_Node_Left (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()
    Goal_Reached = False
    i, j = Find_Blank_Space(Local_Current_Node)
    if j == 0:
        return Current_Node,Goal_Reached
    else:
        print('Moving Left')
        Local_Current_Node[i][j],Local_Current_Node[i][j-1] = swap(Local_Current_Node[i][j],Local_Current_Node[i][j-1])
        num = Convert_int_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
                                  Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
                                  , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num", num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(Local_Current_Node)
            temp_child_list.append(Local_Current_Node)
            Child_dict.update({iter: [Local_Current_Node]})
            Queue.append(Local_Current_Node)
        else:
            Local_Current_Node[i][j], Local_Current_Node[i][j - 1] = swap(Local_Current_Node[i][j], Local_Current_Node[i][j - 1])
            print('Node visited')
    return Current_Node, Goal_Reached#, Child_Node

def Move_Node_Right (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()
    Goal_Reached =False
    i, j = Find_Blank_Space(Local_Current_Node)
    if j == 2:
        return Current_Node, Goal_Reached
    else:
        print('Moving right')
        Local_Current_Node[i][j],Local_Current_Node[i][j+1] = swap(Local_Current_Node[i][j],Local_Current_Node[i][j+1])
        num = Convert_int_to_num(Local_Current_Node[0][0], Local_Current_Node[0][1], Local_Current_Node[0][2],
                                  Local_Current_Node[1][0], Local_Current_Node[1][1], Local_Current_Node[1][2]
                                  , Local_Current_Node[2][0], Local_Current_Node[2][1], Local_Current_Node[2][2])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)
            print(Local_Current_Node)
            print("num",num)
            if is_Goal_Reached(num)== True:
                print("****########$$$$$$$$$$$$$***********######################")
                Goal_Reached = True
            Child_Node.append(Local_Current_Node)
            temp_child_list.append(Local_Current_Node)
            Child_dict.update({iter: [Local_Current_Node]})
            Queue.append(Local_Current_Node)
        else:
            Local_Current_Node[i][j], Local_Current_Node[i][j + 1] = swap(Local_Current_Node[i][j], Local_Current_Node[i][j + 1])
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


# num = Convert_int_to_num(initial_node[0][0],initial_node[0][1],initial_node[0][2],initial_node[1][0],initial_node[1][1],initial_node[1][2]
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
    # print("Updated Current Node: ", Updated_Current_Node)


    Updated_Current_Node,Goal_Reached=Move_Node_Down(Updated_Current_Node,Queue,iter_parent)
    # print("Current Node: ", Updated_Current_Node)
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
    # print("Current Node: ", Updated_Current_Node)
    # print("Queue",Queue)
    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node,Goal_Reached=Move_Node_Right(Updated_Current_Node,Queue,iter_parent)
    # print("Current Node: ", Updated_Current_Node)
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
print('Child Node :', Child_Node)
print('Parent Node:', Parent_Node)
print('parent dict:',Parent_dict)
print('child dict:',Child_dict)
if os.path.exists("Parent_Node_info.txt"):
    os.remove("Parent_Node_info.txt")
f = open("Parent_Node_info.txt", "a")
f.write(str(Parent_dict)+"\n")
f.close()
if os.path.exists("Child_Node_info.txt"):
    os.remove("Child_Node_info.txt")
f = open("Child_Node_info.txt", "a")
f.write(str(Child_dict)+"\n")
f.close()
if os.path.exists("ttChild_Node_info.txt"):
    os.remove("ttChild_Node_info.txt")
f = open("ttChild_Node_info.txt", "a")
f.write(str(test_child_dict)+"\n")
f.close()


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
        if np.array_equal(updated_val,initial_node_mat):
            break

Back_Tracking(Parent_dict,test_child_dict,Goal_Node_Mat,initial_node_mat)
print("No of Steps :",len(FinalNodeList)-1)
if os.path.exists("Final_Node_info.txt"):
    os.remove("Final_Node_info.txt")
f = open("Final_Node_info.txt", "a")
f.write(str(FinalNodeList)+"\n")
f.close()

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
