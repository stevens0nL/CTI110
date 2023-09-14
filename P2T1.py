import matplotlib.pyplot as plt
import turtle

# TODO: Graph the real data


# New version 
data = [] # empty list

num_days = turtle.numinput("Input", "How many days?")
num_days = int(input("How many days? "))
for day in range(num_days):
  # print("Day", day, ":", end = "")
  label = "Day #" + str(day)
  today = turtle.numinput(label, "How many Pokemon?")
  data.append(today) # add it to the end of the list

# Put the daa in a list
# Print MAX and MIN3

print()
print("Best day:", max(data))
print("Worst day:", min(data))



# Collect data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokemon Data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()

total = 0
for num in data:
  total += num
average = total / num_days
print("Total:", total)
print("Average", average)