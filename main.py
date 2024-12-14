# 4 oy 8 dars uyga vazifasi

# 1 vazifa

# import math
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def ab(number):
#     return f"{number}: {math.pow(number, 2)}"
# a = map(ab, numbers)
# b = list(a)
# print(b)


#--------------------------------------------------------------------------------------

# 2 vazifa
#
# text = ["A", "a", "B", "b", "C", "c", "D", "d"]
# def ab(harf: str):
#         if harf.isupper():
#             return harf
# a = filter(ab, text)
# print(list(a))


#--------------------------------------------------------------------------------------

# 3 vazifa

# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# def ab(number: str):
#     if number.startswith("+998"):
#         print(f"{number} O'zbek no'meri !")
#     elif number.startswith("+7"):
#         print(f"{number} Rassiya no'meri !")
#     elif number.startswith("+1"):
#         print(f"{number} Amerika no'meri !")
#     else:
#         print("Bunday no'meri hali mavjud emas !")
# a = map(ab, phone_numbers)
# b = list(a)


#--------------------------------------------------------------------------------------

# 4 vazifa

# names = ['alfred', 'tabitha', 'william', 'arla']
# def ab(nema: str):
#     return nema.title()
# a = map(ab, names)
# print(list(a))


#--------------------------------------------------------------------------------------

# 5 vazifa

# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# into = []
# def ab(ball):
#     global into
#     if ball > 75:
#         into.append(ball)
# a = map(ab, scores)
# b = list(a)
# print(into)


#--------------------------------------------------------------------------------------

# 6 vazifa

# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palindromes = list(filter(lambda word: word.lower() == word.lower()[::-1], words))
# print(palindromes)


#--------------------------------------------------------------------------------------

# 7 vazifa

# text = ['apple', 'banana', 'cherry']
# def ab(soz: str):
#     return len(soz)
# a = map(ab, text)
# print(list(a))


#--------------------------------------------------------------------------------------

# 8 vazifa

# a =  ['orange', 'lemon', 'pineapple']
# b = ['apple', 'banana', 'cherry']
# def ab(soz1: str, soz2:str):
#     return soz1 + soz2
# c = map(ab, a, b)
# print(list(c))


#--------------------------------------------------------------------------------------

# 9 vazfa

# a = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# b = ["Sobir", "Bakir", "Jalil", "Toxir"]
# def ab(soz1: str, soz2: str):
#     return soz1 + soz2
# c = map(ab, a, b)
# d = list(c)
# print(d)


#--------------------------------------------------------------------------------------

# 10 vazifa

# def element_count_with_filter(lst, element):
#     filtered_elements = filter(lambda x: x == element, lst)
#     return len(list(filtered_elements))
# royxat = [1, 2, 3, 4, 2, 3, 2, 5]
# element = int(input("Raqam kiriting: "))
# natija = element_count_with_filter(royxat, element)
# print(f"{element} soni ro'yxatda {natija} marta takrorlangan.")


#--------------------------------------------------------------------------------------

# 11 vazifa

# I1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# I2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# umumiy_elementlar = list(filter(lambda x: x in I2, set(I1)))
# print("Umumiy elementlar:", umumiy_elementlar)


#--------------------------------------------------------------------------------------

# 12 vazifa

# programming_languages = [
#     'Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal',
#     'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo',
#     'Swift', 'Php'
# ]
# toq_tartibdagi_elementlar = list(filter(lambda x: programming_languages.index(x) % 2 == 0, programming_languages))
# print("Toq tartibdagi elementlar:", toq_tartibdagi_elementlar)


#--------------------------------------------------------------------------------------

# 13 vazifa

# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal',
#                          'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# start_index = programming_languages.index('Basic')
# sub_list = programming_languages[start_index:]
# result = list(map(lambda x: x, sub_list))
# print(result)


#--------------------------------------------------------------------------------------

# 14 vazifa

# from collections import namedtuple
# Talaba = namedtuple('Talaba', ['ism', 'guruh', 'baho'])
# talabalar = [
#     Talaba(ism='Ali', guruh=101, baho=92.5),
#     Talaba(ism='Zaynab', guruh=102, baho=95.0),
#     Talaba(ism='Rustam', guruh=103, baho=87.0),
#     Talaba(ism='Madinabonu', guruh=104, baho=89.5),
#     Talaba(ism='Jasur', guruh=105, baho=94.0)
# ]
# eng_yuqori_baho_talaba = max(talabalar, key=lambda talaba: talaba.baho)
# print("Eng yuqori o'rtacha bahoga ega talaba:")
# print(f"Ismi: {eng_yuqori_baho_talaba.ism}")
# print(f"Guruh: {eng_yuqori_baho_talaba.guruh}")
# print(f"Baho: {eng_yuqori_baho_talaba.baho}")


#--------------------------------------------------------------------------------------

# 15 vazifa

# import math
# class SimpleIterator:
#     def __init__(self, limit):
#         self.current = 1
#         self.limit = limit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.limit:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
# limit = int(input("Nechinchi songacha sonlardi kvadrati kerak: "))
# iterator = SimpleIterator(limit)
# for number in iterator:
#     print(f"{number}:{math.pow(number, 2)}")


#--------------------------------------------------------------------------------------

# 16 vazifa

# count = 0
# def ab(text):
#     def bc():
#         global count
#         for i in text:
#             count += 1
#     return bc
# text = input("Matn kiriting: ")
# b = ab(text)
# b()
# print(f"siz kiritgan matn uzunligi: {count}")


#--------------------------------------------------------------------------------------

# 17 vazifa

# def salomlashuvchi():
#     def salom_ber(ism):
#         return f"Salom, {ism}!"
#     return salom_ber
# salomlash = salomlashuvchi()
# print(salomlash(input("Ism kiriting: ")))




#===================================Worked by Rustamov Asilbek========================================