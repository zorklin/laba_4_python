#рядок
string = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
          "Donec quis turpis rhoncus, porttitor magna at, efficitur "
          "leo. Proin nec aliquam arcu. Lorem ipsum dolor sit amet, "
          "consectetur adipiscing morbi.")

#Функція обробки Федорченков Андрій. Функція переводить всі символи в
#верхній регістр, далі заміняє O на o, а потім розвертає кожне слово в рядку
def process_text_first(input_string):
    #верхній регістр
    change_str = input_string.upper()

    #заміна O на o
    change_str = change_str.replace('O', 'o')

    #розвертає кожне слово, знаки теж вважаються за частину слова
    change_str = ' '.join([word[::-1] for word in change_str.split()])

    #повертаємо результат
    return change_str




#викликаємо функцію
change_string = process_text_first(string)

#виводимо результат
print("Result:", change_string)

def process_text_second(input_string):
    __doc__ = '''Функція обробки Попов Максим.

        Функція перетворює кожне слово так, щоб всі вони починались великою літерою, а всі інші літери робить малими.
        Замінює пробіли нижнім підкресленням.
        Замінює літери верхнього регістра нижніми і навпаки.
        '''


    changed_string = input_string.title() #Верхній регістр першої літери кожного слова

    changed_string = changed_string.replace(" ", "_")  # Заміна пробіла символом "_"

    changed_string = changed_string.swapcase()  # Заміна малих літер великими і навпаки

    return  changed_string

#викликаємо функцію
change_string = process_text_second(change_string)

#виводимо результат
print("Result:", change_string)

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


change_string_1 = mesha(string)
#виводимо результат
print("Result mesha:", change_string_1)
