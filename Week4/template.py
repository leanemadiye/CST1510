"""
RECORD CHECK  -  my version
===========================

Name  :Leane
Lane  :Cyber
Date  :15-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
# one line docstring


def check(value, limit):
    """calculate difference, percent and status from value and limit"""
    difference = value - limit
    percent = (value / limit * 100)if limit != 0 else 0
    status ="OVER LIMIT" if value > limit else"OK"
    return difference, percent, status

def print_report(label, value, limit,difference,percent,status):
    """print a formatted usage report"""
    print(f"{label}:")
    print(f"value: {value}")
    print(f"limit: {limit}")
    print(f"difference: {difference}")
    print(f"percent: {percent:.1f}%")
    print(f"status: {status}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#  writing a function load_records(path) that reads
#  label,value,limit lines from a file and returns the list.
# Making a data file, one record per line.

with open("data.txt","w")as f:
    f.write("server A,85,100\n")
    f.write("server B,90,100\n")
    f.write("server C,110,100\n")

def load_records(path):
    """read records from a file and return a list of dictionaries"""
    records =[]

    with open(path,"r")as f:        #opening the file for reading
        for line in f:
            label,value,limit =line.strip().split(",")

            record={
                "label": label,
                "value": int(value),
                "limit": int(limit)
            }
            records.append(record)      #adding each dictionary to a list
        return records                  #giving the list back to the program
        
records = load_records("data.txt")
print(records)
# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#  keeping a running count of how many were OVER LIMIT, and
#  printing that once, after the loop ends.

for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status=check(value,limit)

    print_report(label, value, limit,difference, percent,status)


# =========================================================================
