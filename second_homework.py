# Логування користувача
'''
user_full_name = input("Введіть ваше повне ім'я через пробіл: ")

if user_name:
    separate_words = user_name.split()    # Метод split() розділяє рядок на окремі слова.
    name_part = separate_words[0]
    surname_part = separate_words[1]
    print(f'Ініціали: {name_part[0]} {surname_part[0]}')
else:
    print("Помилка: введіть реальне ім'я.")
'''


# Маскування email
'''
user_email = input('Заповніть інформацію про свою пошту: ')

if user_email and user_email.endswith((".com", ".org")):  # Метод endswith() перевіряє чи закінчується рядок на вибраний суфікс.
    separate_parts = user_email.split('@')
    main_name = separate_parts[0]
    domain = separate_parts[1]
    camouflage = main_name[0] + '*' * (len(main_name)-2) + domain[-1]
    print(f'{camouflage}@{domain}')
else: 
    print('Помилка: введіть реальну ел. пошту.')
'''

# Додавання унікального значення
'''
registered_values_list = [1, 2, 3, 4, 5]

add_new_number = int(input('Яке число ви хочете додати? '))
print(f'Ось як виглядає список до змін: {registered_values_list}')

if add_new_number in registered_values_list: 
    print(f'Це число вже існує, залишаємо як є: {registered_values_list}')
else: 
    registered_values_list.append(add_new_number)
    print(f'Змінили список, тепер він виглядає так: {registered_values_list}')
'''

# Аналіз тегів
'''
first_user_tags = set()
second_user_tags = set()

first_user_interests = input('Теги користувача 1: ').split(',')
second_user_interests = input('Теги користувача 2: ').split(',')

first_user_tags.update(first_user_interests)
second_user_tags.update(second_user_interests)

print('Спільні: ', first_user_tags & second_user_tags)
print('Унікальні: ', first_user_tags ^ second_user_tags)
'''

# Обробка рядка з числами
'''
string_of_values = input('Введіть, будь ласка, числа через пробіл: ').split()

if len(string_of_values) >= 3 and string_of_values[0].isdigit() and string_of_values[1].isdigit() and string_of_values[0].isdigit():    # Метод isdigit() перевіряє, чи є значення числом. 
    first_three_numbers_sum = int(string_of_values[0]) + int(string_of_values[1]) + int(string_of_values[2])
    print(f'Сума трьох чисел: {first_three_numbers_sum}')
else:
    print("Помилка: одне значення або всі не є числами.")
'''