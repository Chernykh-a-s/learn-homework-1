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
def main():
    total_product_sales = 0
    sales = 0
    for product in stock:
        product_sales = sum(product['items_sold'])
        total_product_sales += product_sales
        print(f'Количество продаж {product["product"]}: {round(product_sales,1)}')
        avg_product_sales = sum(product['items_sold']) / len(product['items_sold'])
        print(f'Среднее количество продаж {product["product"]}: {round(avg_product_sales,1)}')
        sales += len(product['items_sold'])
    
    total_avg_sales = total_product_sales / sales
    print(f'Общее количество продаж всех товаров: {total_product_sales}')
    print(f'Среднее количество продаж всех товаров: {round(total_avg_sales, 1)}')

if __name__ == "__main__":
    stock = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]  
    main()
  
    