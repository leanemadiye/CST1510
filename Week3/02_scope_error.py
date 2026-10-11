# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    print(status)       #the name status was not defined so we moved the print statement inside the function
          
          
check(87, 100)


