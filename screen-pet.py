from tkinter import HIDDEN, NORMAL, Tk, Canvas
from time import sleep

def toggle_eyes():
    c.itemconfigure(pupil_left, state=HIDDEN)
    c.itemconfigure(pupil_right, state=HIDDEN)
    c.itemconfigure(eye_left, fill='SkyBlue1')
    c.itemconfigure(eye_right, fill='SkyBlue1')

def open_eyes():
    c.itemconfigure(pupil_left, state=NORMAL)
    c.itemconfigure(pupil_right, state=NORMAL)
    c.itemconfigure(eye_left, fill='white')
    c.itemconfigure(eye_right, fill='white')

def blink():
    toggle_eyes()
    root.after(250, open_eyes)
    root.after(3000, blink)

def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False
def tougue_out():
    c.itemconfigure(tougue_main, state=NORMAL)
    c.itemconfigure(tougue_tip, state=HIDDEN)
    return
def toggle_tongue():
    if not c.tougue_out:
        c.itemconfigure(tougue_tip, state=NORMAL)
        c.itemconfigure(tougue_main, state=NORMAL)
        c.tougue_out = True
    else:
        c.itemconfigure(tougue_tip, state=HIDDEN)
        c.itemconfigure(tougue_main, state=HIDDEN)
        c.tougue_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return
def show_happy(event):
    if(20 <= event.x and event.x <= 350) and (20 <= event.y and event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10
    return
def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return
def sad():
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=HIDDEN)
    c.itemconfigure(mouth_sad, state=NORMAL)
root = Tk()
root.title('screen pet')
c = Canvas(root, width=500, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.body_colour = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_colour, fill=c.body_colour)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_colour, fill=c.body_colour)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_colour, fill=c.body_colour)
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_colour, fill=c.body_colour)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_colour, fill=c.body_colour)
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 220, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tougue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tougue_tip = c.create_oval(170, 270, 230, 315, outline='red', fill='red', state=HIDDEN)
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)
food = c.create_oval(170, 250, 100, 280, fill='Peru', state=HIDDEN)
c.pack()
time = 10000
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
c.eyes_crossed = False
c.tougue_out = False
root.after(5000, blink)
while root.mainloop():
    root.after(time, sad)
    time = time + 10000
root.mainloop()

        
   


