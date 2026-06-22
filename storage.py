import csv
from pathlib import Path

from models import Trening


NAGLOWEK = ["data", "nazwa", "czas_minuty"]


def zapisz_trening(trening: Trening, nazwa_pliku: str = "treningi.csv") -> None:
    sciezka = Path(nazwa_pliku)
    nowy_plik = not sciezka.exists() or sciezka.stat().st_size == 0

    with sciezka.open("a", newline="", encoding="utf-8") as plik:
        zapis = csv.writer(plik)
        if nowy_plik:
            zapis.writerow(NAGLOWEK)
        zapis.writerow([trening.data, trening.nazwa, trening.czas_minuty])


def wczytaj_treningi(nazwa_pliku: str = "treningi.csv") -> list[Trening]:
    sciezka = Path(nazwa_pliku)
    if not sciezka.exists():
        return []

    with sciezka.open("r", newline="", encoding="utf-8") as plik:
        return [
            Trening(
                data=wiersz["data"],
                nazwa=wiersz["nazwa"],
                czas_minuty=int(wiersz["czas_minuty"]),
            )
            for wiersz in csv.DictReader(plik)
        ]

