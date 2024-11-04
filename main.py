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

def histogram(data, name, bins, edgecolor, range):
    plt.hist(data[name], bins=bins, edgecolor=edgecolor, range=range)

    # Opis osi x i y oraz tytul
    plt.xlabel('Długość (cm)')
    plt.ylabel('Liczebność')
    plt.title(f'DŁugość działki kielicha')

    # Ustawienie zakresu osi y
    plt.ylim(0, 35)
    plt.show()

# Wywołanie funkcji histogram
histogram(data, 'Dlugosc kielicha', 8, 'black', (4.0, 8.0))