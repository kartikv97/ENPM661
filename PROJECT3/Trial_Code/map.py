import matplotlib.pyplot as plt
import numpy as np

width  = 5
height = 5
clearance = input("Enter the Clearance required for the Rigid body:")
totalClearance = clearance
totalClearance = int(totalClearance)

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


coords_square1 = np.array([(-3.25 - totalClearance, 0.75 + totalClearance),
                          (-4.75 + totalClearance, 0.75 + totalClearance),
                          (-4.75 + totalClearance, -0.75 - totalClearance),
                          (-3.25 - totalClearance, -0.75 - totalClearance)])
coords_square2 = np.array([(3.25 - totalClearance, 0.75 + totalClearance),
                          (4.75 + totalClearance, 0.75 + totalClearance),
                          (4.75 + totalClearance, -0.75- totalClearance),
                          (3.25 - totalClearance, -0.75 - totalClearance)])
coords_square3 = np.array([(-2.75 - totalClearance, 3.75 + totalClearance),
                          (-1.25 + totalClearance, 3.75 + totalClearance),
                          (-1.25 + totalClearance, 2.25 - totalClearance),
                          (-2.75 - totalClearance, 2.25 - totalClearance)])
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
coords_Circle1 = [(1+totalClearance), (0, 0)]
coords_Circle2 = [(1+totalClearance), (-2, -3)]
coords_Circle3 = [(1+totalClearance), (2, -3)]
coords_Circle4 = [(1+totalClearance), (2, 3)]

def check_obstacle(x,y):
    ################### circle 1######################
    if ((x - 0) ** 2 + (y - 0) ** 2 - (1+totalClearance) ** 2) <= 0:
        print("obstacle found")
        return True

    ################### circle 2 ########################
    if ((x - (-2)) ** 2 + (y - (-3)) ** 2 - (1+totalClearance) ** 2) <= 0:
        print("obstacle found")
        return True
    ################### circle 3 #######################
    if ((x - 2) ** 2 + (y - (-3)) ** 2 - (1+totalClearance) ** 2) <= 0:
        print("obstacle found")
        return True
    ##################### circle 4 ######################
    if ((x - 2) ** 2 + (y - 3) ** 2 - (1+totalClearance) ** 2) <= 0:
        print("obstacle found")
        return True
    ##################### square1##################
    Square1 = []
    for i in range(len(coords_square1)):
        if i == len(coords_square1) - 1:
            Square1.append(get_Line_Equation(coords_square1[i], coords_square1[0], x, y))
            break
        Square1.append(get_Line_Equation(coords_square1[i], coords_square1[i + 1], x, y))
    if (Square1[0] <= 0 and Square1[1] <= 0 and Square1[2] >= 0 and Square1[3] >= 0):
        print("obstacle found")
        return True
    ##################### square2 ########################
    Square2 = []
    for i in range(len(coords_square2)):
        if i == len(coords_square2) - 1:
            Square2.append(get_Line_Equation(coords_square2[i], coords_square2[0], x, y))
            break
        Square2.append(get_Line_Equation(coords_square2[i], coords_square2[i + 1], x, y))
    if (Square2[0] <= 0 and Square2[1] <= 0 and Square2[2] >= 0 and Square2[3] >= 0):
        print("obstacle found")
        return True

    ###################### square3 ############################
    Square3 = []
    for i in range(len(coords_square3)):
        if i == len(coords_square3) - 1:
            Square3.append(get_Line_Equation(coords_square3[i], coords_square3[0], x, y))
            break
        Square3.append(get_Line_Equation(coords_square3[i], coords_square3[i + 1], x, y))
    if (Square3[0] <= 0 and Square3[1] <= 0 and Square3[2] >= 0 and Square3[3] >= 0):
        print("obstacle found")
        return True
    else:
        print("obstacle not found")
        False

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(5, 5)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
axis = fig.add_subplot(xlim=(-width, width), ylim=(-height, height))
circle1 = plt.Circle((coords_Circle1[1]), coords_Circle1[0], fc=None)
circle2 = plt.Circle((coords_Circle2[1]), coords_Circle2[0], fc=None)
circle3 = plt.Circle((coords_Circle3[1]), coords_Circle3[0], fc=None)
circle4 = plt.Circle((coords_Circle4[1]), coords_Circle4[0], fc=None)
square1 = plt.Polygon(coords_square1)
square2 = plt.Polygon(coords_square2)
square3 = plt.Polygon(coords_square3)
#square4 = plt.Polygon(coords_square4)
#square5 = plt.Polygon(coords_square5)
obstacles = [circle1, circle2, circle3, circle4, square1, square2, square3]

for obstacle in obstacles:
    plt.gca().add_patch(obstacle)

plt.show()
#check_obstacle(-2.75,3.5)
