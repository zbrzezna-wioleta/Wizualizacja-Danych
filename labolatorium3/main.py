import math
# #zad1
# a = []
# for x in range(0, 10):
#     a.append(x**2)
# print(a)
# a2=[x**2 for x in range(0, 10)]
# print(a2)
#
# b = []
# for x in range(0, 6):
#     b.append(3**x)
# print(b)
# b2 = [3**x for x in range(0, 6)]
# print(b2)
#
# c = []
# for x in a:
#     if x % 2 == 1:
#         c.append(x)
# print(c)
# c2= [x for x in a if x % 2 == 1]
# print(c2)

#zad2
# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a, b))
# print(lista)
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

#Zad3
#
# slownik = {'PZU':'Państwowy Zakład Ubezpieczeń',
#            'ZUS':'Zakład Ubezpieczeń Społecznych',
#            'PKO':'Państwowa Kasa Oszczędności'}
# slownik_odwrocony={}
# print(slownik)
# for key, value in slownik.items():
#     slownik_odwrocony[value] = key
# print(slownik_odwrocony)
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)

#zad4
# def rown_kwadratowe(a, b, c):
#     delta = b**2 - 4 * a *c
#     if delta < 0:
#         print('brak rozwiazan')
#         return -1
#     elif delta == 0:
#         print('jedno rozwiazanie')
#         x = (-b)/(2*a)
#         return x
#     else:
#         print('dwa rozwiozania')
#         x1 = ((-b)-math.sqrt(delta))/(2*a)
#         x2 = ((-b)+math.sqrt(delta))/(2*a)
#         return x1, x2
#
# print(rown_kwadratowe(6, 1, 3))
# print(rown_kwadratowe(1, 2, 1))
# print(rown_kwadratowe(1, 4, 1))

#zad5
# def czy_parzysta(a):
#     if a % 2 == 0:
#         return 'Parzysta'
#     else:
#         return 'Nieparzysta'
#
# print(czy_parzysta(4))
# print(czy_parzysta(7))

# #zad6
# def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# #argumenty domsylne
# print(dlugosc_odcinka())
# #argumenty pozycyjne
# print(dlugosc_odcinka(4, 5, 6, 9))
# #dwa argumenty pozycyjne i dwa określane
# print(dlugosc_odcinka(2, 2, y2=7, x2=5))
# #cztery określane, argumenty poza kolejnością
# print(dlugosc_odcinka(x2=6, y2=4, x1=2, y1=3))
# #dwa argumenty domyślne, dwa z nową kolejnością
# print(dlugosc_odcinka(x2=4, y2=7))

#zad7
# def ciag(*liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma +=i
#         return suma
#
# print(ciag())
# print(ciag(1, 2, 3, 4, 5, 6, 7, 8))

#zad8

# def co_lubie(**rzeczy):
#     for cos in rzeczy:
#         print('to jest')
#         print(cos)
#         print('co lubie')
#         print(rzeczy[cos])
# co_lubie(gry=['planszowe', 'komputrowe'], slodycze='czekolada')