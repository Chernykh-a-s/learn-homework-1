"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'Как дела?': 'Хорошо!', 
                        'Что делаешь?': 'Программирую', 
                        'Как погода?': 'Ветренно..',
                        'Как тебя зовут?': 'Лёша',
                        'Какое твоё любимое блюдо?': 'Пельмени',
} 


def ask_user(answers_dict):
    while True:
        ask_question = input('Задайте вопрос: ')
        if ask_question == 'Как дела?':
            print(questions_and_answers[ask_question])
        elif ask_question == 'Что делаешь?':
            print(questions_and_answers[ask_question])
        elif ask_question == 'Как погода?':
            print(questions_and_answers[ask_question])
        elif ask_question == 'Как тебя зовут?':
            print(questions_and_answers[ask_question])
        elif ask_question == 'Какое твоё любимое блюдо?':
            print(questions_and_answers[ask_question])
        break    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
