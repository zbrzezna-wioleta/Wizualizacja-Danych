# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej
# lubiane sporty na sam koniec.

# lista=['koszykowka', 'pilka reczna', 'skoki narciarskie', 'tenis', 'hokej', 'boks']
# print(lista)
# lista.reverse()
# print(lista)
# lista.append('siatkowka')
# print(lista)
# lista.append('plywanie')
# print(lista)
# lista.append('pilka nozna')
# print(lista)

# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
# Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
#
# slownik_skrotow={'wyd.': 'wydanie', 'red.': 'redakcja', 'wydawn.': 'wydawnictwo', 'praca zbior.': 'praca zbiorowa' }
# print(slownik_skrotow.keys())
# print(slownik_skrotow.values())

# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co
# wartością w takim słowniku. Policz liczbę elementów w słowniku.

# slownik_gier={'DSJ4':'Delux Ski Jumping4', 'DSJ3':'Delux Ski Jumping3','GTAV': 'Grand Theft Auto5', 'PES21':'Pro Evolution Soccer21'}
# print(slownik_gier.__len__())

# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji
# input
#
# napis=input("Wpisz dowolny napis: ")
# print(napis)
# print(napis.count('a'))

# Zad 5.
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).

# system.stdout.write('Podaj pierwsza liczbe: ')
# a = system.stdin.readline()
# a = int(a)
# system.stdout.write('Podaj druga liczbe: ')
# #b = system.stdin.readline()
#b = int(b)
#system.stdout.write('Podaj trzecia liczbe: ')
#c = system.stdin.readline()
#c = int(c)
#system.stdout.write("Wartosc = " + str(a ** b + c))

# Zad 6. 
# Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od
# wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
#
#
# a=input(u"Podaj liczbę całkowitą a: ")
# b=input(u"Podaj liczbę całkowitą b: ")
# c=input(u"Podaj liczbę całkowitą c: ")
#
# a=int(a)
# b=int(b)
# c=int(c)
#
# if ((a > b) & (a > c)):
#     print(u"Liczba a: %d jest największa" % (a))
# elif ((b >a) & (b > c)):
#     print(u"Liczba b: %d jest największa" % (b))
# elif ((c > a) & (c > b)):
#     print(u"Liczba c: %d jest największa" % (c))
# elif ((a==b) > c):
#     print(u"Liczby a i b są równe: %d, %d i są największe" % (a, b))
# elif ((a==c) > b):
#     print(u"Liczby a i c są równe: %d, %d i są największe" % (a, c))
# elif ((c==b) > a):
#     print("Liczby c i b są równe: %d, %d i są największe" % (c, b))
# elif ((a == b) < c):
#     print(u"Liczba c: %d jest największa" % (c))
# elif ((a == c) < b):
#     print(u"Liczba b: %d jest największa" % (b))
# elif ((c == b) < a):
#     print(u"Liczba a: %d jest największa" % (a))
# else:
#     print("Wszystkie liczby są równe: %d=%d=%d => a=b=c" % (a,b,c))

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą
# użycia pętli for podnieś każdą liczbę do kwadratu.

# liczby = [1, 4.74, 7, 1.50]
# for i in range (0, len(liczby), 1):
#      liczby[i] *= liczby[i]
# print(liczby)

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko
# parzyste liczby.

# lista=[]
# x = 0
# while x <10:
#      a = int(input("Podaj liczbe %d: " % (x+1)))
#      x+=1
#      if a % 2 == 0 :
#          lista.append(a)
# print(lista)

# Zad. 9.
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda
# wartość ujemną to powinien być wyłapany błąd

from math import *
x = (input("Podaj liczbę z której obliczę pierwiastek: "))
x=int(x)
try:
        wynik = sqrt(x)
        print(wynik)
except ValueError:
        print("Podano ujemną liczbę")
