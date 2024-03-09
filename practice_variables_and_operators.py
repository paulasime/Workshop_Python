# Exercitiu 1: Definiți o adresă de memorie care să salveze data curentă. Va fi o variabilă sau o constantă?

CURRENT_DATE = '04-03-2024'   # va fi o constanta

# Exercitiu 2: Identificați tipul de dată pe care îl are variabila
# pe care ați definit-o folosind una din funcțiile învățate la curs.

print(type(CURRENT_DATE))

# Exercitiu 3: Definiți alte câteva variabile care să stocheze cursul la care sunteți,
# ce zi este și la ce sesiune de curs sunteți.

la_ce_curs_sunt = 'Testare automata'
ce_zi_este = '04-03-2024'
la_ce_sesiune_de_curs_suntem = 'Sesiunea 1'

# Exercitiu 4: Salvați fiecare cuvânt din propoziția: “Ana s-a nascut in anul 1990” în câte o adresă de memorie.

cuv1, cuv2, cuv3, cuv4, cuv5, cuv6 = 'Ana', 's-a', 'nascut', 'in', 'anul', '1990'

# sau se poate si cu metoda split

# Exercitiu 5: Printați propoziția de mai sus folosind trei tipuri diferite de printuri.

print(cuv1 + cuv2 + cuv3 + cuv4 + cuv5 + cuv6)  # va returna eroare din cauza nepotrivirii de tip
print(cuv1 + cuv2 + cuv3 + cuv4 + cuv5 + str(cuv6))
print(f"{cuv1} {cuv2} {cuv3} {cuv4} {cuv5} {cuv6}")

# Exercitiu 6: Declarați câteva alte adrese de memorie la alegere și inițializați-le folosind funcția input.

nume = input("Va rugam sa introduceti numele")
prenume = input("Va rugam sa introduceti prenumele")
varsta = input("Va rugam sa introduceti varsta")
adresa = input("Va rugam sa introduceti adresa")
salariu = input("Va rugam sa introduceti salariul")

# Exercitiu 7: Declarați și inițializați câte o variabilă din fiecare din următoarele tipuri de date:
# int, string, float, boolean

varsta = 50
curs = 'Testare Automata'
procent = 20.25
curs_finalizat = True

# Exercitiu 8: Utilizați funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.

assert type(varsta) == int, f"Error: expected bool, actual: {type(varsta)}"

# Scopul sintaxei este de a verifica dacă variabila "varsta" este de tipul int.
# Dacă variabila nu este de tipul int, se va genera o eroare care va indica că se aștepta un întreg (int),
# dar variabila "varsta" este de alt tip. Această verificare este importantă pentru a asigura
# că programul funcționează corect și pentru a evita erorile în timpul executării.

assert type(curs) == str, f"Error: expected bool, actual: {type(curs)}"
assert type(procent) == float, f"Error: expected bool, actual: {type(procent)}"
assert type(curs_finalizat) == bool, f"Error: expected bool, actual: {type(curs_finalizat)}"

# Exercitiu 9: Rotunjiți variabila ‘float’ folosind funcția round() și salvați această modificare
# în aceeași variabilă (suprascriere), apoi verificați din nou tipul de date al acesteia.

print(f"Tipul de date curent este {type(procent)}")
procent = round(procent)
print(f"Noul tip de date este: {type(procent)}")

# Exercitiu 10: Incearcați să convertiti variabila string la int folosind type casting și observați rezultatele.

curs = int(curs)    # returneaza eroare de conversie pentru ca nu putem converti din string in int

# Exercitiu 11: Incearcați să convertiți variabila boolean la int folosind type casting și observați rezultatele.

curs_finalizat = int(curs_finalizat)
print(f"Noua valoare a variabilei curs_finalizat este {curs_finalizat}")

# Exercitiu 12: Schimbați valoarea variabilei boolean (din true în false sau din false în true)
# și repetați exercițiul anterior.

curs_finalizat = False
curs_finalizat = int(curs_finalizat)
print(f"Noua valoare a variabilei curs_finalizat este {curs_finalizat}")

# Exercitiu 13: Folosiți funcția print() și printați în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvați nepotrivirile de tip pe rând prin toate modalitățile cunoscute.

print("La varsta de" + varsta + "ani particip la cursul de" + curs + ". Am parcurs" + procent +
      "% din curs. Cursul e finalizat?" + curs_finalizat)
# Varianta asta va returna eroare pentru ca nu poate face concatenare intre string si int si respectiv string si bool

print("La varsta de" + str(varsta) + "ani particip la cursul de" + curs + ". Am parcurs" + str(procent) +
      "% din curs. Cursul e finalizat?" + str(curs_finalizat))
# Varianta mai buna dar care necesita mult cod scris

print(f"La varsta de {varsta} ani particip la cursul de {curs}. Am parcurs {procent}% din curs. Cursul e finalizat?{curs_finalizat}")
# Cea mai buna varianta

# Exercitiu 14: Citiți de la tastatură numele și prenumele unei persoane și salvați-le în câte o variabilă.
# Afișați pe ecran următoarea propoziție: 'Numele complet are x caractere'.

nume = input("Introduceti numele")
prenume = input("Introduceti prenumele")
nr_caractere = len(nume+prenume)
print(f"Numele complet are {nr_caractere} caractere")

# Exercitiu 15: Citiți de la tastatură lungimea și lățimea unui dreptunghi și salvați-le în câte o variabilă.
# Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.

lungime = float(input("Introduceti lungimea"))
latime = float(input("Introduceti latimea"))
aria = lungime * latime
print(f"Aria dreptungiuliu este {aria}")

# Exercitiu 16: Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# afișați de câte ori apare cuvântul 'the' în acest string

prop = "Coral is either the stupidest animal or the smartest rock"
nr_aparitii = prop.count("the")
print(f"Cuvantul 'the' apare de {nr_aparitii} ori")

# Exercitiu 17: Folosindu-vă de string-ul de la exercițiul 16,
# inlocuiți “the” cu “THE” peste tot (inclusiv în cuvantul “either”) și afișați pe ecran rezultatul

prop = prop.replace("the","THE")
print(f"Noua propozitie este: {prop}")

# Exercitiu 18: Folosindu-vă de string-ul de la exercițiul 16
# si folosiți un assert ca să verificați dacă acest string conține doar numere.

assert prop.isnumeric() == True, f"The string is not numeric"

