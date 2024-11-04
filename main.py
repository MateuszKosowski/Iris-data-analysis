import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytaj plik csv
file = './Zadanie 1 Dane-20241103/data1.csv'

# Wczytaj dane z pliku CSV
# dane to obiekt typu DataFrame
data = pd.read_csv(file, header=None, sep=',')
data.columns = ['Dlugosc kielicha', 'Szerokosc kielicha', 'Dlugosc platka', 'Szerokosc platka', 'Gatunek']


# ------------------- Zadanie 1 -------------------


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

# Statystyki dla danej cechy
def featureStatistics(data):
    print(f'\nNazwa: {data.name}')
    print(f'Minimalna: {min(data)}')
    print(f'Srednia: {np.mean(data)}')
    print(f'Odchylenie standardowe: {np.std(data)}')
    print(f'Mediana: {np.median(data)}')
    print(f'Kwartyl dolny: {np.percentile(data, 25)}')
    print(f'Kwartyl gorny: {np.percentile(data, 75)}')
    print(f'Maksymalna: {max(data)}')


# Wywołanie funkcji featureStatistics dla każdej cechy
featureStatistics(data['Dlugosc kielicha'])
featureStatistics(data['Szerokosc kielicha'])
featureStatistics(data['Dlugosc platka'])
featureStatistics(data['Szerokosc platka'] )


# ------------------- Zadanie 2 -------------------

# fig - obiekt typu Figure, axs - tablica obiektów typu Axes, 4 wiersze, 2 kolumny, figsize - rozmiar wykresu w calach
fig, axs = plt.subplots(4, 2, figsize=(12, 17))

# Wykresy histogramów
def histogram(x, y, data, bins, edgecolor, range, title, ylim):

    # axs[x][y] - obiekt typu Axes, na którym rysowany jest histogram
    # data - dane, bins - liczba przedziałów, edgecolor - kolor krawędzi, range - zakres danych, title - tytuł wykresu, ylim - zakres osi y
    axs[x][y].hist(data, bins=bins, edgecolor=edgecolor, range=range)

    # Opis osi x i y oraz tytul
    axs[x][y].set_xlabel('Długość (cm)')
    axs[x][y].set_ylabel('Liczebność')
    axs[x][y].set_title(f'{title}')

    # Ustawienie zakresu osi y
    axs[x][y].set_ylim(ylim)


# Wywołanie funkcji histogram dla każdej cechy
histogram(0, 0, data['Dlugosc kielicha'], 8, 'black', (4.0, 8.0), 'Długość działki kielicha', (0, 35))
histogram(1, 0, data['Szerokosc kielicha'], 5, 'black', (2.0, 4.5), 'Szerokość działki kielicha', (0, 75))
histogram(2, 0, data['Dlugosc platka'], 12, 'black', (1.0, 7.0), 'Długość płatka', (0, 30))
histogram(3, 0, data['Szerokosc platka'], 5, 'black', (0.0, 2.5), 'Szerokość płatka', (0, 55))


# Przypisanie wartości numerycznych do nazw gatunków
# spacies_labels - słownik przypisujący wartości numeryczne do nazw gatunków
# mapowanie wartości numerycznych na nazwy gatunków - zamiana wartości numerycznych na nazwy gatunków w kolumnie 'Gatunek' w obiekcie data
species_labels = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
data['Gatunek'] = data['Gatunek'].map(species_labels)

# Generowanie boxplotów
def boxplot_by_species(x, y, feature, ylabel, ylim):

    # data.boxplot - generowanie boxplotów, column - cecha, by - grupowanie po gatunku, ax - obiekt typu Axes, na którym rysowany jest boxplot
    data.boxplot(column=feature, by='Gatunek', ax=axs[x][y])
    axs[x][y].set_title('')
    axs[x][y].set_ylim(ylim)
    axs[x][y].set_xlabel('Gatunek')
    axs[x][y].set_ylabel(ylabel)
    axs[x][y].grid(False)

# Generowanie boxplotów dla każdej cechy
boxplot_by_species(0,1, 'Dlugosc kielicha', 'Długość (cm)', (4, 8))
boxplot_by_species(1,1, 'Szerokosc kielicha', 'Szerokość (cm)', (0, 6))
boxplot_by_species(2,1, 'Dlugosc platka', 'Długość (cm)', (0,8))
boxplot_by_species(3,1, 'Szerokosc platka', 'Szerokość (cm)', (0, 4))

plt.suptitle('Analiza Irysów')
plt.subplots_adjust(wspace=0.2, hspace=0.6)

plt.show()



