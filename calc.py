def menu():
    print ("::MENU::\n"
        "1 - dodawanie\n"
        "2 - odejmowanie\n"
        "3 - mnożenie\n"
        "4 - dzielenie\n"
        "5 - dzielenie całkowite\n"
        "6 - potęgowanie\n"
        "7 - autor\n"
        "8 - koniec\n")

def dodawanie():
    x = input("Pierwsza liczba ")
    y = input("Druga liczba ")
    wynik = float(x) + float(y)
    return wynik

def odejmowanie():
    x = input("Pierwsza liczba ")
    y = input("Druga liczba ")
    wynik = float(x) - float(y)
    return wynik

def mnozenie():
    x = input("Pierwsza liczba ")
    y = input("Druga liczba ")
    wynik = float(x) * float(y)
    return wynik

def dzielenie():
    x = input("Pierwsza liczba ")
    y = input("Druga liczba ")
    wynik = float(x) / float(y)
    return wynik

def dzieleniecal():
    x = input("Pierwsza liczba ")
    y = input("Druga liczba ")
    dziel = int(x) / int(y)
    reszta = int(x) % int(y)
    wynik = "wynik", dziel, "reszty", reszta
    return wynik

def potegowanie():
    x = input("Liczba ")
    y = input("Potęga ")
    wynik = float(x) ** float(y)
    return wynik

def autor():
    return "Marcin Wójcik - informatyka stosowana - 210436"

def blad():
    return 'Error'

def zakoncz():
    return 'koniec'