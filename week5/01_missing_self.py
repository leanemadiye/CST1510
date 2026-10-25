# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def status(self,percent):    # this parameter should be self
        return percent           #self should be the first parameter inside a class after creating a method

r = Record()
print(r.status(95))
