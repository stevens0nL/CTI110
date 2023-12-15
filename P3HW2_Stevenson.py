# P3HW2 - Salary
# 11/24/23 (LATE)
# LAILA STEVENSON
#

# 1. Ask user to enter name of employee
# 2. Ask user to enter number of hours the employee worked this week
# 3. Ask user to enter employee's pay rate
employee_name = input("Enter name of employee: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# 4. Evaluate if employee has worked overtime
# 5. Calculate the amount owed to employee for overtime hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = 1.5 * pay_rate * overtime_hours
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("--------------------------------")
print("Employee name:     ", employee_name)
print(" ")
print("Pay Rate:", pay_rate)
print("Hours Worked:", hours_worked)
print("OverTime:", overtime_hours)
print("OverTime Pay:", overtime_pay)
print("RegHour Pay:", regular_pay)
print("Gross pay:", gross_pay)
