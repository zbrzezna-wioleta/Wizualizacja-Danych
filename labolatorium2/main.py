# a = 7
# b = 9
# if a>b:
# print('liczba a jest większa od liczby b')
# elif a<b:
# print('liczba a jest mniejsza od liczby b')
# else:
# print('liczby są równe')

# if a==b:
# print('liczby są równe' % {'zm1':a, 'zm2':b})
# elif a<b:
# print('liczba a jest mniejsza od liczby b')
# else:
# print('liczby nie są równe' % {'zm1':a, 'zm2':b})

# a=input('podaj liczbę: ')
# print(a)
# print(type(a))
# a = int(a)
# print(a)
# print(type(a))

# a=input('podaj pierwszą liczbę: ')
# b=input('podaj drugą liczbę: ')
# c=input('podaj trzecią liczbę: ')
# d=input('podaj czwartą liczbę: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a>b)&(c>d):
# print('a jest wiekszę od b i c jest większę od d')
# else:
# print('a jest mniejsze od b lub c jest mniejsze od d')

# for a in range(0,7,1):
# print(a)
#
# lista=['cos', 4,5,6.5]
# for a in lista:
# print(a)
# else:
# print('wyświetlono wszytskie elementy z liczby')

# licznik = 0
# while licznik!=11:
# print(licznik)
# licznik +=1

# lista=[4, 8, 5, 3, 2, 9, 7]
# licznik = 0
# liczba = input('wpisz liczbe całkowitą: ')
# while licznik != len(lista):
# if int(liczba)- lista[licznik] == 0:
# print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' =0')
# break
# else:
# licznik +=1
# else:
# print('Żadna z wartości nie dała odpowiedniego wyniku')
#
# lista1 = [4, 6, 8, 1, 6, 7, 2, 9]
# lista2 = [4, 7, 3, 5]
# suma = []
# for a in lista1:
# for b in lista2:
# wynik = a + b
# suma.append(wynik)
# print(suma)
#

# a = input("podaj pierwszą liczbę: ")
# b = input("podaj drugą liczbę: ")
# try:
# a = int(a)
# b = int(b)
# wynik = a / b
# print(wynik)
# except ZeroDivisionError:
# print('Nie można dzielić przez 0')
# except ValueError:
# print('Nie wczytano liczby całkowitej')

lista = [1, 4, 6, 8, 0]
słownik = {1:10, 3:7, 9:20, 'a':'n'}
print(lista)
print(słownik)

lista.append(słownik['a'])
print(lista)

lista.insert(słownik[3], słownik[3])
print(lista)

słownik[2] = 'g'
print(słownik)

lista.remove(8)
print(lista)

lista.pop(1)
print(lista)