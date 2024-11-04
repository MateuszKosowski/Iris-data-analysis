import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytaj plik csv
file = './Zadanie 1 Dane-20241103/data1.csv'

# Wczytaj dane z pliku CSV
# dane to obiekt typu DataFrame
data = pd.read_csv(file, header=None, sep=',')
data.columns = ['Dlugosc kielicha', 'Szerokosc kielicha', 'Dlugosc platka', 'Szerokosc platka', 'Gatunek']

# Konwersja DataFrame do listy list (tablicy dwuwymiarowej)
dataList = data.values.tolist()

# Zliczanie ilość z danego gatunku
def countSpecies(dataList):
    satosCount = 0
    versicolorCount = 0
    virginicaCount = 0

    for row in dataList:
        if row[-1] == 0:
            satosCount += 1
        elif row[-1] == 1:
            versicolorCount += 1
        elif row[-1] == 2:
            virginicaCount += 1
    print(f'Ilosc gatunku satosa: {satosCount}, procentowo: {satosCount / len(dataList) * 100}%')
    print(f'Ilosc gatunku versicolor: {versicolorCount}, procentowo: {versicolorCount / len(dataList) * 100}%')
    print(f'Ilosc gatunku virginica: {virginicaCount}, procentowo: {virginicaCount / len(dataList) * 100}%')
    print(f'Wszystkich gatunkow: {len(dataList)}, procentowo: {len(dataList) / len(dataList) * 100}%')

# Wywołanie funkcji countSpecies
countSpecies(dataList)

def charakterystykaCechy(data, name):
    nazwa = data[name]
    print(f'\nNazwa: {name}')
    print(f'Minimalna: {min(nazwa)}')
    print(f'Srednia: {np.mean(nazwa)}')
    print(f'Odchylenie standardowe: {np.std(nazwa)}')
    print(f'Mediana: {np.median(nazwa)}')
    print(f'Kwartyl dolny: {np.percentile(nazwa, 25)}')
    print(f'Kwartyl gorny: {np.percentile(nazwa, 75)}')
    print(f'Maksymalna: {max(nazwa)}')

# Charakterystyka cech dla dlugosci kielicha
charakterystykaCechy(data, 'Dlugosc kielicha')

# Charakterystyka cech dla szerokosci kielicha
charakterystykaCechy(data, 'Szerokosc kielicha')

# Charakterystyka cech dla dlugosci platka
charakterystykaCechy(data, 'Dlugosc platka')

# Charakterystyka cech dla szerokosci platka
charakterystykaCechy(data, 'Szerokosc platka')

# Histogram dla dlugosci kielicha

# Funkcja histogram
# data - dane, name - nazwa kolumny, bins - ilosc przedzialow, edgecolor - kolor krawedzi, range - zakres osi x

fig, axs = plt.subplots(4, 2, figsize=(12, 15))

def histogram(x, y, data, bins, edgecolor, range, title, ylim):
    axs[x][y].hist(data, bins=bins, edgecolor=edgecolor, range=range)

    # Opis osi x i y oraz tytul
    axs[x][y].set_xlabel('Długość (cm)')
    axs[x][y].set_ylabel('Liczebność')
    axs[x][y].set_title(f'{title}')

    # Ustawienie zakresu osi y
    axs[x][y].set_ylim(ylim)

def boxplot(x, y, data, ylim):
    axs[x][y].boxplot(data)

    # Opis osi x i y oraz tytul
    axs[x][y].set_ylabel('Długość (cm)')

    # Ustawienie zakresu osi y
    axs[x][y].set_ylim(ylim)

# Wywołanie funkcji histogram dla dlugosci kielicha
histogram(0, 0, data['Dlugosc kielicha'], 8, 'black', (4.0, 8.0), 'Długość działki kielicha', (0, 35))
histogram(1, 0, data['Szerokosc kielicha'], 5, 'black', (2.0, 4.5), 'Szerokość działki kielicha', (0, 75))
histogram(2, 0, data['Dlugosc platka'], 12, 'black', (1.0, 7.0), 'Szerokość działki kielicha', (0, 30))
histogram(3, 0, data['Szerokosc platka'], 5, 'black', (0.0, 2.5), 'Szerokość działki kielicha', (0, 55))

boxplot(1, 0, data['Dlugosc kielicha'], (4, 8))

plt.subplots_adjust(wspace=0.2, hspace=0.6)

plt.show()