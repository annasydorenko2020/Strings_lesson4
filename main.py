#Task_1:
message = "Mr.Tom takes bus123"
print(message)
alpha,message=0,"Mr.Tom takes bus123"
for i in message:
    if (i.isalpha()):
        alpha+=1
print("Number of digits", len(message)-alpha)
print("Number of letters", alpha)
#
# ########
#
print()
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

# #Task2
#
message = "My friend is fine, but fine is fine for him"
print(message)

result = message.count("fine")
print(result)
#
# ##
#
message = "Why I see 111, while you see 1122 instead"
print(message)

result = message.count("1")

print(result)

####

#Task3
#вивести з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше

print()
text = 'summer is hot, summer is sunny'
result = text.replace('summer', 'winter')
print(result)

print()


#Task4

sentence = "Welcome to San Francisco!"
print(sentence[:])
# # #виведіть третій символ цього рядка
# # print(sentence[0:])
print(sentence[2])
#
# #виведіть передостанній символ цього рядка
print(sentence[-2])
# #
# #виведіть перші п'ять символів цього рядка
print(sentence[0:6])
# #
# #виведіть весь рядок, крім двох останніх символів
print(sentence[:-2])
#
# #виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,
# # \n тому символи виводяться з першого)
print(sentence[0:25:2])
#
# #У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
print(sentence[1:25:2])
#
# #виведіть усі символи у зворотному порядку
print(sentence[::-1])
#
# #виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього
#
print(sentence[::-2])
# #
# #виведіть довжину цього рядка
#
setence = 'Welcome to San Francisco!'
print(len(sentence))



