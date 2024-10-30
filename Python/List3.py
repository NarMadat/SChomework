import random

names_input = input("Enter names: ")
names_list = names_input.split()
length = len(names_list)

x = random.randint(0, length - 1)

print(f"{names_list[x]} will pay")
