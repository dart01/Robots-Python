from roboticstoolbox import *
from spatialmath.base import tr2rpy
from sympy import *
import numpy as np
from numpy.linalg import multi_dot

a1 = 8
a2 = 12
a3 = 12


q1 = 0
q2 = 0
q3 = 0

R = []
R.append(RevoluteDH(d=a1, alpha=np.pi/2, a=0, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=a2, offset=0))
R.append(RevoluteDH(d=0, alpha=0, a=a3, offset=0))

Robot = DHRobot(R, name='3R')
print(Robot)

Robot.teach([q1, q2, q3], 'rpy/zyx', limits=[-30,30,-30,30,-30,30])


MTH = Robot.fkine([q1,q2,q3])
print(MTH) 
# Matriz (DH)
TZ0 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, a1],[0, 0, 0, 1]])
RZ0 = np.array([[cos(q1), -sin(q1), 0, 0],[sin(q1), cos(q1), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
TX1 = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
RX1 = np.array([[1, 0, 0, 0],[0, cos(pi/2), -sin(pi/2), 0],[0, sin(pi/2), cos(pi/2), 0],[0, 0, 0, 1]])
T01 = multi_dot([TZ0, RZ0, TX1, RX1])


