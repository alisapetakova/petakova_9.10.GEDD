# Fails: 04_summa_lidz_n.py

ievade = input("Ievadi veselu pozitīvu skaitli n: ")

# Pārbaudām, vai ievade ir skaitlis
if ievade.lstrip('-').isdigit():
    n = int(ievade)
    
    # Pārbaudām, vai skaitlis ir lielāks par 0
    if n > 0:
        summa = 0
        for i in range(1, n + 1):
            summa += i
        print("Rezultāts:", summa)
    else:
        print("Kļūda: Skaitlim jābūt lielākam par 0!")
else:
    print("Kļūda: Ievadīta nederīga vērtība vai tukšums!")