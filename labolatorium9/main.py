# numpy 1.22.2
# pandas 1.4.0
# openpyxl 3.0.9

import numpy as np
import pandas as pd

s=pd.Series([1, 3, 5.5, np.nan, 'a'])
print(s)
s1=pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s1)

dane={'Kraj':['Belgia', 'Indie', 'Brazylia'],
      'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
      'Populacja':[11190846, 1303171035, 207847628]}
df = pd.DataFrame(dane)
print(df)

# daty = pd.date_range('20220420', periods=5)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)
#
# df = pd.read_csv('iris (1).csv', header=0, sep=',', decimal='.')
# print(df)

# df.to_csv('nowy.csv', index=False)
# # index false indeksy są pomiajne
#
# # xlsx = pd.ExcelFile('wyniki.xlsx')
# # df = pd.read_excel(xlsx, header=0)
# # print(df)
# # otwieranie pliku z rozszerzeniem xlsx
#
# df.to_excel('nowy.xlsx', sheet_name='Arkusz1', index=False)
# zapis do nowego pliku

# print(s1['a'])
# print(s1.a)
#
# print(df['Populacja'])
# print(df.iloc[[0], [0]])
# print(df.loc[[0], ['Kraj']])
# print(df.at[0, 'Kraj'])
#
# print('kraj: ' + df.Kraj)

# do pliku csv
# print(df.sample(10))
# print(df.sample(frac=0.5))
# print(df.sample(10, replace=True))

# print(df.head(10))
# print(df.tail())


# print(s1[(s1 > 10)])
# print(s1.where( s1 > 10, 'element nie spełnia warunku'))
# seria = s1.coppy()
# print(seria)
# seria.where(seria > 10, 'element nie spełnia warunku', inplace=True)
# print(seria)

# print(s1[~(s1 > 10)])
# print(s1[(s1<13) & (s1 > 8)])
#
# print (df[df['Populacja'] > 12000000])
# print(df[((df.Populacja > 1000000) & (df.index.isin([0, 2])))])

# szukaj = pd.isin(['Belgia', 'Brasilia'])
# print(df.isin(szukaj))

s1['e'] = 15
print(s1)
df.loc[3] = 'nowy element'
print(df)

df.loc[4]=['Polska', 'Warszawa', 38675467]
print(df)
df.drop(3, inplace=True)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka poł.', 'Europa']
print(df)

print(df.sort_values(by='Kraj'))

grupa = df.groupby(by='Kontynent')
print(grupa.get_group('Europa'))
print(df.groupby('Kontynent').agg({'Populacja': ['sum']}))


