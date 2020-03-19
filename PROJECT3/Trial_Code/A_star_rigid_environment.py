
import pygame
import pygame.gfxdraw
import math


pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

scale = 1
# Dimensions of the maze specified in the question.
width= 300
height = 200

# Take the radius and clearance inputs from the user.
radius = input("Enter the Radius of the Rigid body:")
clearance = input("Enter the Clearance required for the Rigid body:")
totalClearance = radius + clearance
totalClearance = int(totalClearance)

#Generate a PyGame window
gameDisplay = pygame.display.set_mode((width*scale,height*scale))
gameDisplay.fill(black)

# Draw the obstacles as specified in the maze.
pygame.draw.circle(gameDisplay, white, (225*scale, height-150*scale), (25+totalClearance)*scale)

pygame.draw.polygon(gameDisplay, white, ((20-totalClearance,height-120+totalClearance),(25-totalClearance,height-185-totalClearance),(75+totalClearance,height-185-totalClearance),(100+totalClearance,height-150-totalClearance),(75+totalClearance,height-120+totalClearance),(50,height-150+totalClearance)))

pygame.draw.polygon(gameDisplay, white, ((200-totalClearance,height-25),(225,height-40-totalClearance),(250+totalClearance,height-25),(225,height-10+totalClearance)))

pygame.draw.polygon(gameDisplay, white, ((95 - math.floor((75+totalClearance)*math.sqrt(3)/2),height-30 - math.floor((75+totalClearance)/2)),(95 - math.floor((75+totalClearance)*math.sqrt(3)/2) + math.floor((10+totalClearance)*math.sqrt(1)/2),height-30 - math.floor((75+totalClearance)/2) - math.floor((10+totalClearance)*math.sqrt(3)/2)),(95 + math.floor((10 + totalClearance)/2),height-30 - math.floor(10*math.sqrt(3)/2)),(95 - math.floor(totalClearance/2),height-30+math.floor(totalClearance*math.sqrt(3)/2))))

pygame.draw.ellipse(gameDisplay, white, (110-totalClearance,80 - totalClearance,80+ 2*totalClearance,40+ 2*totalClearance))


# Function to plot start and goal nodes
def draw_Start_and_Goal_Nodes(x,y):
    pygame.gfxdraw.pixel(gameDisplay,x,y,red)
    pygame.display.update()

# Function to plot the explored nodes
def draw_Explored_Nodes(x,y):
    pygame.gfxdraw.pixel(gameDisplay,x,y,green)
    pygame.display.update()

# Function to plot the final optimized path.
def draw_Optimal_Nodes(x, y):
    pygame.gfxdraw.pixel(gameDisplay, x, y, blue)
    pygame.display.update()

# Function to find the equation of the line between two points and substitute the "x" and "y" values.
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

