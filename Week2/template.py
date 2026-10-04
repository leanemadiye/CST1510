"""
RECORD CHECK  -  my version
===========================

Name  :Leane
Lane  :Cyber 
Date  :02-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#     the first is TEXT      
#     the second is a NUMBER
#     the third  is a NUMBER 

label = input("enter label:") 
value = float(input("enter value:")) 
limit = float(input("enter limit:")) 


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit
percent = (value/limit) *100
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
if percent >=100:
    status=("OVER LIMIT")
elif percent >=80:
    status=('WARNING')
else:
    status=('OK')

    

# ========== OUTPUT===========
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" value          :{value:>10.2f}")
print(f" limit          :{limit:>10.2f}")
print(f" difference     :{difference:>10.2f}")
print(f" percent        :{percent:>10.2f}%")
print(f" status         :{status}")


print("=" * 34)


# ==========================DONE
