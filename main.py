import string



b = int(input())
akcje = [input().strip(' ') for operacja in range(b)]
kasacja = []


#for c in range(b):
    #akcje = eval(input())

class Biblioteka:

    tablica_ksiazek = []
    tablica_egzemplarze = []
    tablica_czytelnicy = []
    def __init__(self, limit):
        self.limit = limit
        
    def __ksiazka_dodaj__(self, ksiazka):
        self.tablica_ksiazek.append(ksiazka)
        return True
        
        
    def oddaj(self, osoba_nazwisko, tytul):
        for czytelnik in self.czytelnicy:
            if czytelnik.nazwisko == osoba_nazwisko:
                for ksiazka_czytelnika in czytelnik.lista_czytelnika:
                    if ksiazka_czytelnika.tytul == tytul:
                        self.ksiazki.append(ksiazka_czytelnika)
                        czytelnik.lista_czytelnika.remove(ksiazka_czytelnika)
                        return True
        return False   
    
    def __wypozyczanie__(self, czytelnik, tytul):
        if len(czytelnik.lista_czytelnika) < 3:
            for ksiazka_wypozyczona in self.ksiazki:
                if ksiazka_wypozyczona.tytul == tytul:
                    for ksiazka_czytelnika in czytelnik.lista_czytelnika:
                        if ksiazka_czytelnika.tytul == tytul:
                            return False
                    czytelnik.lista_czytelnika.append(ksiazka_wypozyczona)
                    self.ksiazki.remove(ksiazka_wypozyczona)
                    return True
        return False
class Ksiazka:
	def __init__(self, tytul, autor, rok):
		self.tytul = tytul
		self.autor = autor
		self.rok = rok


class Pozycja:
	def __init__(self, rok_wydania, wypozyczony):
		self.rok_wydania = rok_wydania
		self.wypozyczony = wypozyczony


class Czytelnik:
	def __init__(self, nazwisko, lista_czytelnika):
		self.nazwisko = nazwisko
		self.lista_czytelnika = lista_czytelnika



wypozyczalnia = Biblioteka(15)
#tytul = tytul.translate(str.maketrans('','',string.punctuation))

for x in akcje:
	#usun = x.translate(str.maketrans('','', string.punctuation))
    tekst = x.replace("(", "")
    tekst2 = tekst.replace(")", "")
    cudzyslow = tekst2.replace("\"", "")
    usun = cudzyslow.split(", ")
    if usun[0].strip() == "dodaj":
        ksiazka = Ksiazka(tytul=usun[1].strip(), autor=usun[2].strip(), rok=usun[3].strip())
        print(wypozyczalnia.dodaj_egzemplarz_ksiazki(ksiazka))
        if usun[0].strip() == "wypozycz":
            wypozyczona = False
            tytul = usun[2].strip()
            for czytelnik in wypozyczalnia.czytelnicy:
                if czytelnik.nazwisko == usun[1].strip():
                    wypozyczona = True
                    print(wypozyczalnia.wypozycz(czytelnik, tytul))
                    break
                if not wypozyczona:
                    nowy_czytelnik = Czytelnik(usun[1].strip(), [])
                    wypozyczalnia.czytelnicy.append(nowy_czytelnik)
                    print(wypozyczalnia.wypozycz(nowy_czytelnik, tytul))
                    if usun[0].strip() == "oddaj":
                        osoba_nazwisko = usun[1].strip()
                        tytul = usun[2].strip()
                        print(wypozyczalnia.oddaj(osoba_nazwisko, tytul))