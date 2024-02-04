class Time:
    def __init__(self, seconds):
        self.seconds = seconds
    def minutes(self):
        return self.seconds/60
    def hours(self):
        return self.seconds / 3600
    def from_minutes(self, minutes):
        self.seconds = minutes * 60
    def from_hours(self, hours):
        self.seconds = hours * 3600 
time1 = Time(600)
print(time1.minutes())
print(time1.hours())
time1.from_minutes(40)
print(time1.seconds) 
time1.from_hours(0.6)
print(time1.seconds) 
