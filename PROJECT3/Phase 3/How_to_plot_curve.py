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
    # save_fig(frame_count)
    # print([Xn, Yn])
    if color == 'blue':
        coord_list.append([Xn, Yn])

    Thetan = 180 * (Thetan) / np.pi
    # print("Theta",Thetan)
    return Xn, Yn, Thetan#, coord_list



coord_list =[]

def plot(parentlist, ang, act, actions,angleList, print_flag ):
    global action
    # fig, ax = plt.subplots()



    # actions=[(10, 0), (10, 0), (10, 0), (10, 0), (10, 10), (10, 0), (10, 10), (10, 0), (10, 0)]
    # angleList = [60, 128.5744762676261, 60.0, 128.5744762676261, 60.0, 60.0, 128.5744762676261, 128.5744762676261, 60.0]
    #
    # ang = [60, 60, 60, 128.5744762676261, 128.5744762676261,
    #        60.0, 60.0, 60.0, 60.0, 128.5744762676261, 60.0,
    #        128.5744762676261, 128.5744762676261, 128.5744762676261,
    #        60.0, 60.0, 128.5744762676261, 60.0, 60.0, 128.5744762676261,
    #        128.5744762676261, 128.5744762676261, 60.0, 128.5744762676261, 60.0,
    #        128.5744762676261, 128.5744762676261, 60.0, 60.0, 128.5744762676261, 60.0,
    #        128.5744762676261, 60.0, 60.0, 60.0, 128.5744762676261, 128.5744762676261,
    #        128.5744762676261, 128.5744762676261, 60.0, 128.5744762676261, 60.0,
    #        351.4255237323739, 351.4255237323739, 128.5744762676261, 128.5744762676261,
    #        128.5744762676261, 60.0, 60.0, 60.0, 60.0, 60.0, 128.5744762676261, 60.0, 60.0,
    #        60.0, 60.0, 197.1489525352522, 197.1489525352522, 60.0, 128.5744762676261,
    #        351.4255237323739, 351.4255237323739, 128.5744762676261, 128.5744762676261,
    #        128.5744762676261, 128.5744762676261, 60.0, 128.5744762676261, 128.5744762676261,
    #        128.5744762676261, 60.0, 128.5744762676261]
    # act = [(10, 0), (0, 10), (10, 10), (10, 0), (0, 10), (10, 0), (0, 10), (10, 0), (0, 10),
    #        (10, 10), (10, 10), (0, 10), (10, 0), (0, 10), (10, 10), (10, 0), (10, 10), (10, 0),
    #        (0, 10), (10, 0), (0, 10), (10, 10), (10, 0), (0, 10), (10, 10), (10, 0), (0, 10),
    #        (10, 0), (0, 10), (10, 10), (10, 0), (0, 10), (10, 10), (10, 0), (0, 10), (10, 10),
    #        (10, 0), (0, 10), (0, 10), (10, 10), (10, 10), (10, 0), (10, 0), (0, 10), (10, 0),
    #        (0, 10), (10, 10), (10, 0), (10, 10), (10, 0), (0, 10), (10, 10), (0, 10), (10, 0),
    #        (0, 10), (10, 0), (0, 10), (10, 0), (0, 10), (10, 10), (0, 10), (10, 0), (0, 10),
    #        (0, 10), (10, 0), (0, 10), (10, 10), (10, 0), (10, 0), (0, 10), (10, 10), (10, 0), (10, 0)]
    #
    #
    # parentlist = [(-4, -4), (-4, -4), (-4, -4), (-3.905, -3.8354551732809568),
    #               (-3.905, -3.8354551732809568), (-4.0234709637993085, -3.6869134931488707), (-4.0234709637993085, -3.6869134931488707),
    #               (-3.81, -3.6709103465619135), (-3.81, -3.6709103465619135), (-3.905, -3.8354551732809568), (-4.0234709637993085, -3.6869134931488707),
    #               (-3.715, -3.5063655198428703), (-3.9284709637993083, -3.5223686664298275), (-3.9284709637993083, -3.5223686664298275),
    #               (-3.81, -3.6709103465619135), (-4.046941927598617, -3.3738269862977415), (-3.715, -3.5063655198428703), (-3.8334709637993085, -3.3578238397107842),
    #               (-3.8334709637993085, -3.3578238397107842), (-4.141941927598618, -3.538371813016785), (-4.141941927598618, -3.538371813016785),
    #               (-3.9284709637993083, -3.5223686664298275), (-4.260412891397927, -3.3898301328846996), (-3.7384709637993083, -3.193279012991741),
    #               (-4.046941927598617, -3.3738269862977415), (-3.951941927598617, -3.2092821595786987), (-3.951941927598617, -3.2092821595786987),
    #               (-3.62, -3.341820693123827), (-3.62, -3.341820693123827), (-3.7384709637993083, -3.193279012991741), (-4.070412891397925, -3.060740479446613),
    #               (-3.525, -3.1772758664047838), (-3.8334709637993085, -3.3578238397107842), (-3.856941927598617, -3.044737332859655), (-3.856941927598617, -3.044737332859655),
    #               (-4.141941927598618, -3.538371813016785), (-4.165412891397926, -3.225285306165656), (-4.165412891397926, -3.225285306165656),
    #               (-3.761941927598617, -2.8801925061406117), (-4.070412891397925, -3.060740479446613), (-3.951941927598617, -3.2092821595786987),
    #               (-4.283883855197235, -3.0767436260335703), (-3.905, -3.8354551732809568), (-3.905, -3.8354551732809568), (-3.9754128913979256, -2.8961956527275694),
    #               (-3.9754128913979256, -2.8961956527275694), (-3.761941927598617, -2.8801925061406117), (-4.093883855197234, -2.747653972595484), (-3.62, -3.341820693123827),
    #               (-3.6434709637993086, -3.0287341862726977), (-3.6434709637993086, -3.0287341862726977), (-3.856941927598617, -3.044737332859655), (-3.5484709637993084, -2.8641893595536545),
    #               (-3.7171236495851367, -3.8637831974759416), (-3.7171236495851367, -3.8637831974759416), (-3.8804128913979254, -2.7316508260085266), (-3.8804128913979254, -2.7316508260085266),
    #               (-4.0234709637993085, -3.6869134931488707), (-4.0234709637993085, -3.6869134931488707), (-4.093883855197234, -2.747653972595484), (-3.7854128913979253, -2.5671059992894834),
    #               (-3.9284709637993083, -3.5223686664298275),
    #               (-3.9284709637993083, -3.5223686664298275), (-3.6221236495851366, -3.6992383707568983),
    #               (-4.378883855197235, -3.2412884527526136), (-4.378883855197235, -3.2412884527526136), (-4.165412891397926, -3.225285306165656),
    #               (-4.497354818996543, -3.0927467726205276), (-4.1888838551972345, -2.912198799314527), (-4.1888838551972345, -2.912198799314527), (-3.9754128913979256, -2.8961956527275694),
    #               (-4.307354818996544, -2.763657119182441), (-3.998883855197234, -2.58310914587644)]
    #
    # coord_list.append([-4,-4])


    coord_list = []
    if print_flag == 'Explored':
        for action in range(len(act)):
            # action= 2
            try:

                X1 = plot_curve(parentlist[action][0], parentlist[action][1], ang[action], act[action][0], act[action][1],
                                'black',0.2,coord_list, "Explored Node Path")  # (0,0,45) hypothetical start configuration
            except:
                break

    # nodepath = [(-4, -4), (-3.905, -3.8354551732809568), (-4.0234709637993085, -3.6869134931488707), (-3.9284709637993083, -3.5223686664298275), (-4.046941927598617, -3.3738269862977415), (-3.856941927598617, -3.044737332859655), (-3.761941927598617, -2.8801925061406117), (-3.998883855197234, -2.58310914587644), (-4.117354818996542, -2.4345674657443546), (-3.9273548189965424, -2.105477812306268)]

    # action= 0
    if print_flag == 'Optimal':

        actions.pop(0)
        actions.pop(-2)
        angleList.pop(0)
        # angleList.pop(-1)
        # angleList.append(60)
        coord_list =[]
        coord_list.append([-4, -4])
        # print("actions:",actions)
        # print("ang:",angleList)
        #
        # try:
        frame_rate = 1
        for action in range(len(actions)):
            try:
                X2 = plot_curve(coord_list[action*frame_rate][0], coord_list[action*frame_rate][1], angleList[action*frame_rate], actions[action*frame_rate][0],
                            actions[action*frame_rate][1],'blue',0.5,coord_list, "Optimal Node Path")  # (0,0,45) hypothetical start configuration
            except:
                break
    # except:
    #     print("ERROR:",action)

    # X1= plot_curve(-4, -4,60, act[action][0],act[action][1]) # (0,0,45) hypothetical start configuration
    #
    # for action in range(len(act)):
    #     X2=plot_curve(X1[0],X1[1],X1[2], act[action][0],act[action][1])

    # plt.grid()
    #
    # # ax.set_aspect('equal')
    #
    # plt.xlim(-5, 5)
    # plt.ylim(-5, 5)

    # plt.title('How to plot a vector in matplotlib ?', fontsize=10)

    # plt.show()
    # plt.close()

