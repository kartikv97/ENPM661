import matplotlib.pyplot as plt
import numpy as np

width  = 5
height = 5
clearance = input("Enter the Clearance required for the Rigid body:")

totalClearance = float(0.355) + float(clearance)
print("Total clearance( ---according to robot dimensions the default clearance is 0.355) :",totalClearance)

def get_Line_Equation(A,B,x,y):
    x1,y1 = A
    x2,y2 = B

    if y1==y2:
        line_equation = y - y2
        return line_equation
    if x1==x2:
        line_equation = x - x2
        return line_equation
    line_equation = (y-y2)-((x-x2)*(y1-y2))/(x1-x2)

    return line_equation


coords_square1 = np.array([(-3.25 , 0.75 ),
                          (-4.75 , 0.75 ),
                          (-4.75 , -0.75 ),
                          (-3.25 , -0.75 )])
coords_square2 = np.array([(3.25 , 0.75 ),
                          (4.75 , 0.75 ),
                          (4.75 , -0.75),
                          (3.25 , -0.75 )])
coords_square3 = np.array([(-2.75 , 3.75 ),
                          (-1.25 , 3.75 ),
                          (-1.25 , 2.25 ),
                          (-2.75 , 2.25 )])
# coord_inner_boundary = np.array([(5,5),
#                                (-5,5),
#                                (-5,-5),
#                                (5,-5)])
# coord_outer_boundary = np.array([(5.1,5.1),
#                                 (-5.1,5.1),
#                                 (-5.1,-5.1),
#                                 (5.1,-5.1)])
# coords_square1 = np.array([(-3.25 - totalClearance, 0.75 + totalClearance),
#                           (-4.75 + totalClearance, 0.75 + totalClearance),
#                           (-4.75 + totalClearance, -0.75 - totalClearance),
#                           (-3.25 - totalClearance, -0.75 - totalClearance)])
# coords_square2 = np.array([(3.25 - totalClearance, 0.75 + totalClearance),
#                           (4.75 + totalClearance, 0.75 + totalClearance),
#                           (4.75 + totalClearance, -0.75- totalClearance),
#                           (3.25 - totalClearance, -0.75 - totalClearance)])
# coords_square3 = np.array([(-2.75 - totalClearance, 3.75 + totalClearance),
#                           (-1.25 + totalClearance, 3.75 + totalClearance),
#                           (-1.25 + totalClearance, 2.25 - totalClearance),
#                           (-2.75 - totalClearance, 2.25 - totalClearance)])

"""
coords_square4 = np.array([(-5 , 5 ),
                          (-5 , -5 ),
                          (5  , 5),
                          (5 , -5 )])
coords_square5 = np.array([(-5.1 , 5.1 ),
                          (-5.1 , -5.1 ),
                          (5.1 , 5.1),
                          (5.1 ,-5.1 )])
                          """
coords_Circle1 = [(1), (0, 0)]
coords_Circle2 = [(1), (-2, -3)]
coords_Circle3 = [(1), (2, -3)]
coords_Circle4 = [(1), (2, 3)]

# coords_Circle1 = [(1+totalClearance), (0, 0)]
# coords_Circle2 = [(1+totalClearance), (-2, -3)]
# coords_Circle3 = [(1+totalClearance), (2, -3)]
# coords_Circle4 = [(1+totalClearance), (2, 3)]


def check_Obstacle(x,y):
    ################### circle 1######################
    if ((x - 0) ** 2 + (y - 0) ** 2 - (1+totalClearance) ** 2) <= 0:
        # print("obstacle found in circle 1")
        return True

    ################### circle 2 ########################
    if ((x - (-2)) ** 2 + (y - (-3)) ** 2 - (1+totalClearance) ** 2) <= 0:
        # print("obstacle found in circle 2")
        return True
    ################### circle 3 #######################
    if ((x - 2) ** 2 + (y - (-3)) ** 2 - (1+totalClearance) ** 2) <= 0:
        # print("obstacle found in circle 3")
        return True
    ##################### circle 4 ######################
    if ((x - 2) ** 2 + (y - 3) ** 2 - (1+totalClearance) ** 2) <= 0:
        # print("obstacle found in circle 4")
        return True
    ##################### square1##################
    if (y >= -0.75 - totalClearance) and (y <= 0.75 + totalClearance) and (x >= -4.75 - totalClearance) and (x <= -3.25 + totalClearance):
        # print("obstacle found in square 1")

        return True
    ##################### square2 ########################
    if (y >= -0.75 - totalClearance) and (y <= 0.75 + totalClearance) and (x >= 3.25 - totalClearance) and (
            x <= 4.75 + totalClearance):
        # print("obstacle found in square 2")

        return True

    ###################### square3 ############################
    if (y >= 2.25 - totalClearance) and (y <= 3.75 + totalClearance) and (x >= -2.75 - totalClearance) and (
            x <= -1.25 + totalClearance):
        # print("obstacle found in square 3")

        return True
    else:
        # print("obstacle not found")
        False

# fig = plt.figure()
# fig.set_dpi(100)
# fig.set_size_inches(5, 5)
# fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
# axis = fig.add_subplot(xlim=(-width, width), ylim=(-height, height))
# circle1 = plt.Circle((coords_Circle1[1]), coords_Circle1[0], fc=None)
# circle2 = plt.Circle((coords_Circle2[1]), coords_Circle2[0], fc=None)
# circle3 = plt.Circle((coords_Circle3[1]), coords_Circle3[0], fc=None)
# circle4 = plt.Circle((coords_Circle4[1]), coords_Circle4[0], fc=None)
# square1 = plt.Polygon(coords_square1)
# square2 = plt.Polygon(coords_square2)
# square3 = plt.Polygon(coords_square3)
# #square4 = plt.Polygon(coords_square4)
# #square5 = plt.Polygon(coords_square5)
# obstacles = [circle1, circle2, circle3, circle4, square1, square2, square3]
#
# for obstacle in obstacles:
#     plt.gca().add_patch(obstacle)
#
# plt.show()
# check_Obstacle(2,4)