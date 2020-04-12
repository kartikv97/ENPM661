# Implementation-of- A-Star -algorithm on Turtle-bot and Simulation on V-REP
### Description
Implementation of A* algorithm is tested on an obstacle space for turtle bot. The turtle bot will maneuver through the obstacle space to reach the goal point with minimum cost. The simulation is done in V-REP by importing Turtle-bot modle from the library.

Files need to be included in the same folder to have established Remote API bindings

  1. Make sure "vrep.py" and "vrepConst.py" are also present in the same folder as the execution code these files can be found at (programming\remoteApiBindings\python\python)

  2. Check the V-REP version as "remoteApi.dll" is based on either 32-bit or 64-bit version (for windows .dll file is needed , for other OS, other compatible files needed to be placed in the same folder and can be obtained from "programming\remoteApiBindings\lib\lib")

  3. V-REP scene (phase4.ttt)

  4. To include turtlebot model in your V-REP, simply add the model file (Turtlebot2.ttm) inside the main folder of V-REP installation at the location "models\robots\mobile".

Steps to run the code

1. Open V-REP and place the turtle-bot at the start location with initial orientation and initiate the simulation

2. Run the python file
    -"Phase4.py" in which cost is calculated as the Euclidean distance.

### Note
Run the simulation in the V-REP first and then run the Phase4.py file. The simulation in the V-REP will only start after the turtle bot reaches the goal.

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
matplotlib
cv2
time
vrep

### Run Code
Enter the following to run the Astar for rigid robot.

```
cd [to 'codes' directory]
python3 Phase4.py  for Linux   

python Phase4.py   for Windows 
```

### Input Instruction:
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


### Sample output for Turtle-bot:
After running the python file
```
Enter the Clearance required for the Rigid body:0

Enter Left wheel and Right wheel RPM(values seperated by space): 25 30

Enter the value of Start Node X co-ordinate:-6

Enter the value of Start Node Y co-ordinate:-4

Enter the value of Goal Node X co-ordinate:0

Enter the value of Goal Node Y co-ordinate:-3

Enter the start angle in degrees:90

Entered input is out of bounds. Please enter a valid input!!

Enter the value of Start Node X co-ordinate:-4

Enter the value of Start Node Y co-ordinate:-4
Exploring nodes...
```
```
Cost took to reach the goal coordinate(0,-3) is: 11.783545
Time taken to reach the goal coordinate(0,-3) is: 9.8 seconds
Cost took to reach the goal coordinate(3.7,1.7) is: 10.67
Time taken to reach the goal coordinate(3.7,1.7) is: 10.89 seconds
Backtracking...
```
```
Program Started

Connected to remote API server

Program ended
```
### Note
The value of simulation_runtime_per_action for output 1 is 1.09999
The value of simulation_runtime_per_action for output 2 is 1.14
### Output Video
There are 2 video samples along with the code with simulation
1. Phase4_video1 with initial coordinate (-4,-4) and goal at (0,-3) with initial orientation as 90 degrees. The robot is not reaching the exact coordinates because of the threshold given. In the attached image the followed path can be seen.
2. Phase4_video2 with initial coordinate (-4,-4) and goal at (3.7,1.7) with initial orientation as 90 degrees. The robot is not reaching the exact coordinates because of the threshold given. In the attached image the followed path can be seen.

### Special Instructions
For the older V-REP version port number is 1997. Change it in the turtle bot Lua script and in the Phase4.py file.

Under no circumstance stop the V-REP simulation before stopping the python file, if done it will corrupt the file and you will have to re-extract the phase 4 from the original zip. 
 
### Commits
Due to many test codes we could not make commits to the github repository.