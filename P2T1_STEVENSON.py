import matplotlib.pyplot as plt

# TODO: Graph the real data
print("Enter Pokemon data:")
print("Day 1:", end = "")
day1 = int(input())
print("Day 2:", end = "")
day2 = int(input())
print("Day 3:", end = "")
day3 = int(input())

# Put the daa in a list
data = [day1, day2, day3]

# Collect data
fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title("Pokemon Data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()


