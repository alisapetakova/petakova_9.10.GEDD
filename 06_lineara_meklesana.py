#Definējam doto sarakstu
skaitli = [4, 7, 2, 9, 7, 1]

#Pieprasām lietotājam ievadīt meklējamo skaitli, apstrādājot iespējamo nederīgo ievadi
try:
    meklejamais = int(input("Ievadi meklējamo skaitli: "))
except ValueError:
    print("Nederīga ievade! Lūdzu, ievadi veselu skaitli.")
    exit()

#Mainīgie meklēšanai
pirmais_indekss = -1
visi_indeksi = []

#Cikls saraksta elementu pārbaudei pēc kārtas (lineārā meklēšana)
for indekss in range(len(skaitli)):
    if skaitli[indekss] == meklejamais:
        #Saglabājam pirmo atrasto indeksu (ja tas vēl nav atrasts)
        if pirmais_indekss == -1:
            pirmais_indekss = indekss
        #Pievienojam indeksu sarakstam (papildu līmenim)
        visi_indeksi.append(indekss)

#Rezultātu izvade
if pirmais_indekss != -1:
    print(f"Pirmais indekss, kurā skaitlis atrasts: {pirmais_indekss}")
    print(f"Visi indeksi, kuros vērtība atrasta: {visi_indeksi}")
else:
    print("Nav atrasts")