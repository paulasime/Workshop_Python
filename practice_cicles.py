# Tipăriţi toate numerele prime aflate între două numere naturale citite de la tastatura

nr1 = int(input("Primul numar "))
nr2 = int(input("Al doilea numar "))
nume_prime = []
for i in range(nr1, nr2+1):
 is_prime = 1
 for j in range(2,i+1):
  if (i % j) == 0 and i!=j:
   is_prime = 0
   continue
 if is_prime and i not in nume_prime:
    nume_prime.append(i)
print(nume_prime)


# Se citește un număr natural n. Să se scrie programul care determină și afișează
# câte cifre impare are numărul citit.

numar = input("Cititi numarul ")
nr_cifre_impare = 0
for i in range(len(numar)):
 if int(numar[i])%2!=0:
   nr_cifre_impare+=1
print(f"Numarul {numar} are {nr_cifre_impare} cifre impare")


# Se citește un număr natural n. Să se scrie programul care determină
# și afișează numărul de cifre ale lui n

numar = input("Cititi numarul ")
print(f"Numarul {numar} are {len(numar)} cifre")


# Se citește un număr natural n. Să se scrie programul care verifică dacă
# numărul citește palindrom

numar = input("Cititi numarul ")

if numar == numar[::-1]:
print("Numarul este palindrom")
else:
 print("Numarul nu este palindrom")

# sau

e_palindrom = True
for i in range(len(numar)):
 if numar[i]!=numar[len(numar)-i-1]:
   e_palindrom = False
print(f"Numarul {numar} e palindrom? {e_palindrom}")


# Se citește un număr natural n. Să se scrie programul care determină și
# afișează cea mai mare și cea mai mică cifră a numărului n.

numar = input("Citeste numarul ")
max = 0
min = 99999999999999
for i in range(len(numar)):
 if int(numar[i])>int(max):
   max = numar[i]
 if int(numar[i])<int(min):
   min = numar[i]

print(f"Cifra maxima e {max}")
print(f"Cifra minima e {min}")


# Se citesc n numere întregi. Se cere: suma numerelor citite, maximul, minimul,
# câte sunt negative, câte sunt pare/impare, cel mai mare număr negativ/pozitiv

numere = [12, 456, 35, 1256, 1, 0, 48576]
suma = 0
max = 0
min = 0
numar_negative = 0
numar_pare = 0
numar_impare = 0
cel_mai_mic_pozitiv = 0
cel_mai_mic_negativ = 0

for numar in (numere):
 suma+=numar
 if numar>max:
   max = numar
 if max<min:
   min = min
 if numar >=0 and numar<cel_mai_mic_pozitiv:
   cel_mai_mic_pozitiv = numar
 elif numar<0 and numar !=-1 and numar < cel_mai_mic_negativ:
   cel_mai_mic_negativ = numar
   numar_negative+=1
 if numar%2==0:
   numar_pare+=1
 else:
   numar_impare+=1

print(f"Suma este: {suma}, numarul maxim este: {max} numarul minim este: {min} \n"
  f"Sunt in total {numar_negative} numere negative, {numar_pare} numere pare \n"
  f"{numar_impare} numere impare \n"
  f"Cel mai mic numar pozitiv este {cel_mai_mic_pozitiv} \n"
  f"Cel mai mic numar negativ este {cel_mai_mic_negativ} \n")

