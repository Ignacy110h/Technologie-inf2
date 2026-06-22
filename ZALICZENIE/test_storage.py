import tempfile
import unittest
from pathlib import Path

from models import Trening
from storage import wczytaj_treningi, zapisz_trening


class TestZapisuIOdczytu(unittest.TestCase):
    def setUp(self) -> None:
        self.folder = tempfile.TemporaryDirectory()
        self.plik = str(Path(self.folder.name) / "treningi.csv")

    def tearDown(self) -> None:
        self.folder.cleanup()

    def test_pusty_rejestr(self) -> None:
        self.assertEqual(wczytaj_treningi(self.plik), [])

    def test_zapis_i_odczyt_treningu(self) -> None:
        trening = Trening("2026-06-20", "Bieganie", 30)
        zapisz_trening(trening, self.plik)
        self.assertEqual(wczytaj_treningi(self.plik), [trening])

    def test_dopisywanie_treningow(self) -> None:
        treningi = [
            Trening("2026-06-20", "Bieganie", 30),
            Trening("2026-06-21", "Joga", 45),
        ]
        for trening in treningi:
            zapisz_trening(trening, self.plik)
        self.assertEqual(wczytaj_treningi(self.plik), treningi)


if __name__ == "__main__":
    unittest.main()
