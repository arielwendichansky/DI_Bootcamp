# #Exercise_1
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dic = dict(zip(keys,values))
# print(dic)
#
# print(">"*30)
# #Exercise_2
#
# family = {}
# ticket = 0
# total_price = 0
# ages = []
#
#
# total_ticket = int(input("Enter the number of tickets you want to buy: "))
#
# for i in range(total_ticket):
#     key = input("Enter name: ")
#     value = int(input("Enter age: "))
#     family[key] = value
#
# print(family)
#
# while ticket != total_ticket:
#     for name,age in family.items():
#         ages.append(age)
#         ticket = int(len(ages))
#         if age <= 3:
#             price = 0
#             print(f"{name} has to pay ${price}")
#         elif 3 < age <= 12:
#             price = 10
#             print(f"{name} has to pay ${price}")
#             total_price += price
#         elif age > 12:
#             price = 15
#             print(f"{name} has to pay ${price}")
#             total_price += price
#
#
# print(f"The total price to pay is ${total_price}")
#
# print(">"*30)
# #Exercise_3
#
# brand = {}
# clothes = ["men", "women", "children", "home"]
# competitors = ["Gap", "H&M", "Benetton"]
# brand["name"]= "Zara"
# brand["creation_date"]= 1975
# brand["creator_name"]= "Amancio Ortega Gaona"
# brand["type_of_clothes"]= clothes
# brand["international_competitors"]= competitors
# brand["number_stores"]= 7000
#
# countries = {}
# countries_string = ''' France: blue,
#                         Spain: red,
#                         US: (pink, green)'''
# countries_color = [all.strip(',: ') for all in countries_string.split('\n')]
# for item in countries_color:
#     country, color = item.split(': ' )
#     countries[country] = color
#
# brand["major_color"]= countries
# print(brand)
# # ex3
# brand["number_stores"] = 2
# print(brand)
# #Ex4
# print( f" Hello, we are {list(brand.values())[0]}, a company with {list(brand.keys())[5]} of {str(list(brand.values())[5])}")
# #Ex5
# brand["country_creation"] = "Spain"
# print(brand)
# #Ex6
# if "international_competitors" in brand:
#     competitors.append('Desigual')
# print(brand)
# #Ex7
# del brand["creation_date"]
# print(brand)
# #Ex8
# print(list(brand["international_competitors"])[-1])
# #Ex9
# print(brand['major_color']['US'])
# #Ex10
# print(len(list(brand.keys())))
# #Ex11
# print(brand.keys())
# #Ex12
# more_on_zara = {'creation_date': 1975,
# 'number_stores': 10000}
#
# brand.update(more_on_zara)
#
# #Ex13
# print(brand)
# #Ex14
# #The value number of stores is updated
#
# print(">"*30)
#Exercise_4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
for item in enumerate(users):
    print(item)
disney_users_A = {key: users for (users,key) in enumerate(users)}
print(disney_users_A)

disney_users_B = {key: users for (key,users) in enumerate(users)}
print(disney_users_B)

users.sort()
disney_users_C = {key: users for (users,key) in enumerate(users)}
print(disney_users_C)

names_with_i = {key: users for (users,key) in enumerate(users) if 'i' in key}
print(names_with_i)

start_with = {key: users for (users,key) in enumerate(users) if key[0] in ['M','P']}
print(start_with)
