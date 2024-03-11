# Definiti o funcție care să returneze TRUE dacă un număr este par sau FALSE
# daca numarul este impar

def par_impar(nr):
 if nr%2 == 0:
   return "par"
 else:
   return "impar"


# Definiti o funcție fără return care primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y

def numar_caractere(text):
 nr_lower=0
 nr_upper=0
 for i in range(len(text)):
   if text[i].islower():
     nr_lower+=1
   else:
     nr_upper+=1
 print(f"Lowercase: {nr_lower}, uppercase: {nr_upper}")


# Definiti o funcție care primește o listă de cifre (adică doar 0-9)
# si care returnează un dictionar care va contina cifra ca si cheie si numarul
# de aparitii ale acelei cifre ca valoare

def numar_aparitii(lista_cifre):
 dictionar_aparitii={}
 for i in range(len(lista_cifre)):
   if lista_cifre[i] not in dictionar_aparitii.keys():
     dictionar_aparitii[lista_cifre[i]]=1
   else:
     dictionar_aparitii[lista_cifre[i]] = dictionar_aparitii[lista_cifre[i]]+1
 return dictionar_aparitii


# Definiti o funcție care primește 3 numere si returnează valoarea maximă dintre ele.

def calculeaza_max(nr1,nr2,nr3):
 max = 0
 if nr1 > max:
   max =  nr1
 if nr2 > max:
   max =  nr2
 if nr3 > max:
   max = nr3
 return max


# Definiti o funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.

def suma_numere(nr):
 suma = 0
 for i in range(len(nr)):
   suma+=i
 return suma


# Definiti o funcție care sa primească 2 liste de numere (numerele pot fi dublate)
# si sa returneze numerele comune.

def numere_comune(list1, list2):
 return list(set(list1).intersection(list2))

# sau

def numere_comune(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    numere_comune = set1.intersection(set2)
    return list(numere_comune)

# Exemplu de utilizare

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
print(numere_comune(lista1, lista2))  # Output: [3, 4, 5]


# Definiti o funcție care să aplice o reducere de preț.
# Dacă produsul costă peste 100 lei se aplicăm o reducere de 10%.
# Altfel, nu se va aplica nicio reducere

def reducere_pret(pret):
 if pret > 100:
   discount = 0.1
 return pret - pret * discount

