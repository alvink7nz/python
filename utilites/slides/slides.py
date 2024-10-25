import tkinter as tk

slides = [
    {"title": "", "text": "", "font": "Arial"}
]
slideIndex = 0
def changeFont(thing: tk.Text, newfont):
    try:
        # Get the current selection range
        start_index = thing.index(tk.SEL_FIRST)  
        end_index = thing.index(tk.SEL_LAST)  
        thing.tag_configure('font_change', font=(newfont, 18))  
        thing.tag_add('font_change', start_index, end_index)
    except tk.TclError:
        thing.config(font=(newfont, 18))

def updateSlide():
    global slideIndex
    title.delete(0, tk.END)
    title.insert(0, slides[slideIndex]["title"])
    
    text.delete(1.0, tk.END)
    text.insert(tk.END, slides[slideIndex]["text"])

def saveSlide():
    global slideIndex
    slides[slideIndex]["title"] = title.get()
    slides[slideIndex]["text"] = text.get(1.0, tk.END).strip()

def nextSlide():
    global slideIndex
    if slideIndex < len(slides) - 1:
        saveSlide()  # Save current text data before moving to the next one
        slideIndex += 1
        updateSlide()

def previousSlide():
    global slideIndex
    if slideIndex > 0:
        saveSlide()  # Save current text data before moving to the previous one
        slideIndex -= 1
        updateSlide()

def newSlide():
    global slideIndex
    slides.append({"title": "", "text": "", "font": "Arial"})
    saveSlide()
    slideIndex = len(slides) - 1
    updateSlide()

def toSlide(slideNum):
    global slideIndex
    slideIndex = slideNum - 1
    updateSlide()

def controlMode():
    return True

root = tk.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.title("Notes")
root.geometry(f"{screenWidth}x{screenHeight}")

title = tk.Entry(root, font=("Arial", 24), width=40)
title.pack(pady=30)

text = tk.Text(root, font=("Arial", 16), wrap=tk.WORD, height=15, width=70)
text.pack(pady=10)

prev_button = tk.Button(root, text="Previous slide", command=previousSlide())
prev_button.pack(side=tk.LEFT, padx=20, pady=20)

next_button = tk.Button(root, text="Next slide", command=nextSlide())
next_button.pack(side=tk.RIGHT, padx=20, pady=20)

newSlideButton = tk.Button(root, text="New slide", command=newSlide)
newSlideButton.pack(side=tk.TOP)

text.bind("<Left>", previousSlide())
text.bind("<Right>", nextSlide())

menuBar = tk.Menu(root)
root.config(menu=menuBar)
changeFontMenu = tk.Menu(menuBar, tearoff=0)

changeFontMenu.add_command(label="Arial", command=lambda: changeFont(text, "Arial"))
changeFontMenu.add_command(label="Courier", command=lambda: changeFont(text, "Courier"))
changeFontMenu.add_command(label="Verdana", command=lambda: changeFont(text, "Verdana"))
changeFontMenu.add_command(label="Impact", command=lambda: changeFont(text, "Impact"))
changeFontMenu.add_command(label="Tahoma", command=lambda: changeFont(text, "Tahoma"))
menuBar.add_cascade(label="Font", menu=changeFontMenu)

quickScroll = tk.Menu(menuBar, tearoff=0)
counter = 1
for i in slides:
    quickTitle = i["title"]
    quickScroll.add_command(label=f"{counter}: {quickTitle}", command=toSlide(counter))
    counter += 1
menuBar.add_cascade(label="Slides", menu=quickScroll)

root.mainloop()