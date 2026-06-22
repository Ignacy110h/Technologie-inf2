from models import Trening
from storage import wczytaj_treningi, zapisz_trening


def pobierz_dodatnia_liczbe(komunikat: str) -> int:
    while True:
        try:
            liczba = int(input(komunikat))
            if liczba > 0:
                return liczba
        except ValueError:
            pass
        print("Wpisz dodatnią liczbę całkowitą.")


def dodaj_trening() -> None:
    print("\nDODAWANIE TRENINGU")
    data = input("Data (np. 2026-06-20): ").strip()
    nazwa = input("Nazwa treningu: ").strip()
    czas = pobierz_dodatnia_liczbe("Czas w minutach: ")
    zapisz_trening(Trening(data, nazwa, czas))
    print("Trening został zapisany.")


def pokaz_treningi() -> None:
    treningi = wczytaj_treningi()
    if not treningi:
        print("\nBrak zapisanych treningów.")
        return

    print("\nZAPISANE TRENINGI")
    for numer, trening in enumerate(treningi, start=1):
        print(
            f"{numer}. {trening.data} | {trening.nazwa} | "
            f"{trening.czas_minuty} min"
        )


def main() -> None:
    while True:
        print("\n===== REJESTR TRENINGÓW =====")
        print("1. Zapisz trening")
        print("2. Odczytaj treningi")
        print("0. Zakończ")
        wybor = input("Wybierz opcję: ").strip()

        if wybor == "1":
            dodaj_trening()
        elif wybor == "2":
            pokaz_treningi()
        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Nie ma takiej opcji.")


if __name__ == "__main__":
    main()

