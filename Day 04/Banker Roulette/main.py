import random

name_list = input('Enter the list of names ')
arrey_of_names = name_list.split(', ')
random_number_picker = random.randint(0, len(arrey_of_names) - 1)
print(f"{arrey_of_names[random_number_picker]} will pay the bill today")
