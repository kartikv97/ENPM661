import numpy as np
import time
import os

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
                final_input[i] = int(np.array((input_val)))

    return final_input
########################################################################################################################
inp = False
while inp is False:
    initial_node = Get_User_Input().astype(int)
    initial_node_mat = initial_node.copy()
    inp = is_Node_Solvable(initial_node)
########################################################################################################################

def Convert_mat_to_num(a,b,c,d,e,f,g,h,i):
    number= a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i
    return  number
Visited_Nodes_List = []
initial_node_list = initial_node.copy()
num_initial = Convert_mat_to_num(initial_node_list[0],initial_node_list[1],initial_node_list[2]
                                 ,initial_node_list[3],initial_node_list[4],initial_node_list[5]
                                 ,initial_node_list[6],initial_node_list[7],initial_node_list[8])
Visited_Nodes_List.append(num_initial)
Goal_Node = 123456780
initial_node_matrix = initial_node.copy()
Goal_Node_Mat= [1,2,3,4,5,6,7,8,0]
Queue = []
Parent_dict = {}
test_child_dict = {}
FinalNodeList =[]
node_info = []
test_child_dict.update({0:[initial_node_list]})
########################################################################################################################
def Find_Blank_Space(node):
      for i in range(len(node)):
          if node[i] == 0:
              return i
########################################################################################################################
def swap (a, b):
    return b,a
########################################################################################################################
def Move_Node_Up (Local_Current_Node,Queue,iter):
    Current_Node= Local_Current_Node.copy()
    Goal_Reached=False
    x = Local_Current_Node.flatten().copy()
    i = Find_Blank_Space(x)
    if i == 0 or i ==1 or i==2:
        return Current_Node,Goal_Reached
    else:
        print('Moving Up')

        x[i],x[i-3]= swap(x[i],x[i-3])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                  x[3], x[4], x[5]
                                  , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:

            Visited_Nodes_List.append(num)

            if is_Goal_Reached(num)== True:

                Goal_Reached = True
            Queue.append(x)
            node_info.append(iter)
            temp_child_list.append(x)
        else:
            x[i],x[i-3]= swap(x[i],x[i-3])

    return Current_Node,Goal_Reached
########################################################################################################################
def Move_Node_Down (Local_Current_Node,Queue,iter):
    Current_Node =Local_Current_Node.copy()
    Goal_Reached =False
    x = Local_Current_Node.copy()
    i= Find_Blank_Space(x)

    if i == 6 or i ==7 or i==8:
        return Current_Node,Goal_Reached
    else:
        print('Moving Down')

        x[i], x[i + 3] = swap(x[i], x[i + 3])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)

            if is_Goal_Reached(num)== True:

                Goal_Reached = True

            node_info.append(iter)
            temp_child_list.append(x)
            Queue.append(x)
        else:
            x[i], x[i + 3] = swap(x[i], x[i + 3])

    return Current_Node, Goal_Reached
########################################################################################################################
def Move_Node_Left (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()
    Goal_Reached = False
    x = Local_Current_Node.copy()
    i = Find_Blank_Space(x)
    if i == 0 or i==3 or i==6:
        return Current_Node,Goal_Reached
    else:
        print('Moving Left')
        x[i], x[i - 1] = swap(x[i], x[i - 1])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 , x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)

            if is_Goal_Reached(num)== True:

                Goal_Reached = True

            temp_child_list.append(x)

            node_info.append(iter)
            Queue.append(x)
        else:
            x[i], x[i - 1] = swap(x[i], x[i - 1])

    return Current_Node, Goal_Reached
