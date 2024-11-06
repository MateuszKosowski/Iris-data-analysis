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

# Zliczanie ilość z danego gatunku
def countSpecies(data):
    satosCount = 0
    versicolorCount = 0
    virginicaCount = 0

    for value in data:
        if value == 0:
            satosCount += 1
        elif value == 1:
            versicolorCount += 1
        elif value == 2:
            virginicaCount += 1
    print(f'Ilosc gatunku satosa: {satosCount}, procentowo: {satosCount / len(data) * 100}%')
    print(f'Ilosc gatunku versicolor: {versicolorCount}, procentowo: {versicolorCount / len(data) * 100}%')
    print(f'Ilosc gatunku virginica: {virginicaCount}, procentowo: {virginicaCount / len(data) * 100}%')
    print(f'Wszystkich gatunkow: {len(data)}, procentowo: {len(data) / len(data) * 100}%')

# Wywołanie funkcji countSpecies
countSpecies(data['Gatunek'])

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
fig, axs = plt.subplots(4, 2, figsize=(12, 18))

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

# Generowanie boxplotów
def boxplot_by_species(x, y, feature, ylabel, ylim):

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
plt.subplots_adjust(wspace=0.2, hspace=0.6)

# ------------------- Zadanie 3 -------------------

# Tworzymy nową figurę i ustawiamy jej rozmiar
fig2, axs2 = plt.subplots(3, 2, figsize=(8, 14))

def correlations(row, col, data, data1, desc, desc1):

    # Ustawienie odstępów między wykresami
    plt.subplots_adjust(wspace=0.3, hspace=0.6)

    # Analiza regresji i wykres dla każdej pary cech

    x = data
    y = data1

    # Obliczenie współczynnika korelacji, funkcja corrcoef zwraca macierz korelacji, dlatego wybieramy element [0, 1]
    correlation = np.corrcoef(x, y)[0, 1]

    # Obliczenie parametrów regresji liniowej, funkcja polyfit zwraca współczynniki wielomianu, w tym przypadku liniowego
    slope, intercept = np.polyfit(x, y, 1)

    # Obliczenie wartości na prostej regresji
    regression_line = slope * x + intercept

    # Przypisanie wykresu do odpowiedniej pozycji w siatce (wiersz, kolumna)
    axs2[row, col].scatter(x, y, s=60, edgecolor='none')

    # Dodanie prostej regresji
    axs2[row, col].plot(x, regression_line, color="red")

    # Ustawienia tytułów i etykiet
    axs2[row, col].set_xlabel(desc)
    axs2[row, col].set_ylabel(desc1)

    # Ustawienie zakresu osi x
    axs2[row, col].set_xlim(x.min() - 0.5, x.max() + 0.5)

    # .2f - zaokrąglenie do dwóch miejsc po przecinku
    axs2[row, col].set_title(f'r = {correlation:.2f}; y = {slope:.1f}x + {intercept:.1f}')

# Wywołanie funkcji correlations dla każdej pary cech
correlations(0, 0, data['Dlugosc kielicha'], data['Szerokosc kielicha'], 'Długość działki kielicha (cm)', 'Szerokość działki kielicha (cm)')
correlations(0, 1, data['Dlugosc kielicha'], data['Dlugosc platka'], 'Długość działki kielicha (cm)', 'Długość płatka (cm)')
correlations(1, 0, data['Dlugosc kielicha'], data['Szerokosc platka'], 'Długość działki kielicha (cm)', 'Szerokość płatka (cm)')
correlations(1, 1, data['Szerokosc kielicha'], data['Dlugosc platka'], 'Szerokość działki kielicha (cm)', 'Długość płatka (cm)')
correlations(2, 0, data['Szerokosc kielicha'], data['Szerokosc platka'], 'Szerokość działki kielicha (cm)', 'Szerokość płatka (cm)')
correlations(2, 1, data['Dlugosc platka'], data['Szerokosc platka'], 'Długość płatka (cm)', 'Szerokość płatka (cm)')

# Wyświetlenie wykresów
plt.show()




