import time
import random
import tkinter as tk

# Existing functions
class TypingTest():
    def __init__(self, root):
        self.root = root
        self.words = ["house", "shoes", "hello", "can't", "gasps", "tears", "monks", "donut", "silly", "funny", "found", "hours", "lucky", "sucks", "mucks"]
        self.total_time = 0
        self.total_words_typed = 0
        self.sentence = []
        self.start()
    def start(self):
        for i in range(8):
            self.sentence.append(random.choice(self.words))
        self.sentence = " ".join(self.sentence)
        self.startLabel = tk.Label(root, text=f"\nType the following words as quickly and accurately as you can.\n Sentence: {self.sentence} \n Press Enter when you are ready to start")
        self.startLabel.pack()
        self.startLabel.bind("<Return>", self.typing)
    def typing(self):
        self.start_time = time.time()
        typingLabel = tk.Label(root, text="\nStart typing here: ")
        typingLabel.pack()
        self.textbox = tk.Text(root, width=50, height=1)
        self.end_time = time.time()
        self.text = self.textbox.get("1.0", tk.END)
        self.getScore()
    def getScore(self):
        self.elapsed_time = self.end_time - self.start_time
        self.total_time += self.elapsed_time
        self.words_typed = len(self.text.split())
        self.total_words_typed += self.words_typed
        self.typing_speed = round(self.words_typed / (self.elapsed_time / 60), 1)  # Round speed to 1 decimal place
        self.accuracy = calculate_accuracy(self.sentence, self.text)
        self.real_speed = self.typing_speed * self.accuracy
        self.real_speed = self.real_speed / 100
    def finalScore(self):
        self.finishLabel = tk.Label(root, text=f"\nTest completed!\nTyping Speed: {self.typing_speed:.0f} WPM\nAccuracy: {self.accuracy:.0f}%\nReal Speed: {self.typing_speed:.0f} WPM x {self.accuracy:.0f}% = {self.real_speed:.0f} WPM")
        self.finishLabel.pack()


def calculate_accuracy(reference, typed):
    reference_words = list(reference)
    typed_words = list(typed)

    correct_words = 0
    for ref_word, typed_word in zip(reference_words, typed_words):
        if ref_word == typed_word:
            correct_words += 1

    return (correct_words / len(reference_words)) * 100

def playAgain(root:tk.Tk):
    global playing
    root.destroy
    root = tk.Tk()
    playing = True
def playNoMore(root:tk.Tk):
    root.destroy
root = tk.Tk()

playing = True
while playing:
    TypingTest(root)
    playingLabel = tk.Label(root, text="Again? (y/n)")
    playingY = playingLabel.bind("y", playAgain)
    playingX = playingLabel.bind("n", playNoMore)

root.mainloop()