########################################################################################################################
def Move_Node_Right (Local_Current_Node,Queue,iter):
    Current_Node = Local_Current_Node.copy()
    Goal_Reached =False
    x = Local_Current_Node.copy()
    i = Find_Blank_Space(x)
    if i == 2 or i==5 or i==8:
        return Current_Node, Goal_Reached
    else:
        print('Moving right')
        x[i], x[i + 1] = swap(x[i], x[i + 1])
        num = Convert_mat_to_num(x[0], x[1], x[2],
                                 x[3], x[4], x[5]
                                 ,x[6], x[7], x[8])
        if is_Node_Visited(num) == False:
            Visited_Nodes_List.append(num)

            if is_Goal_Reached(num)== True:

                Goal_Reached = True

            temp_child_list.append(x)

            node_info.append(iter)
            Queue.append(x)
        else:
            x[i], x[i + 1] = swap(x[i], x[i + 1])

    return Current_Node,Goal_Reached
########################################################################################################################
def is_Node_Visited(node):

    for i in Visited_Nodes_List[::-1]:
        if node == i:

            return True
    return False
########################################################################################################################
def is_Goal_Reached(node):
    if node == Goal_Node:
        print("Goal Reached",node)
        return  True
    else:
        return False
########################################################################################################################
def Update_Current_Node(Queue,iter):

    var= Queue.pop(0)
    Parent_dict.update({iter:var})

    Current_Node = (var).copy()
    return Current_Node, Queue
########################################################################################################################
print("start node",initial_node)
Queue.append(initial_node)
Updated_Current_Node = initial_node.copy()
start_time= time.time()
level =0
iter_child= 0
iter_parent= 1
while Queue:
    temp_child_list = []
    Updated_Current_Node,Queue = Update_Current_Node(Queue,iter_parent)



    Updated_Current_Node,Goal_Reached=Move_Node_Down(Updated_Current_Node,Queue,iter_parent)


    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node, Goal_Reached = Move_Node_Up(Updated_Current_Node, Queue,iter_parent)


    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node, Goal_Reached = Move_Node_Left(Updated_Current_Node, Queue,iter_parent)


    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    Updated_Current_Node,Goal_Reached=Move_Node_Right(Updated_Current_Node,Queue,iter_parent)


    if Goal_Reached == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break
    test_child_dict.update({iter_parent:temp_child_list})
    level = level + 1
    iter_parent = iter_parent +1

    print('#######################################  Node:', iter_parent)
########################################################################################################################
def Generate_Text_Files(FinalNodeList, test_child_dict, ):

    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    f = open("nodePath.txt", "a")
    for i in FinalNodeList:
        i = np.array(i).reshape((3, 3))
        for j in range(len(i.flatten())):

            x = (np.transpose(i).flatten())
            f.write(str((x[j])) + " ")
        f.write("\n")
    f.close()

    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")
    f = open("Nodes.txt", "a")

    for i in range(len(test_child_dict)):

        for val in test_child_dict.get(i):

            val = np.array(val).reshape(3, 3)
            for j in range(len(val.flatten())):

                x = (np.transpose(val)).flatten().astype(int)
                f.write(str(int(x[j])) + " ")
            f.write("\n")
    f.close()

    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")
    f = open("NodesInfo.txt", "a")
    count = 0
    for val in test_child_dict.keys():
        f.write(str(val ) + " " + str(node_info[count]) + " " + str(0))
        count = count + 1
        f.write("\n")
    f.close()
    return None
########################################################################################################################
def Back_Tracking(Parent_dict,test_child_dict,FinalValue,InitialValue):
    updated_val= FinalValue
    while updated_val is not InitialValue :
        val_found = False
        for key,val in test_child_dict.items():

            for v in val:
                if np.array_equal(updated_val,v):
                    parent_key= key

                    updated_val = Parent_dict[parent_key]

                    FinalNodeList.append(updated_val)
                    val_found= True
                    break
            if val_found is True:
                break


        if np.array_equal(updated_val,initial_node_matrix):

            break
########################################################################################################################
print("############################   Backtracking ...   ###################################")
Back_Tracking(Parent_dict,test_child_dict,Goal_Node_Mat,initial_node_mat)

FinalNodeList.reverse()
FinalNodeList.append(Goal_Node_Mat)


print("No of Steps :",len(FinalNodeList))

Generate_Text_Files(FinalNodeList,test_child_dict)
end_time = time.time()
total_time =  end_time -start_time

print('Total Time:',total_time)
