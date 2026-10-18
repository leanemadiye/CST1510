# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

with open("records.txt","r") as f:  #there was an error because there was no mode
    print(f.read())
