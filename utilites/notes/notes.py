from tkinter import *
import os

root = Tk()
root.title("Notebook")

def getNote(name):
    file_path = "C:/Users/alvin/code/python/utilites/notes/notes.txt"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    with open(file_path, 'r') as plainNotes:
        notes = plainNotes.read()
        notes = notes.split("\n\n")
        for note in notes:
            note = note.split(":")
            if note[0] == name:
                return note[1]
        return None
    
class writeNote():
    def __init__(self) -> None:
        self.label = Label(root, text="Please enter name fo note to write in:")
        self.label.pack()
        self.name = Entry(root, width=30)
        self.name.pack()
        self.text = Text(root, width=50, height=4)
        self.submit = Button(root, text="Submit", command=self.displayTextEntry)
        self.submitText = Button(root, text="Submit Text", command=self.PutInNote)
        self.submit.pack()
        self.note = None
        self.newNotes = []
    def displayTextEntry(self):
        self.text.pack()
        self.submitText.pack()
    def PutInNote(self):
        self.note = self.text.get("1.0", END)
        file_path = "C:/Users/alvin/code/python/utilites/notes/notes.txt"
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return None
        with open(file_path, 'r') as plainNotes:
            notes = plainNotes.read()
            notes = notes.split("\n\n")
        with open(file_path, 'w') as AllNotes:
            for note in notes:
                note = note.split(":")
                if note[0] == self.name:
                    note[1] == self.note
                note = ':\n'.join(note)
                print(note)
                self.newNotes.append(note)
            self.newNotes = '\n\n'.join(notes)
            print(self.newNotes)
            AllNotes.write(self.newNotes)

class readNote():
    def __init__(self) -> None:
        self.label = Label(root, text="Please enter name fo note:")
        self.label.pack()
        self.Entryvar = Entry(root, width=30)
        self.Entryvar.pack()
        self.submit = Button(root, text="Submit", command=self.displayNote)
        self.submit.pack()
    def displayNote(self):
        note = getNote(self.Entryvar.get())
        if note:
            note_text = str(note)
            label = Label(root, text=f"{self.Entryvar.get()}'s text: {note_text}")
        else:
            label = Label(root, text=f"No note found for {self.Entryvar.get()}")
        label.pack()

read = Button(root, text="Read Notes", command=readNote)
write = Button(root, text="Write notes", command=writeNote)
read.pack()
write.pack()

root.mainloop()