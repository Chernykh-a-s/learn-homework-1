"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user(how_are_you):
    while True:
      how_are_you = input('Как дела? ')
      if how_are_you == 'Хорошо':
        break
    
    
if __name__ == "__main__":
    msg1 = hello_user('Привет')
