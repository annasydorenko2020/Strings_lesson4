# for i in range(5):
#     # print("Hello")
#     print(i, end="")
#
# print()
# for i in range(2, 5):
#     print(i, end=" ")
#
# print()
# for i in range(1, 5, 2):
#     print(i, end=" ")
#
# print()
# print()
# for i in range(1, 5, 1):
#     print(i, end=" ")
#
# print()
# for i in range(-1, 5, 2):
#     print(i, end=" ")
#
# print()
# start, end = 1, 10
# for i in range(start, end + 1):
#     print(i,end=" ")
#
# print()
# start, end = 1, 10
# for i in range(end, start - 1, -1):
#     print(i, end=" ")
#
# print()
# start, end = 1, 10
# for i in range(end, start - 1, -2):
#     print(i, end=" ")
#
# print()
# for value in 2, "hello", 2.5, "world", True:
#     print(value)
#
# print()
# for i in range(3):
#     print("hello")
#
# print()
# for _ in range(3):
#     print("sally")
import args

#######################

#показати на екрані всі прості чилас в діапазоні, вказаному юзером.
#просте число - це число, яке ділиться без залишку тільки на себе і на одиницю.
#напрю. три - це просте число, а чотири - ні.
#всі прості числа починаються з 2, бо все, що менше 2 - не вважається простим числом.

# print()
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# # for i in range(start, end+1):
# #     print(i)
# #
# # print()
# #якщо start number буде більше, ніж end number:
# # if start < end:
# #     for i in range(start, end+1):
# #         print(i)
# # else:
# #     for i in range(end, start - 1, -1):
# #але це не дуже добре, бо ми використовуємо дублювання коду, а цього треба уникати
# #тому використаєм інший алгоритм
#
# # if start > end:
# #     for i in range(start, end + 1):
# #         start, end = end, start
# # for i in range(start, end +1):
#
# for number in range(start, end +1):
#     if number < 2:
#         continue
#
#     is_simple = True
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_simple = False
#             break
#
#     if is_simple:
#         print(number, end=" ")
#
# print()

#################
#вивод на екран таблиці множення з використанням вкладених циклів для for та while
#v1.

# print()
# FROM = 1
# TO = 10
#
# for i in range(FROM, TO):
#     for j in range(FROM, TO):
#         print(i * j, end=" ")
#     print()
#
# #v2.
#
# print("\n")
# i = FROM
# while i < TO:
#     j = FROM
#     while j < TO:
#         print(i * j, end= " ")
#         j += 1
#     i += 1
#     print()

#######
#створення малюнків з символів за допомогою циклів
#v1.
# LENGTH = 5
# SYMBOL = '* '
#
# for i in range(1, LENGTH + 1):
#     print(SYMBOL * i)
#
# print()
#
# #v.2
#
# for i in range(1, LENGTH + 1):
#     for j in range(i):
#         print(SYMBOL, end="")
# print()
###############

# print()
# LENGTH = 5
# SYMBOL = '* '
#
# for i in range(1, LENGTH + 1):
#     for j in range(1, LENGTH + 1):
#         if (i < j and i < 5) or (i < j and i > 5 - 1 - j):
#     print(SYMBOL * i)
#
# print()

# LENGTH = 5
# SYMBOL = '* '
#
# for i in range(5, LENGTH - 1):
#     for j in range(i):
#         print(SYMBOL, end="")
# print()

#завдання 4 - Дано рядок. (зробити зрізи)

