import numpy as np
import pandas as pd

# zad1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
# zad2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[df['Liczba'] > 1000])
# tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imie'] == 'WIOLETA'])
# sumę wszystkich urodzonych dzieci w całym danym okresie,
print(df.agg({'Liczba': ['sum']}))
#sumę dzieci urodzonych w latach 2000-2005
print(df[((df.Rok >= 2000) & (df.Rok <= 2005))].agg({'Liczba' : ['sum']}))
# sumę urodzonych chłopców i dziewczynek,
print(df.groupby('Plec').agg({'Liczba':['sum']}))
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(df.groupby)
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,


# zad3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# df=pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# # print(df['Sprzedawca'].unique())
# # print('')
# 5 najwyższych wartości zamówień
# # print(df.sort_values('Utarg', ascending=False).head())
# # print('')
# ilość zamówień złożonych przez każdego sprzedawcę
## print(df.sort_values('Utarg', ascending=False).head())
# print('')
# print(df.groupby('Sprzedawca').size())
# print('')

# sumę zamówień dla każdego kraju
# # print(df.groupby('Kraj').agg({'Utarg':['sum']}))
# # print(df.groupby('Kraj').size())
# # print('')
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
#
# średnią kwotę zamówienia w 2004 roku,
# # print(df[df['Data zamówienia'].str[:4]=='2004'].agg({'Utarg':['mean']}))
# # print('')
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
# print(df[df['Data zamowienia'].str[:4]=='2004'].agg({'Utarg':['mean']}))
# rok_2004=df[((df['Data zamowinia']>='2004-01-01')&(df['Data zamowinia']<='2004-12-31'))]
# rok_2004.to_csv("zamowinia_2004.csv", index=False)






