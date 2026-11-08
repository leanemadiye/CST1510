"""
RECORD CHECK  -  my version
===========================

Name  :  Leane Madiye
Lane  :  Cyber 
Date  :  05-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Writing a parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.


def parse_line(raw_line): #creating our function
    """Parse a messy raw security log line into a structured dictionary with converted values"""

    line = raw_line.strip().lower()
    parts = line.split(",") #splitting the line into parts using  a comma
    data ={}

    records = {} #an empty dictionary

    for piece in parts:
        if "=" in piece:
            key, val = piece.split("=", 1)
            cleaned_val = val.strip()
            try:
                if "." in cleaned_val:
                    data[key.strip()] = float(cleaned_val)
                else:
                    data[key.strip()] = int(cleaned_val)
            except ValueError:
                data[key.strip()] = cleaned_val

        
    return data

def status_of(data):
    """Evaluates security evnt metrics and return a status (FLAGGED, WARNING, or OK)"""
    attempts = data.get("attempts", 0)
    result = data.get("result", "").upper()

    if attempts >= 10 and result == "FAILED":
        return "FLAGGED"
    elif result == "FAILED":
        return"WARNING"
    else:
        "OK"

# 2.messy records  5, deliberately varied in spacing and case.   
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"

#messy records
raw_records = [
    "SRC=10.0.0.5, ATTEMPTS=12, RESULT=FAILED",
    "src=190.166.1.10, attempts=3 , results=success",
    "SRC=170.10.1.3 , ATTEMPTS=8 , RESULT=FAILED"
    "src=10.1.0.8, ATTEMPTS=2,RESULT=SUCCESS",
    "SRC=182.100.1.10 , attempts=16 , result=failed"
]  

#parse and report on every record
total_records = 0
flagged_count = 0

print("---Cybersecurity Log Analysis---")
for raw_line in raw_records:
    if not raw_line.strip:
        continue

    total_records += 1
    parsed =parse_line(raw_line)
    status = status_of(parsed)

    if status in ["FLAGGED", "WARNING"]:
        flagged_count += 1

    print(f"Record: {parsed} -> Status: {status}")

print("\n--- Summary ---")
print(f"Total records: {total_records}")
print(f"How many flagged: {flagged_count}")
