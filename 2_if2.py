"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        if str1 == str2:
            return 1
        if len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
        elif len(str1) < len(str2):
            return 4
    else:
        return 0

    
if __name__ == "__main__":
    msg1 = main('привет', 'привет')
    msg2 = main('при', 'привет')
    msg3 = main('при', 'learn')
    msg4 = main(1, 'learn')
    print(msg1, msg2, msg3, msg4, sep = '\n')
 
