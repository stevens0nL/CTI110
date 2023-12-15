# Stevenson
# 10/24

def main():
  print("Hllo World")
  burger = 4.999
  print_money(burger)
  print_money(12)
  print_money(0.3)
  # main() ends

# ther functions
def print_money(amount):
  print("$", format(amount, ".2f"), sep="")

#now start program
main()