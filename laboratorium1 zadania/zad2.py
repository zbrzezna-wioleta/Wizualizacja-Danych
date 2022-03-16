#Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
# I sposób
a=10
b=2

dzielenie=a/b
print(dzielenie)

dodawanie=a+b
print(dodawanie)

odejmowanie=a-b
print(odejmowanie)

mnozenie=a*b
print(mnozenie)

potega=a**b
print(potega)

# II sposób

znak = input("Podaj znak: /,+,%,^,-,*")
a = input("Podaj liczbe: ")
b = input("Podaj liczbe: ")
a = float(a)
b = float(b)
if znak == '+':
    print("Suma: ", a + b)
elif znak == '-':
    print("Roznica = ", a - b)
elif znak == '^':
    if (a == 0 & b == 0):
        print("symbol nieoznaczony")
    else:
        print("Potega: ", a ** b)
elif znak == '*':
    print("Iloczyn: ", a * b)
elif znak == '/':
    if (b == 0):
        print("Nie dzielimy przez 0!")
    else:
        print("Dzielenie", a / b)
else:
    print("Nieprawidlowy znak")