# message = "hello world"
# print(message)
#
# #як об'єднати слова у кілької рядках у один рядок\обне слово отримати:
#
# text = ("hello"
#         "world")
# print(text)
#
# #або
#
# text = "hello" \
#         "world"
# print(text)
#
# #raw строка - використовується як чорновик для внутрішніх нотаток, принцип - що ввели, те й побачили
#
# text = '''
# qwerty
#     abcrty
#         qwerty2
# '''
#
# print(text)
#
# #ще варіанти для виведення сирої строки
#
# path = r"C:\Users\admin\PycharmProjects\FastAPI_materials"
# print(path)
#
# #або
# path ="C:\\Users\\admin\\PycharmProjects\\FastAPI_materials"
# print(path)
#
# #використання ескейп послідовностей для модифікації візуального вигляда рядка
# print("hello, \"world\"\n\tfrom program")
#
# #функція формат
# dogs, cats, bats = 12, 15, 5
# result =f"Dogs {dogs} and cats {cats}"
# print(result)
#
# result = "Dogs {} and cats {}".format(dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {0}".format( dogs, cats)
# print(result)
#
# result = "Dogs {1} and cats {1}".format( dogs, cats)
# print(result)
#
# result ="Dogs {1} and cats {0} and bats {2}".format(dogs, cats, bats)
# print(result)
#
# #індекси та індексатори
# #індекс - це подрядковий номер елемента в масиві\ у колекції
# #[] - індексатори вказуються у таких скобках
# #індекси рахуються завжди з нуля.
#
# message = "hello world"
# print(message[0]) #вивели останній символ у рядку
# print(len(message)) #вивели кількість символів у рядку
# print(message[len(message) -1]) #вивели останній символ у рядку
# print(message[-1]) #альтернативне рішення для вивовду останнього символу у рядку і воно більш просте
# print(message[len(message) -2]) #вивели передостанній символ у рядку
#
# #string\ рядок - це immutable тип даних, ми не можемо його змінювати та звертатися до нього як до індекса
# name = "Petya"
# print(name)

#срезы або slices (це можливість получить подстрочку с индекса 1 по индекс 2)

# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])
# print(sentence[10:1:-1])
#
# print()
# name = "Vasya"
# surname = "Petrov"
# age = 33
# fullname = name + " " + surname + " " + str(age)
# print(fullname)
#
# #коли текст\рядок потрібно паписати кілька разів
# text = "Hello, world" * 3
# print(text)
#
# #коли треба поставити розділювач у тексті
# print("---" * 10)
#
# #для порівняння рідків (тут буде враховуватись сума букв у рядку з таблиці ASCII Table)
#
# a1 = "abc"
# a2 = "abs"
#
# if a1 > a2:
#     print(a1)
# else:
#     print(a2)
#
# #якщо треба отримати код або перевести цифру у символ у ASCII Table
#
# print(ord("A"))
# print(chr(98))


#Task_1:
# message = "Mr.Tom takes bus123"
# print(message)
# alpha,message=0,"Mr.Tom takes bus123"
# for i in message:
#     if (i.isalpha()):
#         alpha+=1
# print("Number of digits", len(message)-alpha)
# print("Number of letters", alpha)
#
# ########
#
# print()
# message = "highway666"
# print(message)

# initialized value
# total_digits = 0
# total_letters = 0

# iterate through all characters
# for s in message:
#
#         if s.isnumeric():
#                 total_digits += 1
#
#         else:
#                 total_letters += 1
#
# print("Total letters: ", total_letters)
# print("Total numbers: ", total_digits)

#################

# #Task2
#
# message = "My friend is fine, but fine is fine for him"
# print(message)
#
# result = message.count("fine")
# print(result)
#
# ##
#
# message = "Why I see 111, while you see 1122 instead"
# print(message)
#
# result = message.count("1")
#
# print(result)

####

#Task3
#вивести з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше

# print()
# text = 'summer is hot, summer is sunny'
# result = text.replace('summer', 'winter')
# print(result)
#
# print()


#Task4

# sentence = "Welcome to San Francisco!"
# print(sentence[:])
# # #виведіть третій символ цього рядка
# # print(sentence[0:])
# print(sentence[2])
#
# #виведіть передостанній символ цього рядка
# print(sentence[-2])
# #
# #виведіть перші п'ять символів цього рядка
# print(sentence[0:6])
# #
# #виведіть весь рядок, крім двох останніх символів
# print(sentence[:-2])
#
# #виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
# # \n тому символи виводяться з першого)
# print(sentence[0:25:2])
#
# #У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# print(sentence[1:25:2])
#
# #виведіть усі символи у зворотному порядку
# print(sentence[::-1])
#
# #виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього
#
# print(sentence[::-2])
# #
# #виведіть довжину цього рядка
#
# setence = 'Welcome to San Francisco!'
# print(len(sentence))

