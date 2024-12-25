import datetime
from tkinter import Tk, Canvas

todayDate = datetime.datetime.today().date()
todayDate = str(todayDate)
listTodayDate = todayDate.split("-")
dateTodayDate = datetime.datetime.today().date()
def differences(date1, date2):
    difference = str(date1 - date2)
    numOfDays = difference.split(" ")
    return numOfDays

def readFiles():
    dates = []
    with open("c:/Users/alvin/code/python/utilites/calendar/dates.txt", 'r') as file:
        file = file.readlines()
        for line in file:
            line = line.split(", ")
            month, day = line[1].split('/')
            month = month.zfill(2)  # Zero-pad month to 2 digits
            day = day.zfill(2)      # Zero-pad day to 2 digits
            # Construct the full date string and convert to a datetime object to ensure format
            if (int(listTodayDate[1]) < int(month)) or (int(listTodayDate[1]) == int(month) and int(listTodayDate[2]) < int(day)):
                full_date_str = f"{listTodayDate[0]}/{month}/{day}"
            else:
                nextYr = int(listTodayDate[0]) + 1
                full_date_str = f"{nextYr}/{month}/{day}"
            line[1] = full_date_str.strip()
            eventDate = datetime.datetime.strptime(line[1], "%Y/%m/%d").date()
            line[1] = eventDate
            dates.append(line)
    return dates

dates = readFiles()
root = Tk()
root.title("Calendar")

c = Canvas(root, width=800, height=600, bg="green")
c.pack()
c.create_text(30, 30, anchor="w", fill="orange", font="Arial 30 bold underline", text="My Calendar")
verticalSpace = 100
dates.sort(key=lambda x: x[1])
for date in dates:
    daysUntil = differences(date[1], dateTodayDate)
    eventName = date[0]
    display = f"There are {daysUntil[0]} days until {eventName}"
    c.create_text(30, verticalSpace, anchor="w", fill="black", font="Arial 30 bold", text=display)
    verticalSpace += 32

root.mainloop()