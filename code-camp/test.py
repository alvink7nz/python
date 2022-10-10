import winsound

def make_sound():
    for i in range(40):
        winsound.Beep(2000, 200)

make_sound()
