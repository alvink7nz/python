import turtle as t
import tkinter as tk
from tkinter import messagebox


def splitString(string):
    dashSplit = string.split("-")
    command = []
    for i in dashSplit:
        commaSplit = i.split(",")
        command.append(commaSplit)
    return command
repeat = 0
def drawCommand(drCo):
    global drawScreen
    def line(direction, long=0):
        global repeat
        if direction == "F" :
            myturtle.forward(long)
        elif direction == "B":
            myturtle.backward(long)
        elif direction == "R":
            myturtle.right(long)
        elif direction == "L":
            myturtle.left(long)
        elif direction == "U":
            myturtle.up()
        elif direction == "F":
            myturtle.down()
        elif direction == "REPEAT"  and repeat == 0:
            repeat = long + 1
        elif direction == "REPEAT"  and repeat > 0:
            pass
        elif direction == "ENDREPEAT" and repeat == 0:
            pass
        elif direction == "ENDREPEAT" and repeat > 0:
            for i in range(len(drCo)-1,-1,-1):
                if drCo[i][0] == "REPEAT":
                    messagebox.showinfo("Repeat", f"repeat found: {i}")
                    break
            repeat -= 1
    targetLetter = ["F","B","R","L","U","D","REAPEAT","ENDREPEAT"]
    found = True
    for element in drCo:
        firstElement = element[0]
        if any(char in targetLetter for char in firstElement):
            pass
        else:
            messagebox.showwarning("Incorect Element", f"Incorect Element From Command: {firstElement}")
            return
    for i in drCo:
        way = i[0]
        if len(i) > 1:
            strMuch = i[1]
            much = int(strMuch)
        else:
            strMuch = None
            much = None
        if much is not None:
            line(way, much)
        elif much is None:
            line(way)
    drawScreen.exitonclick()
drawScreen = t.Screen()
drawScreen.screensize(1400,800)
myturtle = t.Turtle()
myturtle.hideturtle()

instructions = '''Command Rules:
                      F = Forward
                      B = Backward
                      R = Turn right
                      L = Turn left
                      U = Pen up
                      D = Pen down
                      then a comma
                      then enter length(pixels) or degrees(if L or R)
                      then a dash
                      repeat until finished command
                      e.g, F,100-R,90-F,100. It will go forward 100 pixels,
                      turn right 90 degrees and go foward 100 pixels.
                      Enter command below'''
draw = drawScreen.textinput("Command", instructions)
splitDraw = splitString(draw)
drawCommand(splitDraw)