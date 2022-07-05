
from turtle import Turtle as t, getscreen
import re

def draw(do_val):
    mg = re.match(r"^([A-Z])([\d]*)", do_val)
    if mg.group(1).lower() == 'f':
        t.forward(self = t, distanse = int(mg.group(2)))
    elif mg.group(1).lower() == 'b':
        t.back(self = t, distanse = int(mg.group(2)))
    elif mg.group(1).lower == 'r':
        t.right(self = t, distance = int(mg.group(2)))
    else:
        t.left(self = t, distanse = int(mg.group(2)))

instructions = '''Enter a program for a drawing:
eg F100-R45-U-F100-L45-D-F100-R90-B50
N = new drawing
U/D = pen up/pen down
F = forward
B = backward
R = right(put the degrees after)
L = left(put the degrees after)'''

Screen = getscreen()
t_program = Screen.textinput('drawing machine', instructions)
while True:
    if t_program == None or t_program.upper() == 'END':
        break
    else:
        draw(t_program)
        t_program = Screen.textinput('drawing machine', instructions)