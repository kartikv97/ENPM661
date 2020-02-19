
import numpy as np


initial_node = np.array([[1,2,3],[4,6,5],[8,7,0]])
Visited_Nodes_List = []
Visited_Nodes_List.append(initial_node)
# print(len(initial_node[0]))
def Find_Blank_Space(current_node):
    row,col = np.shape(current_node)
    # print(row)
    for i in range(row):
        for j in range (col):
            if initial_node[i][j] == 0:
                return i, j
                break
            # print(initial_node[i][j])
    #return i, j
# i,j = Find_Blank_Space(initial_node)
# print('i',i)
# print('j',j)
def swap (a, b):
    return b,a

def Move_Node_Up ():
    i, j = Find_Blank_Space(initial_node)
    if i == 0:
        return None
    else:
        initial_node[i][j],initial_node[i-1][j] = swap(initial_node[i][j],initial_node[i-1][j])
        Visited_Nodes_List.append([initial_node])
        print(initial_node)
    return initial_node

def Move_Node_Down ():
    i, j = Find_Blank_Space(initial_node)
    if i == 2:
        return None
    else:
        initial_node[i][j],initial_node[i+1][j] = swap(initial_node[i][j],initial_node[i+1][j])
        Visited_Nodes_List.append([initial_node])
        print(initial_node)
    return initial_node

def Move_Node_Left ():
    i, j = Find_Blank_Space(initial_node)
    if j == 0:
        return None
    else:
        initial_node[i][j],initial_node[i][j-1] = swap(initial_node[i][j],initial_node[i][j-1])
        if is_Node_Visited(initial_node) == False:
            Visited_Nodes_List.append([initial_node])
            print(initial_node)
        else:
            print('Node visited')
    return initial_node

def Move_Node_Right ():
    i, j = Find_Blank_Space(initial_node)
    if j == 2:
        return None
    else:
        initial_node[i][j],initial_node[i][j+1] = swap(initial_node[i][j],initial_node[i][j+1])
        Visited_Nodes_List.append([initial_node])
        print(initial_node)
    return initial_node



# print (initial_node)

def is_Node_Visited(node):
    for i in range (len(Visited_Nodes_List)):
        if np.array_equal(node,Visited_Nodes_List[i]):
            return True
        else :
            return False


# for i in range(5):
print("start node",initial_node)
Move_Node_Up()
Move_Node_Up()
Move_Node_Up()
Move_Node_Left()
Move_Node_Left()
Move_Node_Right()