# Function to check all the obstacle spaces.
def check_Obstacle(x,y):
    ########################  For circle  #############################
    if (x - 225) ** 2 + ( height-y- 150) ** 2 <= (25+totalClearance) ** 2:
        # print("Obstacle Detected in circle")
        return True
    #########################  For ellipse  #############################

    p = ((math.pow((x - 150), 2) / math.pow(40+totalClearance, 2)) +
         (math.pow(( height - y - 100), 2) / math.pow(20+totalClearance, 2)))

    if p<=1:
        # print("Obstacle Detected in ellipse")
        return True

    # Store the coordinates of all the obstacle figures in individual lists.
    parallelogram_coordinates = [(200-totalClearance,height-25),(225,height-(40+totalClearance)),(250+totalClearance,height-25),(225,height-(10-totalClearance))]

    rectangle_coordinates = [(95 - math.floor((75+totalClearance)*math.sqrt(3)/2),height-30 - math.floor((75+totalClearance)/2)),
                             (95 - math.floor((75+totalClearance)*math.sqrt(3)/2) + math.floor((10+totalClearance)*math.sqrt(1)/2),height-30 - math.floor((75+totalClearance)/2) - math.floor((10+totalClearance)*math.sqrt(3)/2)),
                             (95 + math.floor((10 + totalClearance)/2),height-30 - math.floor(10*math.sqrt(3)/2)),
                             (95 - math.floor(totalClearance/2),height-30+math.floor(totalClearance*math.sqrt(3)/2))]
    # Coordinates for the Polygon which is divided into 4 triangles.
    triangle_1_coordinates = [(20-totalClearance,height-120+totalClearance),(25-totalClearance,height-185-totalClearance), (50,height-150+totalClearance)]
    triangle_2_coordinates = [(25-totalClearance,height-185-totalClearance),(75+totalClearance,height-185-totalClearance), (50,height-150+totalClearance)]
    triangle_3_coordinates = [(75+totalClearance,height-185-totalClearance),(100+totalClearance,height-150-totalClearance), (50,height-150+totalClearance)]
    triangle_4_coordinates = [(100+totalClearance,height-150-totalClearance), (75+totalClearance,height-120+totalClearance),   (50,height-150+totalClearance)]


    #########################  For Polygon section 1  #############################
    half_plane_val_tri1= []
    for i in range(len(triangle_1_coordinates)):
        if i == len(triangle_1_coordinates)-1:
            half_plane_val_tri1.append(get_Line_Equation(triangle_1_coordinates[i], triangle_1_coordinates[0], x, y))
            break
        half_plane_val_tri1.append(get_Line_Equation(triangle_1_coordinates[i],triangle_1_coordinates[i+1],x,y))

    if (half_plane_val_tri1[0]>=0 and half_plane_val_tri1[1]>=0  and
        half_plane_val_tri1[2]<=0 ):
        # print("Obstacle Detected in triangle 1 of polygon.")
        return True

    #########################  For Polygon section 2  #############################
    half_plane_val_tri2 = []
    for i in range(len(triangle_2_coordinates)):
        if i == len(triangle_2_coordinates) - 1:
            half_plane_val_tri2.append(get_Line_Equation(triangle_2_coordinates[i], triangle_2_coordinates[0], x, y))
            break
        half_plane_val_tri2.append(get_Line_Equation(triangle_2_coordinates[i], triangle_2_coordinates[i + 1], x, y))

    if (half_plane_val_tri2[0] >= 0 and half_plane_val_tri2[1] <= 0 and
            half_plane_val_tri2[2] <= 0):
        # print("Obstacle Detected in triangle 2 of polygon.")
        return True

    #########################  For Polygon section 3  #############################
    half_plane_val_tri3 = []
    for i in range(len(triangle_3_coordinates)):
        if i == len(triangle_3_coordinates) - 1:
            half_plane_val_tri3.append(get_Line_Equation(triangle_3_coordinates[i], triangle_3_coordinates[0], x, y))
            break
        half_plane_val_tri3.append(get_Line_Equation(triangle_3_coordinates[i], triangle_3_coordinates[i + 1], x, y))

    if (half_plane_val_tri3[0] >= 0 and half_plane_val_tri3[1] <= 0 and
            half_plane_val_tri3[2] >= 0):
        # print("Obstacle Detected in triangle 3 of polygon.")
        return True

    #########################  For Polygon section 4  #############################
    half_plane_val_tri4 = []
    for i in range(len(triangle_4_coordinates)):
        if i == len(triangle_4_coordinates) - 1:
            half_plane_val_tri4.append(get_Line_Equation(triangle_4_coordinates[i], triangle_4_coordinates[0], x, y))
            break
        half_plane_val_tri4.append(get_Line_Equation(triangle_4_coordinates[i], triangle_4_coordinates[i + 1], x, y))

    if (half_plane_val_tri4[0] <= 0 and half_plane_val_tri4[1] <= 0 and
            half_plane_val_tri4[2] >= 0):
        # print("Obstacle Detected in triangle 4 of polygon.")
        return True

    #########################  For Parallelogram  #############################
    half_plane_val_parallelogram = []
    for i in range(len(parallelogram_coordinates)):
        if i == len(parallelogram_coordinates) - 1:
            half_plane_val_parallelogram.append(get_Line_Equation(parallelogram_coordinates[i], parallelogram_coordinates[0], x, y))
            break
        half_plane_val_parallelogram.append(get_Line_Equation(parallelogram_coordinates[i], parallelogram_coordinates[i + 1], x, y))
    if (half_plane_val_parallelogram[0] >= 0 and half_plane_val_parallelogram[1] >= 0 and
        half_plane_val_parallelogram[2] <= 0 and half_plane_val_parallelogram[3] <= 0 ):
        # print("Obstacle Detected in parallelogram")
        return True

    #########################  For Inclined Rectangle  #############################
    half_plane_val_rectangle = []
    for i in range(len(rectangle_coordinates)):
        if i == len(rectangle_coordinates) - 1:
            half_plane_val_rectangle.append(
                get_Line_Equation(rectangle_coordinates[i], rectangle_coordinates[0], x, y))
            break
        half_plane_val_rectangle.append(
            get_Line_Equation(rectangle_coordinates[i], rectangle_coordinates[i + 1], x, y))
    if (half_plane_val_rectangle[0] >= 0 and half_plane_val_rectangle[1] >= 0 and
            half_plane_val_rectangle[2] <= 0 and half_plane_val_rectangle[3] <= 0):
        # print("Obstacle Detected in rectangle")
        return True
    else:
        # print("No Obstacle Detected")
        return False



