# Implementation-of- A-Star -algorithm on Turtle-bot
### Description
Implementation of A* algorithm is tested on an obstacle space for turtle bot. The turtle bot will maneuver through the obstacle space to reach the goal point with minimum cost. For rigid robot, the dimension of the robot is also considered and world space is converted into configuration space by increasing the scale of the obstacles and converting the rigid robot into point robot.

### Actions
There are eight acions carried out to make the robot reach the goal point:
1. [0, RPM1]
2. [RPM1, 0]
3. [RPM1, RPM1]
4. [0, RPM2]
5. [RPM2, 0]
6. [RPM2, RPM2]
7. [RPM1, RPM2]
8. [RPM2, RPM1]


### Dependencies 
python -version 3   

### Library
Numpy
math
matplotlib (dependencies to be installed)
cv2
time

### Run Code
Enter the following to run the Astar for Turtle-bot.

```
cd [to 'codes' directory]
python3 Phase3.py  for Linux   

python Phase3.py   for Windows 
```

### Input Instruction:
All the dimensions are in meter

As soon as you run the program, the following prompt occurs in the command window:
```
Enter the Clearance required for the Rigid body:

Enter Left wheel and Right wheel RPM(values seperated by space)

Enter the value of Start Node X co-ordinate:

Enter the value of Start Node Y co-ordinate:

Enter the value of Goal Node X co-ordinate:

Enter the value of Goal Node Y co-ordinate:

Enter the start angle in degrees:
```
For all these prompt please enter integers between -5 and 5 for X-coordinate and -5 and 5 for Y-coordinate.

Angle: Enter the Start angle (robot orientation) in degrees in the range 0 to 360

Please enter the elements of the matrix row wise typing enter

Please enter the RPM values seperated by space


### Sample output for rigid robot:
After running the python file
```
Enter the Clearance required for the Rigid body:0

Enter Left wheel and Right wheel RPM(values seperated by space): 25 30

Enter the value of Start Node X co-ordinate:-6

Enter the value of Start Node Y co-ordinate:-4

Enter the value of Goal Node X co-ordinate:3

Enter the value of Goal Node Y co-ordinate:4.5

Enter the start angle in degrees:60

Entered input is out of bounds. Please enter a valid input!!

Enter the value of Goal Node X co-ordinate:-4

Enter the value of Goal Node Y co-ordinate:-4
Exploring nodes...
```
```
Cost took to reach the goal is: 12.2955435
Backtracking...
Total time taken is 8.91 seconds (video generation takes 1+ hours).
```

### Output Video
Make sure 'Node' folder exists before uncommenting the lines in the code to generate the video. 
The video was sampled at a frame rate of 3 frames per second for explored nodes and at a frame rate of 1 frames per second for the optimal path generated. An image of the final output is also attached (actual_output_img.png and zoomed_actual_img.png) which displays all the visited nodes.


### Output Images
![Output_actual.](actual_output_img.png)
![Output_zoomed.](zoomed_actual_img.png)
![Output_video_result.](output_img.png)

### Legend
Goal area is shown by green circle

Explored Nodes are shown by brown curves

Optimal Path is shown by black curve

### Note
For small distances, after finding the goal point the matplotlib will immediately start the simulation and reach the goal point. The goal exploration is not clearly seen for small distances. For large distances it is clearly seen.


### Commits
Due to many test codes we could not make commits to the github repository.