# Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie
# wyświetl je wykorzystując odpowiednie formatowanie

val1 = "Ala ma kota"
val2 = 2.453
liczba_szesnastkowa=0x1f
print("Zmienna typu string: %(zm1)s" %{'zm1':val1})
print("Zmienna typu float: %(zm1)f"%{'zm1':val2})
print('{0:x}'.format(liczba_szesnastkowa))
