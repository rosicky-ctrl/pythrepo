from calc import *

menu()

funkcje = {'1': dodawanie, '2': odejmowanie, '3': mnozenie, '4': dzielenie, '5': dzieleniecal, '6': potegowanie,
           '7': autor, '8': zakoncz}
nazwyFunkcji = {'1': 'dodawanie', '2': 'odejmowanie', '3': 'mnożenie', '4': 'dzielenie', '5': 'dzielenie całkowite',
                '6': 'potęgowanie', '7': 'autor', '8': 'zakończ'}

operacja = input("Co wybierasz?")
while operacja != "8":
    wybranaFkcja = funkcje.get(operacja, blad)
    nazwaWybranejFkcji = nazwyFunkcji.get(operacja, blad)
    print(nazwaWybranejFkcji)
    print(wybranaFkcja())
    operacja = input("Co wybierasz? ")
print("Koniec")