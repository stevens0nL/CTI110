# CTI 110
# P4T2
# Time Card
# LAILA STEVENSON
# 11/24/23 (LATE)

# This program will act like a time card reader,
# adding up each day's hours to get the total.

# Version 1 - uses numbers for days
# change line below if it's a 7 day week
DAYS_IN_WEEK = 5
totalHours = 0  # the total starts at zero

print("Please enter your hours worked.")

for day in range(DAYS_IN_WEEK):
    print(f"Hours for day {day+1}: ", end="")
    hoursToday = float(input())
    while hoursToday < 0 or hoursToday > 24:  # input validation
        print("Please enter a valid value between 0 and 24")
        hoursToday = float(input())
    totalHours += hoursToday  # add to running total

# print the total
print(f"You worked a total of ${totalHours:.2f} hours this week.")

# print the average
avgHours = totalHours / DAYS_IN_WEEK
print(f"For an average of ${avgHours:.2f} hours per day.")