#Приклади з різними функціями

# #isalpha() - повертає True, якщо рядок складається лише з алфавітних символів
# text = "hello woRLD"
# print(text.isalpha())
#
# #islower() - повертає True, якщо рядок складається лише із символів у нижньому регістрі (маленькі букви)
# print(text.islower())
#
# #isupper() - повертає True, якщо рядок складається лише із символів у верхньому регістрі (великі букви)
# print(text.isupper())
#
# #isdigit() - повертає True, якщо всі символи рядка - цифри (тобто рядок цифр 1,2,3,4...).
# print(text.isdigit())
#
# #isnumeric() - повертає True, якщо рядок є числом (напр. число 123), вона частіше використовується.
# print(text.isnumeric())
#
# #startswith(str) - повертає True, якщо рядок починається з підрядка.
# print(text.startswith("hello"))
#
# #endswith(str) - повертає True, якщо рядок закінчується на підрядок.
# print(text.endswith("D"))
#
# #lower() - перекладає рядок у нижній регістр (весь рядок буде написано маленькими буквами)
# print(text.lower())
#
# #upper() - перекладає рядок у верхній регістр (весь рядок буде написано великими буквами)
# print(text.upper())
#
# #title() - початкові символи всіх слів у рядку перекладаються у верхній регістр (кожне слово буде написано з великої літери)
# print(text.title())
#
# #capitalize() - перекладає у верхній регістр першу літеру тільки першого слова рядка.
# print(text.capitalize())
#
# #приклад для вдосконалення фіо юзера, які він неправильно заповнив
#
# fio = input("Enter fio: ").title()
# print(fio)

#lstip() - видаляє початкові пробіли з рядка (left strip)
# text = "  hello woRLD  "
# print(text)
# print(text.lstrip())

#rstip() - видаляє кінцеві пробіли з рядка (right strip)
# text = "  hello woRLD  "
# print(text)
# print(text.rstrip())

#stip() - видаляє початкові та кінцеві пробіли з рядка (її використовують найчастіше)
# text = "  hello woRLD  "
# print(text)
# print(text.strip())

#ljust(width) - якщо довжина рядка менша за параметр width, то праворуч від рядка додаються пробіли
# щоб доповнити значення width, а сам рядок вирівнюється по лівому краю

# text = "hello world"
# print(text)
# print(text.ljust(20))

#rjust(width) - якщо довжина рядка менша за параметр width, то зліва від рядка додаються пробіли
# щоб доповнити значення width, а сам рядок вирівнюється праворуч

# text = "hello world"
# print(text)
# print(text.rjust(20))

#center(width) - якщо довжина рядка менша за параметр width, то зліва і справа від рядка додаються пробіли
# щоб доповнити значення width, а сам рядок вирівнюється по центру
# text = "hello world"
# print(text)
# print(text.center(20))

#find(str[, start[, end])   - функція, яка дозволяє знайти якесь значення, вона повертає індекс підрядка у рядку.
# Якщо підрядок не знайдено, то повертає число -1.
#find шукає зліва направо, rfind шукає справа наліво.
# text = "hello world"
# print(text.find("hello")) #0, бо він знайшов hello, починаючи з нульового індекса \ з самого початку
# print(text.find("l"))   #2, він знайшов літеку, починаючи з другого індекса
# print(text.rfind("l"))  #9, він знайшов літеку, починаючи з права на місці 9го індекса.

#якщо ми хочемо задати конкрентний індекс, з якого починати пошук (а не шукати тільки справа, або зліва)
# # то ми можемо використувати наступную функцію
# first_found_index = text.find("l")  #(ми тут ставимо індекс першої літери l зліва)
# print(text.find("l", first_found_index +1 ))
#(почни шукати букву l, починаючи з індекса, він поверте індекс 3)

# print(text.find("p")) #ми просимо знайти p у слові hello world, його не існує, тому отримуємл -1

#приклади пошуку
#v1. - треба знайти всі індекси, по яким у тексті зустрічаються літери l.
#такий варіант рішення краще використовувати, коли треба працювати з індексами\порядковими номерами
# for i in range(len(text)):
#     if text[i] == "l":
#         print(i)  #2, 3, 9 індекси виводить у консоль

