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

def count_species(species_data):
    """
    Zlicza i wyświetla liczbę wystąpień każdego gatunku w danych.
    :param species_data: dane numeryczne dla gatunków.
    :return: None
    """

    satos_count = 0
    versicolor_count = 0
    virginica_count = 0

    for value in species_data:
        if value == 0:
            satos_count += 1
        elif value == 1:
            versicolor_count += 1
        elif value == 2:
            virginica_count += 1
    print(f'Ilosc gatunku satosa: {satos_count}, procentowo: {satos_count / len(species_data) * 100}%')
    print(f'Ilosc gatunku versicolor: {versicolor_count}, procentowo: {versicolor_count / len(species_data) * 100}%')
    print(f'Ilosc gatunku virginica: {virginica_count}, procentowo: {virginica_count / len(species_data) * 100}%')
    print(f'Wszystkich gatunkow: {len(species_data)}, procentowo: {len(species_data) / len(species_data) * 100}%')

# Wywołanie funkcji countSpecies
count_species(data['Gatunek'])

def feature_statistics(feature_data):
    """
    Oblicza i wyświetla statystyki opisowe dla danej cechy rośliny.
    :param feature_data: dane numeryczne dla danej cechy.
    :return: None
    """

    print(f'\nNazwa: {feature_data.name}')
    print(f'Minimalna: {min(feature_data)}')
    print(f'Srednia: {np.mean(feature_data)}')
    print(f'Odchylenie standardowe: {np.std(feature_data)}')
    print(f'Mediana: {np.median(feature_data)}')
    print(f'Kwartyl dolny: {np.percentile(feature_data, 25)}')
    print(f'Kwartyl gorny: {np.percentile(feature_data, 75)}')
    print(f'Maksymalna: {max(feature_data)}')


# Wywołanie funkcji featureStatistics dla każdej cechy
feature_statistics(data['Dlugosc kielicha'])
feature_statistics(data['Szerokosc kielicha'])
feature_statistics(data['Dlugosc platka'])
feature_statistics(data['Szerokosc platka'])


# ------------------- Zadanie 2 -------------------

# fig - obiekt typu Figure, axs - tablica obiektów typu Axes, 4 wiersze, 2 kolumny, figsize - rozmiar wykresu w calach
fig, axs = plt.subplots(4, 2, figsize=(12, 18))

def histogram(x, y, feature_data, bins, value_range, title, ylim):
    """
    Rysuje histogram dla wybranej cechy rośliny na wskazanej osi wykresu.
    :param x: indeks wiersza osi na wykresie.
    :param y: indeks kolumny osi na wykresie.
    :param feature_data: dane dla danej cechy.
    :param bins: liczba przedziałów histogramu.
    :param value_range: zakres wartości na osi x.
    :param title: tytuł wykresu.
    :param ylim: zakres wartości na osi y.
    :return: None
    """

    # axs[x][y] - obiekt typu Axes, na którym rysowany jest histogram
    # data - dane, bins - liczba przedziałów, edgecolor - kolor krawędzi, range - zakres danych, title - tytuł wykresu, ylim - zakres osi y
    axs[x][y].hist(feature_data, bins=bins, edgecolor='black', range=value_range)

    # Opis osi x i y oraz tytul
    axs[x][y].set_xlabel('Długość (cm)')
    axs[x][y].set_ylabel('Liczebność')
    axs[x][y].set_title(f'{title}')

    # Ustawienie zakresu osi y
    axs[x][y].set_ylim(ylim)


# Wywołanie funkcji histogram dla każdej cechy
histogram(0, 0, data['Dlugosc kielicha'], 8, (4.0, 8.0), 'Długość działki kielicha', (0, 35))
histogram(1, 0, data['Szerokosc kielicha'], 5, (2.0, 4.5), 'Szerokość działki kielicha', (0, 75))
histogram(2, 0, data['Dlugosc platka'], 12, (1.0, 7.0), 'Długość płatka', (0, 30))
histogram(3, 0, data['Szerokosc platka'], 5, (0.0, 2.5), 'Szerokość płatka', (0, 55))

