# Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie
# wyświetl je wykorzystując odpowiednie formatowanie

x = hex(16)
z = 'informatyka'
y = 3.79
print("nazwa przedmiotu: %s, zmienna szesnastkowa: %s, zmienna float: %f" % (z, x, y))

liczba_szesnastkowa=0x1f
print('{0:x}'.format(liczba_szesnastkowa))