#v2.
# index = 0
#
# for letter in text: #такий варіант краще для рішень, коли треба працювати зі значеннями у коллекціях,
# а не з індексами \ порядковими номерами у коллекціях
#     if letter == "l":
#       print(index)
#     index += 1 #результат буде такий самий 2, 3, 9 індекси виводить у консоль

#replace(old, new[, num]) - замінює в рядку один підрядок на інший
# text = "hello world hello"
# print(text)

#v1. - тут всі слова будуть замінені
# text = text.replace("hello", "goodbye")
# print(text)

#v2. - тут буде замінено слово тільки один раз
# text = text.replace("hello", "goodbye", 1)
# print(text)

#щоб порахувати кількість якогось символу у тексті
# text = "qqqqqqq"
# print(text.count("q"))






#Task5
#Реалізуйте наступну функціональність у тексті:
#Змінити текст таким чином, щоб кожне речення починалися з великої літери;

text = "ask him to come home. he should listen to you."
#
print()
search_item = ". "
current_index = text.find(search_item)
print(current_index)
#
print()
first_sentence = text[:current_index + len(search_item)]
second_sentence = text[current_index + len(search_item):]

#
print()
print(first_sentence)
print(second_sentence)
#
print()
final_sentence = first_sentence.capitalize() + second_sentence.capitalize()
print(final_sentence)


#Порахуйте скільки разів цифри зустрічаються у тексті;

print()
print()
text = "my friend is sick for 11 or 13 days already"
print(text)

digit=0
for i in text:
   if i.isdigit():
      digit=digit+1
   else:
      pass
print("Total digits:", digit)

print()

#Порахуйте скільки разів розділові знаки зустрічаються в тексті;
print()

text = "Morning, Sam!!! Hof do you feel today?? I've seen you yesterday, you looked sick...."
print(text)
print(text.count("!"))
print(text.count("?"))
print(text.count("."))
print(text.count(","))


#Порахуйте кількість знаків оклику в тексті.
print()
text = "He should be here!!! He promised! This is not possible!!!!!!!!!"
print(text)
print(text.count("!"))

print()
print()

#Tack6
#намалювати фігури, заповнені зірочками

stars_count = 5
spaces_count = 0

#A

# for i in range(5):
#    for j in range(spaces_count):
#       print(" ", end=" ")
#    for j in range(stars_count):
#       print("*", end=" ")
#
#    stars_count -= 1
#    spaces_count += 1
#
#    print()

#Б

# for i in range(5):
#     for j in range(i+1):
#         print("* ", end="")
#     print()


#В

# for i in range(5):
#    for j in range(spaces_count):
#       print(" ", end=" ")
#    for j in range(stars_count):
#       print(" * ", end=" ")
#
#    stars_count -= 1
#    spaces_count += 1
#
#    print()


#Г - не розумію, як його зробити

#Д
# for i in range(11):
#    for j in range(spaces_count):
#       print("  ", end="")
#    for j in range(stars_count):
#       print("* ", end="")
#    for j in range(spaces_count):
#       print("  ", end="")
#    if i >= 5:
#       stars_count += 2
#       spaces_count -= 1
#    else:
#       stars_count -= 2
#       spaces_count -= 1
#    print()

#Е - не знаю, як його зробити

#Ж
# rows = 7
# for i in range(0, 7):
#    for j in range(0, i + 1):
#       print("* ", end="")
#    print("\r")
# for i in range(7, 0, -1):
#    for j in range(0, i + 1):
#       print("* ", end="")
#    print("\r")

#З - не знаю, як його зробити


#И

# stars_count = 5
# spaces_count = 0
#
# for i in range(5):
#    for j in range(stars_count):
#       print("* ", end=" ")
#    for j in range(spaces_count):
#       print(" ", end="")
#
#    stars_count -= 1
#    spaces_count += 1
#
#    print()

#К
# for i in range(6):
   # for j in range(spaces_count):
   #    print(" ", end="   ")
   # for j in range(stars_count):
   #    print("* ", end="")
   #
   # spaces_count -= 1
   # stars_count += 1
   #
   # print()



