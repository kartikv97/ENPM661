
import numpy as np


initial_node = np.array([[1,2,3],[4,6,5],[8,7,0]])
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
i,j = Find_Blank_Space(initial_node)
# print('i',i)
# print('j',j)
def swap (a, b):
    return b,a

def Move_Node_Up (i,j):
    if i == 0:
        return None
    else:
        initial_node[i][j],initial_node[i-1][j] = swap(initial_node[i][j],initial_node[i-1][j])
    return initial_node

def Move_Node_Down (i,j):
    if i == 2:
        return None
    else:
        initial_node[i][j],initial_node[i+1][j] = swap(initial_node[i][j],initial_node[i+1][j])
    return initial_node

def Move_Node_Left (i,j):
    if j == 0:
        return None
    else:
        initial_node[i][j],initial_node[i][j-1] = swap(initial_node[i][j],initial_node[i][j-1])
    return initial_node

def Move_Node_Right (i,j):
    if i == 0:
        return None
    else:
        initial_node[i][j],initial_node[i-1][j] = swap(initial_node[i][j],initial_node[i-1][j])
    return initial_node
Move_Node_Up(i,j)
print (initial_node)

