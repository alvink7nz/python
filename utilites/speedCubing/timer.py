import tkinter as tk
import time
import scrambleGenerator

class TimerApp:
    def __init__(self, root:tk.Tk, scramble):
        self.root = root
        self.root.title("Timer App")

        self.letterScramble = scramble

        self.scramble = tk.Label(root, text=scramble, font=("Helvetica", 24))
        self.scramble.place(x=120, y=50)

        self.time_label = tk.Label(root, text="0.00", font=("Helvetica", 100))
        self.time_label.place(x=400, y=250)

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.root.bind('<KeyRelease-space>', self.startTimer)

    def startTimer(self, event):
        self.running = True
        self.start_time = time.time()
        self.update_timer()
        root.bind('<space>', self.stopTimer)

    def stopTimer(self, event):
        self.running = False
        self.elapsed_time = time.time() - self.start_time
        self.root.unbind("<KeyRelease-space>")
        self.root.after(300, self.resetTimer)

    def resetTimer(self):
        self.root.bind("<KeyRelease-space>", self.startTimer)

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=f"{self.elapsed_time:.2f}")
            self.root.after(50, self.update_timer)

if __name__ == "__main__":
    scramble = scrambleGenerator.scramble
    root = tk.Tk()
    root.geometry("800x600")
    app = TimerApp(root, scramble)
    root.mainloop()