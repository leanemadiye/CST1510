"""
RECORD CHECK  -  my version
===========================

Name  : Leane
Lane  : Cyber 
Date  : 22-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# 1. Define a class called Record.
#
# adding a method status(self) that returns "OVER LIMIT" (100%+),
# "WARNING" (90%+) or "OK", worked out from self.value and
#self.limit.
 
class Record:
    def __init__(self, label, value, limit):
        """initiaze a Record with label,value and limit"""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returning status based on value vs limit"""
        percent = (self.value / self.limit) *100
        if percent > 100:
            return "OVERLIMIT"
        elif percent > 90:
            return "WARNING"
        else:
            return "OK"
        
# 2. Create your records.

# creating 2 Record instances
rec1 = Record("Srv", 85, 100)
rec2 = Record("Srv", 90, 100)

records = [rec1, rec2]  #storing them in a list

for r in records:       
    print(r.status())   #printing each ones status

# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"Value: {record.value}")
    print(f"Limit: {record.limit}")
    print(f"Status: {record.status()}")

    print("=" * 34)

