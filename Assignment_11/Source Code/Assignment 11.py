import time

class Clock:

    def __init__(self, hour, minute, second, clock_type=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clock_type = clock_type

    def __str__(self):
        if (self.clock_type == 0):
            return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
        else:
            return "{:02}:{:02}:{:02} {}".format(self.hour, self.minute, self.second, 'pm' if self.hour > 11 else 'am')
    
    def tick(self):
        self.second += 1

        if (self.second == 60):
            self.second = 0
            self.minute += 1
        else:
            return
        
        if (self.minute == 60):
            self.minute = 0
            self.hour += 1
        else:
            return

        if (self.hour == 24):
            self.hour = 0

if __name__ == "__main__":
    h = int(input("What is current hour ==> "))
    m = int(input("What is current minute ==> "))
    s = int(input("What is current second ==> "))
    clock = Clock(h, m, s, 1)

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)