# Generowanie boxplotów
def boxplot_by_species(x, y, feature, ylabel, ylim):
    """
    Generuje boxploty dla danej cechy rośliny, grupując dane według gatunku.
    :param x: indeks wiersza osi na wykresie.
    :param y: indeks kolumny osi na wykresie.
    :param feature: cecha rośliny.
    :param ylabel: opis osi y.
    :param ylim: zakres wartości na osi y.
    :return: None
    """

    # data.boxplot - generowanie boxplotów, column - cecha, by - grupowanie po gatunku, ax - obiekt typu Axes, na którym rysowany jest boxplot
    data.boxplot(column=feature, by='Gatunek', ax=axs[x][y], medianprops=dict(color="orange"))
    axs[x][y].set_title('')
    axs[x][y].set_ylim(ylim)
    axs[x][y].set_xticklabels(['setosa', 'versicolor', 'virginica'])
    axs[x][y].set_xlabel('Gatunek')
    axs[x][y].set_ylabel(ylabel)
    axs[x][y].grid(False)

# Generowanie boxplotów dla każdej cechy
boxplot_by_species(0,1, 'Dlugosc kielicha', 'Długość (cm)', (4, 8))
boxplot_by_species(1,1, 'Szerokosc kielicha', 'Szerokość (cm)', (1, 5))
boxplot_by_species(2,1, 'Dlugosc platka', 'Długość (cm)', (0,7))
boxplot_by_species(3,1, 'Szerokosc platka', 'Szerokość (cm)', (0, 3))

# Ustawienie tytułu wykresu
plt.suptitle('')

# Ustawienie odstępów między wykresami
plt.subplots_adjust(wspace=0.2, hspace=0.6)

# ------------------- Zadanie 3 -------------------

# Tworzymy nową figurę i ustawiamy jej rozmiar
fig2, axs2 = plt.subplots(3, 2, figsize=(8, 14))

def correlations(x, y, feature_data, feature_data_1, desc, desc1):
    """
    Rysuje wykres punktowy wraz z linią regresji i wyświetla współczynnik korelacji dla dwóch cech.
    :param x: indeks wiersza osi na wykresie.
    :param y: indeks kolumny osi na wykresie.
    :param feature_data: dane numeryczne dla jednej cechy.
    :param feature_data_1: dane numeryczne dla drugiej cechy.
    :param desc: opis osi x.
    :param desc1: opis osi y.
    :return: None
    """

    # Obliczenie współczynnika korelacji, funkcja corrcoef zwraca macierz korelacji, dlatego wybieramy element [0, 1]
    correlation = np.corrcoef(feature_data, feature_data_1)[0, 1]

    # Obliczenie parametrów regresji liniowej, funkcja polyfit zwraca współczynniki wielomianu, w tym przypadku liniowego
    slope, intercept = np.polyfit(feature_data, feature_data_1, 1)

    # Obliczenie wartości na prostej regresji
    regression_line = slope * feature_data + intercept

    # Przypisanie wykresu do odpowiedniej pozycji w siatce (wiersz, kolumna)
    axs2[x, y].scatter(feature_data, feature_data_1, s=60, edgecolor='none')

    # Dodanie prostej regresji
    axs2[x, y].plot(feature_data, regression_line, color="red")

    # Ustawienia tytułów i etykiet
    axs2[x, y].set_xlabel(desc)
    axs2[x, y].set_ylabel(desc1)

    # Ustawienie zakresu osi x
    axs2[x, y].set_xlim(feature_data.min() - 0.5, feature_data.max() + 0.5)

    # .2f - zaokrąglenie do dwóch miejsc po przecinku
    axs2[x, y].set_title(f'r = {correlation:.2f}; y = {slope:.1f}x + {intercept:.1f}')

# Wywołanie funkcji correlations dla każdej pary cech
correlations(0, 0, data['Dlugosc kielicha'], data['Szerokosc kielicha'], 'Długość działki kielicha (cm)', 'Szerokość działki kielicha (cm)')
correlations(0, 1, data['Dlugosc kielicha'], data['Dlugosc platka'], 'Długość działki kielicha (cm)', 'Długość płatka (cm)')
correlations(1, 0, data['Dlugosc kielicha'], data['Szerokosc platka'], 'Długość działki kielicha (cm)', 'Szerokość płatka (cm)')
correlations(1, 1, data['Szerokosc kielicha'], data['Dlugosc platka'], 'Szerokość działki kielicha (cm)', 'Długość płatka (cm)')
correlations(2, 0, data['Szerokosc kielicha'], data['Szerokosc platka'], 'Szerokość działki kielicha (cm)', 'Szerokość płatka (cm)')
correlations(2, 1, data['Dlugosc platka'], data['Szerokosc platka'], 'Długość płatka (cm)', 'Szerokość płatka (cm)')

# Ustawienie odstępów między wykresami
plt.subplots_adjust(wspace=0.3, hspace=0.6)

# Wyświetlenie wykresów
plt.show()
