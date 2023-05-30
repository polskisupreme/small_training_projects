# zad 1
liczba_poczatkowa = int(input('Podaj liczbe poczatkowa: '))
liczba_koncowa = int(input('Podaj liczbe koncowa: '))

odstep_miedzy_liczbami = liczba_koncowa - liczba_poczatkowa

print('Odstep miedzy liczbami wynosi: ', odstep_miedzy_liczbami)

# zad 2
komunikat = str(input('Podaj swoj komunikat: '))

print(komunikat[::-1])

# zad 3
import random

lista_slow = ["wakacje", "kot", "samochód", "dom", "programowanie", "funkcja", "komputer"]

slowo = random.choice(lista_slow)

print(f"Zgadnij wybrane słowo. Ma ono {len(slowo)} liter.")

odgadywane_litery = []

for i in range(5):
    litera = input("Podaj literę: ")

    if litera in odgadywane_litery:
        print("Ta litera została już wcześniej odgadnięta.")
        continue

    odgadywane_litery.append(litera)

    if litera in slowo:
        print("Tak")
    else:
        print("Nie")

    zgadywanie_slowa = input("Czy chcesz spróbować odgadnąć całe słowo? Wpisz tak lub nie: ")
    if zgadywanie_slowa.lower() == "tak":
        slowo_gracza = input("Podaj słowo: ")

        if slowo_gracza == slowo:
            print("Brawo! Odgadłeś słowo!")
            break
        else:
            print("Niestety, to nie jest poprawne słowo.")

    if set(slowo) == set(odgadywane_litery):
        print("Brawo! Odgadłeś wszystkie litery i wygrałeś grę!")
        break

    if i == 4:
        print("Niestety, przegrałeś grę. Szukane słowo to:", slowo)

# zad 4
import random

lista_slow = ['python', 'programowanie', 'kodowanie', 'algorytm', 'funkcja']


def losuj_haslo(lista_slow):
    return random.choice(lista_slow)


def sprawdz_litere(litera, haslo, zgadniete_litery):
    if litera in zgadniete_litery:
        print("Już zgadłeś literę", litera)
        return zgadniete_litery
    elif litera in haslo:
        print("Tak, litera", litera, "znajduje się w haśle!")
        zgadniete_litery.append(litera)
        return zgadniete_litery
    else:
        print("Niestety, litera", litera, "nie znajduje się w haśle.")
        return zgadniete_litery


def rysuj_szubienice(liczba_bledow):
    if liczba_bledow == 0:
        print(" _______ ")
        print("|       |")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|__________")
    elif liczba_bledow == 1:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|__________")
    elif liczba_bledow == 2:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|       |")
        print("|       ")
        print("|       ")
        print("|__________")
    elif liczba_bledow == 3:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|      /|")
        print("|       ")
        print("|       ")
        print("|__________")
    elif liczba_bledow == 4:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|       ")
        print("|       ")
        print("|__________")
    elif liczba_bledow == 5:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / ")
        print("|       ")
        print("|__________")
    else:
        print(" _______ ")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / \\")
        print("|       ")
        print("|__________")


def sprawdz_wygrana(haslo, zgadniete_litery):
    for litera in haslo:
        if litera not in zgadniete_litery:
            return False
    return True


def graj():
    haslo = losuj_haslo(lista_slow)
    zgadniete_litery = []
    liczba_bledow = 0
    koniec_gry = False

    while not koniec_gry:
        rysuj_szubienice(liczba_bledow)
        print("Zgadnij literę:", end=" ")
        for litera in haslo:
            if litera in zgadniete_litery:
                print(litera, end=" ")
        else:
            print("_", end=" ")
        print("")
        litera = input()
        zgadniete_litery = sprawdz_litere(litera, haslo, zgadniete_litery)
        if litera not in haslo:
            liczba_bledow += 1
        if liczba_bledow == 6:
            koniec_gry = True
            print("Niestety, przegrałeś. Szukane słowo to", haslo)
        else:
            if sprawdz_wygrana(haslo, zgadniete_litery):
                koniec_gry = True
                print("Gratulacje, wygrałeś! Szukane słowo to", haslo)


graj()

#zad 5
def rysuj_plansze(plansza):
    print(plansza[0] + " | " + plansza[1] + " | " + plansza[2])
    print("---------")
    print(plansza[3] + " | " + plansza[4] + " | " + plansza[5])
    print("---------")
    print(plansza[6] + " | " + plansza[7] + " | " + plansza[8])

def sprawdz_wygrana(plansza, znak):
    if (plansza[0] == znak and plansza[1] == znak and plansza[2] == znak) or \
            (plansza[3] == znak and plansza[4] == znak and plansza[5] == znak) or \
            (plansza[6] == znak and plansza[7] == znak and plansza[8] == znak) or \
            (plansza[0] == znak and plansza[3] == znak and plansza[6] == znak) or \
            (plansza[1] == znak and plansza[4] == znak and plansza[7] == znak) or \
            (plansza[2] == znak and plansza[5] == znak and plansza[8] == znak) or \
            (plansza[0] == znak and plansza[4] == znak and plansza[8] == znak) or \
            (plansza[2] == znak and plansza[4] == znak and plansza[6] == znak):
        return True
    else:
        return False

def graj():
    plansza = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    kolej_gracza = "X"
    koniec_gry = False

    while not koniec_gry:
        rysuj_plansze(plansza)
        print("Gracz", kolej_gracza, "wybierz pole (1-9):")
        pole = int(input()) - 1
        if plansza[pole] != " ":
            print("To pole jest już zajęte. Wybierz inne pole.")
        else:
            plansza[pole] = kolej_gracza
            if sprawdz_wygrana(plansza, kolej_gracza):
                rysuj_plansze(plansza)
                print("Gracz", kolej_gracza, "wygrał!")
                koniec_gry = True
            elif " " not in plansza:
                rysuj_plansze(plansza)
                print("Remis!")
                koniec_gry = True
            else:
                if kolej_gracza == "X":
                    kolej_gracza = "O"
                else:
                    kolej_gracza = "X"

graj()
