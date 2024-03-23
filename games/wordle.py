from tkinter import *
from tkinter.messagebox import showinfo
import random

# Define the list of words
word_list = [
    "apple", "table", "chair", "house", "mouse",
    "happy", "funny", "smile", "sunny", "cloud",
    "water", "ocean", "river", "music", "dance",
    "dream", "sleep", "awake", "learn", "teach",
    "study", "write", "paint", "color", "green",
    "blue", "black", "white", "pages", "makes"
]

# Choose a random word from the list
target_word = random.choice(word_list)

root = Tk()
root.title("Wordle")

def checkGuess(guess, answer):
    if guess == answer:
        showinfo("Correct", "Correct!")

def main():
    pass