#!/usr/bin/env python3

from kostka import Kostka 
from lod import Lod 

class Sektor:
    """
    Sprava souboje dvou lodí:
    """

    def __init__(self, lod_1, lod_2, kostka):
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def souboj(self):
        print("Vítej v sektoru Bojové pole!")
        print ("============================")
        print(f"Dnes se utkají lodě {self._lod_1} a {self._lod_2}.")
        print("Zahájit soubor...")
        input()

        self._lod_1.utoc(self._lod_2)
        self._vypis_zpravu(self._lod_1.vypis_zpravu())
        self._vypis_zpravu(self._lod_2.vypis_zpravu())
        self._lod_2.utoc(self._lod_1)
        self._vypis_zpravu(self._lod_2.vypis_zpravu())
        self._vypis_zpravu(self._lod_1.vypis_zpravu())

    def _vypis_zpravu(self, zprava):
        print(zprava)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Mega Killer", 100, 80, 50, k)
    clun = Lod ("Small Killer", 40, 20, 30, k)
    pole = Sektor(lodicka, clun, k)

    pole.souboj()
