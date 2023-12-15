# P4HW2 - Salary Calculator
# 11/24/23 (LATE)
# LAILA STEVENSON
#

# VARIABLES 
done_value = "DONE"
keep_going = True
while keep_going:
  print("Enter DONE to finish.")
  employee_name = input("Name of employee: ")
  if employee_name == done_value:
    print("You have finished using Salary Calculator!")
    keep_going = False
    
  else:
    hours_worked = float(input("Hours worked this week: "))
    pay_rate = float(input("Employee pay rate: "))
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
    print("Gross pay:", gross_pay, "\n")