def noteikt_vecuma_grupu():
    #1. Pieprasa lietotāja vecumu
    ievade = input("Lūdzu, ievadi savu vecumu: ").strip()
    
    #Pārbauda vai ievade ir tukša vai satur nevalīdus datus
    if not ievade:
        print("Kļūda: Ievāde nevar būt tukša!")
        return
        
    try:
        #Mēģina pārveidot ievadi par veselu skaitli
        vecums = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli!")
        return

    #Pārbauda negatīvus skaitļus
    if vecums < 0:
        print("Kļūda: Vecums nevar būt negatīvs skaitlis!")
        return

    #2. un 3. Ar if, elif un else nosaka grupu un izvada rezultātu
    #Vecuma robežas:
    # - Bērns: 0 līdz 12 gadi (ieskaitot)
    # - Pusaudzis: 13 līdz 17 gadi (ieskaitot)
    # - Pieaugušais: 18 līdz 64 gadi (ieskaitot)
    # - Seniors: 65 gadi un vecāki
    
    if vecums <= 12:
        grupa = "bērns"
    elif vecums <= 17:
        grupa = "pusaudzis"
    elif vecums <= 64:
        grupa = "pieaugušais"
    else:
        grupa = "seniors"
        
    print(f"Tava vecuma grupa: {grupa}")

if __name__ == "__main__":
    noteikt_vecuma_grupu()