#zad1 Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku
import sys
# lista = []
# for x in range(0,31):
#     lista.append(x*2)
# plik = open('plik.txt', 'a+')
# plik.write(str(lista))
# plik.close()

# #zad2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
# with open('plik.txt', 'r') as plik:
#     for linia in plik:
#         print(linia)

# #zad3
# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
# dane = sys.stdin.readline()
# plik = open('dane.txt', 'w+', encoding='utf-8')
# plik.write(dane)
# plik.close()
# with open('dane.txt', 'r') as plik:
#     for linia in plik:
#         print(linia)

# zad4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# nazwa_produktu, ilosc, jednostka_miary, cena_jed
# oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt () – drukuje informacje o produkcie na ekranie
# ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu
# np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

# import nazakupy
# from nazakupy import *
# produkt = nazakupy("Jabłka", 2.5, "Kg", 2.60)
# produkt.wyswietl_Produkt()
# produkt.ile_produktu()
# print(produkt.ile_kosztuje())

#zad5
# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako
# atrybut. Klasa powinna mieć metody:
# • wyświetl_dane – drukuje elementy na ekran
# • pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# • pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość
# elementów ciągu do wygenerowania.
# • policz_sume – liczy sume elementow
# • policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

# class ciag_aryt:
#     """Ciag arytmetyczny"""
#     def __init__(self, a1, n, r):
#         self.a1 = a1
#         self.n = n
#         self.r = r
#
#     def wyswietl_dane(self):
#         for x in range(self.a1, self.n):
#             print(x+self.r)
#
#
#     def pobierz_parametry(self):
#         self.a1 = input("Podaj poczatek: ")
#         self.a1 = int(self.a1)
#         self.n = input("Podaj ilosc: ")
#         self.n = int(self.n)
#         self.r = input("Podaj roznice: ")
#         self.r = int(self.r)
#
#         ciag = []
#         for x in range(0, self.n):
#             ciag.append(self.a1 + self.r*x)
#         return ciag
#
#     def pobierz_elementy(self):
#         ciag = []
#         self.a1 = input("Podaj ilosc w ciagu: ")
#         self.a1 = int(self.a1)
#         for x in range (0,self.a1):
#             self.n = input("Podaj wartosc: ")
#             ciag.append(self.n)
#         return ciag
#
#     def policz_sume(self):
#         ciag = []
#         suma = 0
#         for x in range(self.a1,self.n):
#             ciag.append(x + self.r)
#             suma += x+self.r
#         return suma
#
#     def policz_elementy(self):
#         ciag = []
#         suma = 0
#         for x in range(self.a1, self.n):
#             ciag.append(x + self.r)
#             suma += 1
#         return suma
#
# ciag = ciag_aryt(1, 10, 2)
# print(ciag.wyswietl_dane())
# print(ciag.pobierz_elementy())
# print(ciag.pobierz_parametry())
# print(ciag.policz_sume())
# print(ciag.policz_elementy())

# zad6
# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna
# przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć
# następujące metody:
# • konstruktor – który nadaje wartość dla x, y i krok
# • idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow * krok w
# odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow * krok w
# odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow * krok w
# odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow * krok w
# odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# • pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody

#
# class Robaczek:
#     """Robaczek"""
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, kroki):
#         self.y = self.y + kroki * self.krok
#
#     def idz_w_prawko(self, kroki):
#         self.x = self.x + kroki * self.krok
#
#     def idz_w_dol(self,kroki):
#         self.y = self.y - kroki * self.krok
#
#     def idz_w_lewo(self,kroki):
#         self.x = self.x - kroki * self.krok
#
#     def gdzie_jestem(self):
#         return 'wspolrzedne x:' + str(self.x) + ' y:' + str(self.y)
#
#
# robak = Robaczek(0, 0, 10)
# robak.idz_w_gore(4)
# robak.idz_w_prawko(2)
# robak.idz_w_dol(3)
# robak.idz_w_lewo(1)
# print(robak.gdzie_jestem())