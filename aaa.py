products = ['Апельсини', 'Банани']
products_list = list()

print('Продукти в наявності:')
number = 1
for product in products:
    print(number, product)
    number +=1

print('Постачання продуктів')
print('Введіть назву продукту або 0 для виходу')
while True:
    product = input()

    if product == '0':
        break
    else:
        products.append(product)

products_new = ['Картопля', 'Цибуля']
products.extend(products_new)
print('Продукти в наявності:')
number = 1
for product in products:
    print(number, product)
    number +=1
print('Продаж продуктів за назвою:')
print('Введіть назву продукту, який бажаєте купити:')
product = input()
products_sold = list()
if product in products:
    products.remove(product)
    products_sold.append(product)
    print('Дякуємо за покупку')
else:
    print('Вказаного продукту більше немає')

print('Продаж продуктів за номером:')
print('Введіть номер продукту, який бажаєте купити')
product_index = int(input())
if 0<=product_index<len(product):
    product = products.pop(product_index)
    products_sold.append(product)
    print('Ви купили', product)
    print('Дякуємо за покупку')
else:
    print('Неправильно вказанний номер')

print('Оновлення продукту:')
product_index = products.index('Картопля')
products.insert(product_index,'Картопля молода')

print('Продукти на кінець дня')
products_sold.reverse()

for product in products:
    print(product)