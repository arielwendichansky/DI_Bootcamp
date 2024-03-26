# Exercise 1 : Cars
car = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
list_cars = car.split(',')  # Convert it into a list using Python
print(list_cars)
print(f"There are {len(list_cars)} different car brands in the list")
list_cars.sort(reverse=True)  # Print the list of manufacturers in reverse/descending order
print(list_cars)

o_cars = [car for car in list_cars if 'o'in car]  # Find out how many manufacturers’ names have the letter ‘o’ in them.
print(f"There are {len(o_cars)} brands where the letter 'o' is in it's name")

not_i_cars = [car for car in list_cars if 'i' not in car]  # Find out how many manufacturers’ names do not have the letter ‘i’ in them.

print(f"There are {len(not_i_cars)} brands where the letter 'i' is not in it's name")


list_cars.sort()
reversed_cars = [car.strip()[::-1] for car in list_cars]  # Strip whitespace from each brand and reverse letters
for car in reversed_cars:
    print(car)


