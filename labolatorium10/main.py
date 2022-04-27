import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts=ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png') #zapis rozszerzenie jpg
# plt.show()

# dane = {'Kraj':['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         "Stolica":["Bruksela", 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja':[11190846, 1303171035, 207847528, 38675467],
#         'Kontynent':['Europa', 'Azja', 'Amerykapol', "Europa"]}
#
# df=pd.DataFrame(dane)
# grupa=df.groupby("Kontynent").agg({'Populacja':['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja w mld', xlabel='Kontynent', rot=0, legend=True, title='Populacja dla kontynentow', color='pink')# rot ze nazwy w x są poziomokolumnowy
# plt.legend(loc='upper left')#zmiana miejsca legedy
# plt.grid()#siatka
# plt.show()#odczyt wykresu

#wykres kolowy

# df = pd.read_csv('dane (1).csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa= df.groupby("Imię i nazwisko").agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
# plt.legend(loc='upper left')
# plt.show()

# wykres liniowy

# ts = pd.Series(np.random.randn(1000))#losowaie do 1000
# ts=ts.cumsum()
# df=pd.DataFrame(ts)
# print(df)
# df['Śrdnia krocząca'] = df.rolling(window=100).mean()
# print(df)
# df.plot()
# plt.legend(['Wartości', "Srednia krocząca"])
# plt.show()