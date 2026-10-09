#Pajautā, cik skaitļus ievadīs
skaits = int(input("Cik skaitļus tu ievadīszi? "))

summa = 0
pozitivi = 0
negativi = 0
nulles = 0
para = 0
nepara = 0

#Cikls skaitļu saņemšanai
for i in range(skaits):
    skaitlis = int(input(f"Ievadi {i + 1}. skaitli: "))
    
    #Pieskaita summai
    summa += skaitlis
    
    #Skaita pozitīvos, negatīvos un nulles
    if skaitlis > 0:
        pozitivi += 1
    elif skaitlis < 0:
        negativi += 1
    else:
        nulles += 1
        
    #Skaita pāra un nepāra skaitļus
    if skaitlis % 2 == 0:
        para += 1
    else:
        nepara += 1

#Aprēķina vidējo aritmētisko
videjais = summa / skaits

#Izvada rezultātus
print("\nRezultāti:")
print("Summa:", summa)
print("Pozitīvi:", pozitivi)
print("Negatīvi:", negativi)
print("Nulles:", nulles)
print("Pāra:", para)
print("Nepāra:", nepara)
print("Vidējais aritmētiskais:", videjais)