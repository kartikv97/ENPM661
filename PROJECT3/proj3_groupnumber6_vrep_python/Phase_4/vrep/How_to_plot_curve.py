import matplotlib.pyplot as plt
import numpy as np
import math

frame_count = 0

def save_fig(count):
    print("frame no:",count)
    if 0 <= count < 10:
        plt.savefig(r"./Node/0000000" + str(count) + ".png", bbox_inches='tight')
    if 10 <= count < 100:
        plt.savefig(r"./Node/000000" + str(count) + ".png", bbox_inches='tight')
    if 100 <= count < 1000:
        plt.savefig(r"./Node/00000" + str(count) + ".png", bbox_inches='tight')
    if 1000 <= count < 10000:
        plt.savefig(r"./Node/0000" + str(count) + ".png", bbox_inches='tight')
    if 10000 <= count < 100000:
        plt.savefig(r"./Node/000" + str(count) + ".png", bbox_inches='tight')
    if 100000 <= count < 1000000:
        plt.savefig(r"./Node/00" + str(count) + ".png", bbox_inches='tight')

def plot_curve(Xi, Yi, Thetai, UL, UR, color,linewidth,coord_list,label):
    global p6, frame_count
    # coord_list = []

    t = 0.0
    r = 0.038
    L = 0.3175
    dt = 0.1
    Xn = Xi
    Yn = Yi
    Thetan = np.deg2rad(Thetai)

    # Xi, Yi,Thetai: Input point's coordinates
    # Xs, Ys: Start point coordinates for plot function
    # Xn, Yn, Thetan: End point coordintes

    while t < 1:
        # print("t",t)
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5 * r * (UL + UR) * np.cos(Thetan) * dt
        Yn += 0.5 * r * (UL + UR) * np.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        p6 = plt.plot([Xs, Xn], [Ys, Yn], color=color, linewidth=linewidth, markersize=5, label= label)

    frame_count = frame_count +1

    # Uncomment the following line to generate video.
    # save_fig(frame_count)

    if color == 'blue':
        coord_list.append([Xn, Yn])

    Thetan = 180 * (Thetan) / np.pi

    return Xn, Yn, Thetan



coord_list =[]

def plot(parentlist, ang, act, actions,angleList, print_flag ):
    global action

    coord_list = []
    if print_flag == 'Explored':
        for action in range(len(act)):

            try:

                X1 = plot_curve(parentlist[action][0], parentlist[action][1], ang[action], act[action][0], act[action][1],
                                'black',0.2,coord_list, "Explored Node Path")  # (0,0,45) hypothetical start configuration
            except:
                break

    if print_flag == 'Optimal':

        actions.pop(0)
        actions.pop(-2)
        angleList.pop(0)

        coord_list =[]
        coord_list.append([-4, -4])

        frame_rate = 1
        for action in range(len(actions)):
            try:
                X2 = plot_curve(coord_list[action*frame_rate][0], coord_list[action*frame_rate][1], angleList[action*frame_rate], actions[action*frame_rate][0],
                            actions[action*frame_rate][1],'blue',0.5,coord_list, "Optimal Node Path")  # (0,0,45) hypothetical start configuration
            except:
                break




