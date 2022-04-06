# import numpy as np   #deklaracja tablicy tworzenie tablic
# a = np.arange(2)
# print(a)

#Przykład1

# import numpy as np
# a = np.array([0, 1]) #inicjalizacja tablicy
# print(a)
# a = np.arange(2) #drugi sposób
# print(a)
# print(type(a)) #wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray
# print(a.dtype) #sprawdzenie typu danych tablicy
# a = np.arange(2, dtype='int64') #inicjalizacja tablicy z konkretnym typem danych
# print(a.dtype)
# b = a.astype('float') #zapisywanie kopii tablicy jako tablicy z innym typem
# print(b)
# print(b.dtype)
# print(b.shape) #wypisanie rozmiaru tablicy
# print(a.ndim) #można też sprawdzić ilośc wymiarów tablicy
# #stworzenie tablicy wielowymiarowej może wyglądać tak parametrem przekazywanym
# #do funkcji array jest obiekt, który zostanie skonwertowany na tablicę
# #może to być Pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m.shape)
# print(type(m)) #ponownie typem jest ndarray

#Przykład2

import numpy as np
zera=np.zeros((5,5)) #tworzenie macierzy danego rozmiaru wypełniona 0
jedynki=np.ones((4,4)) #tworzenie macierzy danego rozmiaru wypełniona 1
print(zera)
print(jedynki)
print(zera.dtype) #warto sprawdzic jaki jest domyślny typ danych takich tablic
print(jedynki.dtype)

#można równiez stworzyć 'pustą' macierz o podanych wymiarach,
#która pusta wcale nie jest
#wartości umieszczane są losowo, najpierw podawana jest ilość wierszy pózniej kolumn
pusta = np.empty((2,2))
print(pusta)
poz_1 = pusta[1,1]#odwoływanie się do elementów tablicy rak jak w liście
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)
macierz = np.array([[1, 2], [3, 4]]) #twozrenie macierzy 2x2 z uzupelnieniem
print(macierz)

liczby = np.arange(1, 2, 0.1) #funkcja arange potrafi wtozryc ciągi
print(liczby)                  # liczb zmiennoprzecinkowych

liczby_lin = np.linspace(1, 2, 5) #podobnie działa funkcja linspace,
print(liczby_lin)                  #ktre działanie jest równoważne tej samej funkcji w matlabie

z= np.indices((5, 3)) #tworzymy dwie macierze, najpierw wartosci interowane
print(z)

x, y = np.mgrid[0:5, 0:5] #wielowymiarowe macierze możemy również generować
print(x)                # funkcją mgrid
print(y)

mat_diag = np.diag([a for a in range(5)]) #podobnie jak w matlabie możemy tworzyc
print(mat_diag)                           #macierze diagonalne

#w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na głównej przekątnej
# macierzy możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem
# głównej przekątnej która zostanie wypełniona wartościami podanego wektora
mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)

z = np.fromiter(range(5), dtype='int32') #Numpy jest w stanie stworzyć tablicę jednowymiarową
print(z)                  # z dowolnego obiketu iterowalnego (iterable)

#ciekawą funkcją Numpy jesr funkcja frombuffer, dzięki której
#możemy stworzy np. tablicę znaków

# marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S1')
# print(mar)
# mar_2 = np.frombuffer(marcin, dtype='S2')
# print(mar_2)
#powyższa funkcja ma jednak pewną wadę dla pythona 3.x, która powodóje, że trzeba jawnie określić#
# iż ciąg znaków przekazujemy jako ciąg bajtów co osiągamy po przez podanie litery 'b' przed wartością
#zmiennej tekstowej. Można podobne efekty osiągnąć inaczej

marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_4 = np.array(list(marcin), dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin, dtype='S1')
mar_7 = np.fromiter(marcin, dtype='U1')
print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)

#tablice w Numpy możemy w prosty sposób do siebie dodawać, odejmować, mnożyc i dzielić
mat = np.ones((2,2))
mat_1 = np.ones((2, 2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat * mat_1)
print(mat/mat_1)

#indeksowanie i cięcia tablic

import numpy as np
#cięcie (slicing) tablicy numpy można wykonać za pomocą wartości z
# funkcji slice lub range
a= np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
#możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)

print(a[2:7:2])
#lub tak
print(a[1:])
print(a[2:5])
#w podobny sposób postępujemy w przypadku tablic wielowymiarowych

mat = np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])
#od drugiego wiersza
print(mat[:,1])
#druga kolumna jako wektor
print(mat[:,-1:])
#ostatnia kolumna
print(mat[2:6, 1:3])
# 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2,6,2)])
# 3 i 5 kolumna
print('')
#bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcia można osiągnąć wg. poniższego przykładu
#y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows,cols]
print(y)