import numpy as np
#Zad1.
#Za pomocą funkcji arange stwórz tablicę numpy składającą się z 20 kolejnych wielokrotności liczby 4

# a=np.arange(0, 4*20+1, 4)
# print(a)

# Zad2.
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int32
lista = [1.5, 2.3, 4.7, 3.6, 6.7]
a=np.array(lista)
print(a)
b=a.astype(dtype='int32')
print(b)
c=np.array(lista, dtype='int32')
print(c)

#zad3
# def tablica(n):
    a = np.zeros(n*n, dtype='int32')
    for i in  range (0, len(a)):
        a[i]=2**i
    tab=a.reshape((n,n))
    return tab

print(tablica(5))

#zad4
def generuj(liczba, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=liczba)
print(generuj(2, 4))
#zad5
# def diagonalna(n):
#     a = np.arange(n, -1, -1)
#     diag = np.diag(a, 2)
      return diag
print(diagonalna(4))

 # zad6
 malina = np.array(list('malina'))
mrowka = np.array(list('mrowka'))
armata = np.array(list('armata'))
armata=np.flip(armata)

wykreslanka=np.zeros((6,6), dtype='str')
print(wykreslanka)
#
# wykreslanka=np.diag(mrowka)
# # wykreslnka[:, 0]=malina
# # wykreslanka[5,::-1]=armata
# # wykreslanka

# zad7#
def macierz(n):
    mac=p.zeros((n, n), dtype='int32')
    mac+=np.diag([2 for _ in range(n)])
    for i in

# zad8