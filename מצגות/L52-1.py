import random

# פונקציות

# def hello():
#     print("Hello class")

# hello()

# def print_seven():
#     x = 7
#     return x

# a = print_seven()
# print(a)

# def seven_eleven():
#     x = 7
#     y = 11
#     return x, y

# var1, var2 = seven_eleven()
# print("{} {}".format(var1, var2))

# def speak():
#     word = "hi"
#     print(word)
# speak()
# print(word)

# הגדרת List

# my_list = [11, 'aaa', 35.6, True]

# print(my_list[0])

# for i in range(len(my_list)):
#     print(my_list[i], end = " ")

# print()

# for i in my_list:
#     print(i, end = " ")

# shopping_list = ['cheese', 'orange', 'salami', 'apples']

# if 'apples' in shopping_list:
#     print("Apples inside!")

# for i in shopping_list:
#     print(i, end = " ")

# print()
# shopping_list.append('milk')

# for i in shopping_list:
#     print(i, end = " ")

# print()
# shopping_list.pop(0)

# for i in shopping_list:
#     print(i, end = " ")

# print()
# shopping_list.sort()

# for i in shopping_list:
#     print(i, end = " ")

# my_sentence='Welcome to QA 2023 class'
# words = my_sentence.split(' ')

# print()
# for i in words:
#     print(i, "#", end = " ")

# הגדרת Dictionary

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in car:
    print(x, "=", car[x])

car["color"] = "white"

print()
for x in car:
    print(x, "=", car[x])

car.update({"year": 2000})

print()
for x in car:
    print(x, "=", car[x])