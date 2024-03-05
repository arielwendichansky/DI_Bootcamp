#Exercise_1
"""
word = input("Give me a word: ")
my_dic = {}
for index,letter in enumerate(word):
    letter_str = str(letter)
    if letter_str in my_dic:
        my_dic[letter_str].append(index)
    else:
        my_dic[letter_str] = [index]

print(my_dic)

print('>' *30)
#Exercise_2
"""
products = []
prices = []
my_cart =[]
combo = {}
def valuestring (price):
    return float(price.replace('$','').replace(',',''))

wallet = float(input("how much money you have in your wallet? "))

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2",
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

for x,y in items_purchase.items():
    products.append(x)
    prices.append(valuestring(y))

combo = dict(zip(products,prices))

for product, price in combo.items():
    if wallet >= float(price):
        my_cart.append(product)
        wallet -= float(price)
        my_cart.sort()
print(f"This are the products in your cart {my_cart}")



if len(my_cart) == 0:
        print("You don't have enough money to buy a product")




