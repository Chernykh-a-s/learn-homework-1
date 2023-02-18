"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def sales(stock_sales):
  sum_sales = 0
  for sale in stock_sales:
    sum_sales += sale
  return sum_sales


def avg_sales(stock_sales):
  s_sales = 0
  for sale in stock_sales:
    s_sales += sale
  return s_sales / len(stock_sales)


for one_product in stock:
  product_avg = sales(one_product['items_sold'])
  print(f'Количество продаж {one_product["product"]}: {round(product_avg,1)}')

for one_product in stock:
  product_avg = avg_sales(one_product['items_sold'])
  print(f'Среднее количество продаж {one_product["product"]}: {round(product_avg,1)}')

store_sales = 0
for key in stock:
    for i in key['items_sold']:
        store_sales += i
print(f'Общее количество продаж составляет: {store_sales}')
print(f'Среднее количество продаж составляет: {store_sales/len(stock)}')

    