from tkinter import Tk, Canvas
from datetime import date, datetime

def get_events():
    list_events = []
    with open('python\my-records-of-time\event.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date = datetime.strptime(current_event[1], '%d/%m/%Y').date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

root = Tk()

c = Canvas(root, width=600, height=270, bg='green')
root.title('alvin\'s important dates')
c.pack()
c.create_text(170, 15, anchor='w', fill='white', font='Arial 18 bold underline', text='alvin\'s important dates')

events = get_events()
today = date.today()

vertical_space = 60
events.sort(key=lambda x: x[1])
for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = 'it\'s %s days until %s'% (days_until, event_name)
    if (int(days_until) <= 7):
        text_col = 'red'
    else:
        text_col = 'lightblue'
    c.create_text(50, vertical_space, anchor='w', fill=text_col, font='Arial 18 bold', text=display)

    vertical_space += 30

root.mainloop()