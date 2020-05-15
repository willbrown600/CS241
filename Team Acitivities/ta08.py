##############################################
# Team Activity 08, CS241
# Author: Will Brown
# Instructor: Brother N Parrish
##############################################

class Time:
    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
        self._period = ""

    def _set_hours(self, value):

        if value > 23:
            self._hours = 23
        elif value < 0:
            self._hours = 0
        else:
            self._hours = value

    def _get_hours(self):

        return self._hours

    def _set_minutes(self, value):

        if value >= 60:
            self._minutes = 59
        elif value < 0:
            self._minutes = 0
        else:
            self._minutes = value

    def _get_minutes(self):

        return self._minutes

    def _set_seconds(self, value):

        if value >= 60:
            self._seconds = 59
        elif value < 0:
            self._seconds = 0
        else:
            self._seconds = value

    def _get_seconds(self):

        return self._seconds

   
    @property
    def hours_simple(self):

        return self._hours    


    @hours_simple.setter
    def hsetter(self):
        
        if self._hours > 12:
            self._hours = self._hours - 12
        else:
            self._hours = self._hours

        
    @property
    def period(self):
        
        return self._period
        
    @period.setter
    def p(self):
        
        if self._set_hours() <= 12:
            self._period = "AM" 
        else:
            self._period = "PM"

    

    hours = property(_get_hours, _set_hours)
    minutes = property(_get_minutes, _set_minutes)
    seconds = property(_get_seconds, _set_seconds)

def main():

    t = Time()
    print()
    print("Enter time: ")
    h = int(input("Hours: "))
    m = int(input("Minutes: "))
    s = int(input("Seconds: "))

    t.hours = h
    t.minutes = m
    t.seconds = s

    
    print()
    print("The time is: {}:{}:{} in 24 hour clock display".format(t.hours, t.minutes, t.seconds))
    print()

    print("Time with 12 hour clock is: {}:{}:{} {}".format(t.hours_simple, t.minutes, t.seconds, t.period))
    print()










if __name__ == "__main__":
    main()

