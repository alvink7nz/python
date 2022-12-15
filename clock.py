from turtle import *
from time import *

mode('logo')
h = Turtle()
h.color('blue')
h.shape('arrow')
h.shapesize(1, 10)

m = Turtle()
m.color('black')
m.shape('arrow')
m.shapesize(1, 14)

s = Turtle()
s.color('red')
s.shape('arrow')
s.shapesize(1, 15)

def showhands():
    global s, m, h
    t = localtime()
    s.seth(t.tm_sec * 6)
    m.seth(t.tm_min * 6)
    h.seth(t.tm_hour * 30 + t.tm_min * 0.5)
    ontimer(showhands, 1000)

showhands()