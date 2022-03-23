import math
import random
# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,47
# C = {x: x∈B i x jest liczbą podzielną przez 2}
# a = [ 1 - x for x in  range(1, 11, 1)]
# print(a)
# b = [ 4 ** x for x in range(8)]
# print(b)
# c = [x for x in b if x % 2 == 0]
# print(c)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python
# # Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy
# lista=[]
# for x in range(10):
#     lista.append(random.randrange(1, 50))
# print(lista)
# lista2=[x for x in lista if x%2==0]
# print(lista2)

# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a
# wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do
# zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
# produkty={'Masło':"G", "Karton Mleka":"Sztuki", "Cukierki":"KG","Butelki Wody":"Sztuki"}
# print(produkty)
# produkty2={key:value for key, value in produkty.items() if value=="Sztuki"}
# print(produkty2)

# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
# def czyProstokatny(a, b, c):
#     if pow(a, 2)+pow(b, 2)==pow(c, 2):
#         print("Jest prostokątny")
#     else:
#         print("Nie jest prostokątny")
# czyProstokatny(3,4,5)

# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
# def poleTrapezu(a=5, b=6, h=3):
#     pole=((a+b)*h)/2
#     return pole
# print(poleTrapezu())

# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile
# elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
# def ciag(a1=1,b=4,ile=10):
#     for x in range(ile):
#         a1=a1*b
#     return a1
# print(ciag())

# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.
# def ciag2(*liczba):
#     if len(liczba)==0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in liczba:
#             iloczyn=iloczyn*x
#     return iloczyn
# print(ciag2(1,2,3,4,5))

# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz
# to nazwa produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i
# zwracać całościową wartość tych produktów.
# def kasa(**koszyk):
#     suma=0
#     for key,value in koszyk.items():
#         print("Produkt: {} , Cena: {}".format(key,value),"zł")
#     for key,value in koszyk.items():
#         suma=suma+value
#     print("Suma zakupów: "+ str(suma) + " zł")
#
# kasa(Jablko= 2, Marchew= 1.5, Bulka= 1.8, Ser= 5, Maka= 5.2, Jajka= 6)
# # Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami
# arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.
#
# print(ciagi.aryt.n_ty_wyraz_a1 (1, 3, 3))
# print(ciagi.aryt.n_ty_wyraz_ak (5, 3, 2, 1))
# print(ciagi.aryt.n_ty_wyraz_suma(10, 2))
# print(ciagi.aryt.suma_p_i_n(1, 11, 2))
# print(ciagi.aryt.suma_p(2, 3, 1))
#
# print(ciagi.geom.n_ty_wyraz_a1(1, 3, 3))
# print(ciagi.geom.n_ty_wyraz_ak(9, 3, 2, 3))
# print(ciagi.geom.suma(2, 1, 3))
# print(ciagi.geom.suma(2, 2, 3))