from datetime import datetime
from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, szobaszam):
        self.szobaszam = szobaszam
        self.foglalt = False

    @abstractmethod
    def ar(self):
        pass

class EgyagyasSzoba(Szoba):
    def ar(self):
        return 5000

class KetagyasSzoba(Szoba):
    def ar(self):
        return 8000

class Szalloda:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and not szoba.foglalt:
                szoba.foglalt = True
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas.ar()
        return "A szoba nem elérhető."

    def lemondas(self, szobaszam):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam:
                foglalas.szoba.foglalt = False
                self.foglalasok.remove(foglalas)
                return "A foglalás lemondva."
        return "Nincs ilyen foglalás."

    def listazas(self):
        return [(foglalas.szoba.szobaszam, foglalas.datum) for foglalas in self.foglalasok]

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def ar(self):
        return self.szoba.ar()

# Példa használatra
szalloda = Szalloda("Budapest Hotel", [EgyagyasSzoba(101), KetagyasSzoba(102), EgyagyasSzoba(103)])
print(szalloda.foglalas(101, datetime.now()))  # Foglalás létrehozása
print(szalloda.foglalas(101, datetime.now()))  # Próbálkozás ugyanazon szoba foglalásával
print(szalloda.lemondas(101))  # Foglalás lemondása
print(szalloda.listazas())  # Foglalások listázása
