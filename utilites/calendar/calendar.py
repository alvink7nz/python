import datetime

todayDate = datetime.datetime.today().date()
todayDate = str(todayDate)
todayDate = todayDate.split("-")

def readFiles():
    dates = []
    with open("c:/Users/alvin/code/python/utilites/calendar/dates.txt", 'r') as file:
        for line in file:
            line = line.split(", ")
            month, day = line[1].split('/')
            month = month.zfill(2)  # Zero-pad month to 2 digits
            day = day.zfill(2)      # Zero-pad day to 2 digits
             # Construct the full date string and convert to a datetime object to ensure format
            full_date_str = f"{todayDate[0]}/{month}/{day}"
            line[1] = full_date_str.strip()
            eventDate = datetime.datetime.strptime(line[1], "%Y/%m/%d").date()
            line[1] = eventDate
            dates.append(line)
    return dates

dates = readFiles()
print(dates)
print(todayDate)

def differences(date1, date2):
    difference = date1 - date2
    return difference