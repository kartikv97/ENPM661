# Implementation-of-Dijkstra-algorithm
### Description
Implementation of A* algorithm is tested on a obstacle space for rigid robot. The robot will maneuver through the obstacle space to reach the goal point with minimum cost. For rigid robot, the dimension of the robot is also considered and world space is converted into configuration space by increasing the scale of the obstacles and converting the rigid robot into point robot.

### Actions
There are five acions carried out to make the robot reach the goal point:
1. firstAction
2. secondAction
3. thirdAction
4. fourthAction
5. fifthAction



### Dependencies 
python -version 3   

### Library
Numpy
math
matplotlib

### Run Code
Enter the following to run the Astar for rigid robot.

```
cd [to 'codes' directory]
python3 Astar_rigid.py
```

### Input Instruction:
As soon as you run the program, the following prompt occurs in the command window:
```
Enter the Radius of the Rigid body:

Enter the Clearance required for the Rigid body:

Enter the value of Start Node X co-ordinate:

Enter the value of Start Node Y co-ordinate:

Enter the value of Goal Node X co-ordinate:

Enter the value of Goal Node Y co-ordinate:

Enter the step size in range 1-10:

Enter the start angle in degrees:
```
For all these prompt please enter integers between 0 and 299 for X-coordinate and 0 and 199 for Y-coordinate.
Please enter the elements of the matrix row wise typing enter


### Sample output for rigid robot:
After running the python file
```
Enter the Radius of the Rigid body:5
Enter the Clearance required for the Rigid body:5

Enter the value of Start Node X co-ordinate:50

Enter the value of Start Node Y co-ordinate:30

Enter the value of Goal Node X co-ordinate:195

Enter the value of Goal Node Y co-ordinate:295

Enter the step size in range 1-10:1

Enter the start angle in degrees:60

Entered input is out of bounds. Please enter a valid input!!

Enter the value of Goal Node X co-ordinate:150

Enter the value of Goal Node Y co-ordinate:150
Exploring nodes...
```
```
Cost took to reach the goal is: 395.64675298172733
Backtracking...
Total time taken 160.9800910949707
```
For worst case time taken for rigid robot is 201.9800910949707 seconds.

### Note
For small distances, after finding the goal point the matplotlib will immediately start the simulation and reach the goal point. The goal exploration is not clearly see for small distances. For large distances it is clearly seen.

### Obstacle assumption:
In obstacle space, for rectangle obstacle which is faced at an angle of 30 degrees, we were getting decimal points as coordinates. So we round that to integer as pixel values cannot be decimals. As a result, when you give 10 or greater than 10 as clearance, the shape of the rectangle may differ.

### Commits
Due to many test codes we could not make commits to the github repository.
