from tkinter.filedialog import *
import datetime

todayDate = datetime.datetime.today().date()
todayDate = str(todayDate)
todayDate = todayDate.split("-")

def readFiles():
    dates = []
    filePath = askopenfilename(title="dates", filetypes=[("Text files", "*.txt")], initialdir="c:/Users/alvin/code/python/utilites/calendar")
    with open(filePath, 'r') as file:
        for line in file:
            dates.append(line.strip())
    return dates

dates = readFiles()
findDate = []
for line in dates:
    line = line.split(", ")
    findDate.append(line)
dates = findDate
print(dates)
print(todayDate)

for date in dates:
    addYrDate = date[1]
    addYrDate = todayDate[0] + "/" + addYrDate
    date[1] = addYrDate
print(dates)