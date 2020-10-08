def check_day_week(day):
    week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }
    try:
        if day in week:
            return week[day]
        else:
            
    except:
        print("There is no such day of the week!Please try again")

print(check_day_week(0))
