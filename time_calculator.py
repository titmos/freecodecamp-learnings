# acknowledge adviksinghania and github people
def add_time(start, lenght, day=None):
    # list days of the week
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    # Begin time and lenght
    Start_time = list(map(int, start[:-3].split(':')))
    lenght = list(map(int, lenght.split(':')))

    # minutes 
    Start_time[1] += lenght[1]
    x = 0  # to store the extra number of hours (60 minutes)
    while Start_time[1] > 60:
        x += 1
        Start_time[1] -= 60
    
    # hours
    Start_time[0] += x + lenght[0]
    x = 0  # counter for days
    while Start_time[0] >= 12:
        Start_time[0] -= 12
        if 'PM' in start:
            
            x += 1
            
            start = start.replace('PM', 'AM')
        elif 'AM' in start:
            
            start = start.replace('AM', 'PM')

    Start_time[0] = '12' if Start_time[0] == 0 else str(Start_time[0])
    Start_time[1] = str(Start_time[1]).rjust(2, '0')
    new_time = ':'.join(Start_time) + start[-3:]

    if day is not None:
        day = day.lower().capitalize()
        days = days[days.index(day):] + days[:days.index(day)]
        n = x
        while n > 7:
            n -= 7
        new_time += ', ' + days[n]
    
    if x == 1:
        new_time += ' (next day)'
    elif x > 1:
        new_time += ' (' + str(x) + ' days later)'

    return new_time