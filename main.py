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

# message = "ask him to cook 12 pancakes"
# print(message)
# i = number
# for i in range(message):
#         print(number)

#Task_1:
message = "Mr.Tom takes bus123"
print(message)
alpha,message=0,"Mr.Tom takes bus123"
for i in message:
    if (i.isalpha()):
        alpha+=1
print("Number of digits", len(message)-alpha)
print("Number of letters", alpha)

########

message = "highway666"
print(message)

# initialized value
total_digits = 0
total_letters = 0

# iterate through all characters
for s in message:

        if s.isnumeric():
                total_digits += 1

        else:
                total_letters += 1

print("Total letters: ", total_letters)
print("Total numbers: ", total_digits)

#################



