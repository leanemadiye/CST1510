"""
RECORD CHECK  -  my version
===========================

Name  :Leane
Lane  : Cyber     
Date  :29-09-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.




label = input("please enter your label")
first = float(input("please enter the first number")) 
second =float(input("please input the second number")) 


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#     difference : calculating how far the first is from the second
#     percent    : calculating the first as a percentage of the second



difference = first -second
percent = (first/second) *100


# =================================================================== OUTPUT
# 3. Print the report.

#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own

#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"label: {label}")
print(f"First: {first:>10.2f}")
print(f"Second: {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"percente: {percent:>10.2f}%")

print("Status: Report completed successfully!")


print("=" * 34)
