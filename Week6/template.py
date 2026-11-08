"""
RECORD CHECK  -  my version
===========================

Name  :  Leane Madiye
Lane  :  Cyber 
Date  :  03-11-2026

Run it:   python template.py

import pandas as pd

# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("login_attempts.csv")  # replace with pd.read_csv("your_file.csv")
"""renaming the columns to match the ones required for Cyber lane and leave out region"""
df = df.rename(columns={
    "ip": "source_ip",              #ip becomes source_ip
    "failed": "failed_logins",      #failed becomes failed_attempts
    "attempts": "total_attempts"    #attempts becomes total_attempts
})
df = df[["source_ip", "failed_logins", "total_attempts"]]

# 2. Add a "percent" column: (value / limit) * 100.
df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else ("WARNING" if x >= 90 else "OK")
)
# 3. Print the DataFrame.

print(df)
print(df[df["status"] != "OK"])

#grouping by status, count, saving CSV and PNG chart
status_counts = df.groupby("status").size() #groupby("status")groups records according to their status
                                            #.size()counts how many records are in each group
print("\nCounts per status:")
print(status_counts)
df.to_csv("status_report.csv", index=False)

#saving one bar chart showing the counts per status
import matplotlib.pyplot as plt

status_counts.plot(kind="bar")

plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()

print("=" * 34)
