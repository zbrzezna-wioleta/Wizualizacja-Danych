#Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
a = input("Podaj pierwsza wartosc: ")
b = input("Podaj pierwsza wartosc: ")
a = float(a)
b = float(b)
a += 3
print(a)
b -= 4 + 2
print(b)
a *= b
print(a)
b /= 2
a **= 3
print(a)
a %= 15
print(a)
