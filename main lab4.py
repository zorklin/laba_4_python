#рядок
string = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
          "Donec quis turpis rhoncus, porttitor magna at, efficitur "
          "leo. Proin nec aliquam arcu. Lorem ipsum dolor sit amet, "
          "consectetur adipiscing morbi.")

#Функція обробки Федорченков Андрій. Функція переводить всі символи в
#верхній реестр, далі заміняє O на !, а потім розвертає кожне слово в рядку
def process_text_first(input_string):

    #верхній регістр
    change_str = input_string.upper()

    #заміна O на o
    change_str = change_str.replace('O', 'o')

    #розвертає кожне слово, знаки теж вважаються за частину слова
    change_str = ' '.join([word[::-1] for word in change_str.split()])

    #повертаємо результат
    return change_str
#Функція обробки Меша Павло. Функція визначае довжину рядка,
# кількість літер P у рядку та розбивае рядок за пробілом.
def mesha(string):

    # Визначимо довжину рядка
    l = len(string)
    print("Довжина рядка :", l)

    # Підрахуємо кількість літери P у рядку
    l1 = string.count('P')
    print("Кількість літери P у рядку :", l1)

    # Розіб'ємо рядок за пробілом
    l2 = string.split(' ')

    return l2

#викликаємо функцію
change_string = process_text_first(string)

change_string_1 = mesha(string)

#виводимо результат
print("Result:", change_string)

print(change_string_1)