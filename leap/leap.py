import calendar
def is_leap_year(year):
    
    if calendar.isleap(int(year)):
        return True
    else:
        return False
