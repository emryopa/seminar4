#!/usr/bin/env python3

from kostka import Kostka 
from lod import Lod 
import random

class Sektor:
    """
    Sprava souboje dvou lodí:
    """

    def __init__(self, lod_1, lod_2, kostka, jmeno="bez nazvu"):
        self._jmeno = jmeno
        self._lod_1 = lod_1
        self._lod_2 = lod_2
        self._kostka = kostka

    def _vycisti(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith('win'):
            _subprocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subprocess.call(['clear'])

    def _vypis_lod(self, lod):
        print(lod)
        print(f'Trup: {lod._trup}\n')

    def _vykresli(self):
        self._vycisti()
        print(f'============== {self._jmeno} ==============\n')
        print('Lodě:')
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print()

    def souboj(self):
        print(f"Vítej v sektoru {self._jmeno}!")
        print ("============================")
        print(f"Dnes se utkají lodě:")
        self._vypis_lod(self._lod_1)
        self._vypis_lod(self._lod_2)
        print("Zahájit soubor...")
        input()

        if random.randint(0, 1):
            self._lod_1, self._lod_2 = self._lod_2, self._lod_1

        while self._lod_1.je_operacni() and self._lod_2.je_operacni():
            self._lod_1.utoc(self._lod_2)
            self._vykresli()
            self._vypis_zpravu(self._lod_1.vypis_zpravu())
            self._vypis_zpravu(self._lod_2.vypis_zpravu())

            if self._lod_2.je_operacni():
                self._lod_2.utoc(self._lod_1)
                self._vykresli()
                self._vypis_zpravu(self._lod_2.vypis_zpravu())
                self._vypis_zpravu(self._lod_1.vypis_zpravu())

    def _vypis_zpravu(self, zprava):
        import time as _time
        if zprava:
            print(zprava)
            _time.sleep(1.5)

if __name__ == '__main__':
    k = Kostka(10)
    lodicka = Lod("Velká bárka", trup=100, utok=70, stit=40, kostka=k)
    clun = Lod ("Křehká bárka", 140, 35, 30, k)
    barka = Lod("Plachetnice", 120, 40, 50, k)
    pole = Sektor(lodicka, clun, k, "Bojové pole")
    gamma = Sektor(lodicka, barka, k, "Gamma")

    pole.souboj()
    gamma.souboj()