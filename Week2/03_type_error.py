# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:   #cannot compare a string and an integer
    print("OVER")
else:
    print("OK")
