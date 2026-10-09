def izvedot_reizinasanas_tabulu():
    #Pārbaudām ievadi, lai nodrošinātu, ka lietotājs ievada veselu skaitli
    ievade = input("Ievadi veselu skaitli: ")
    
    try:
        skaitlis = int(ievade)
    except ValueError:
        print("Kļūda: Lūdzu, ievadi derīgu veselu skaitli, nevis tekstu!")
        return

    #Ar for ciklu izvadām reizināšanas tabulu no 1 līdz 10
    for i in range(1, 11):
        rezultats = skaitlis * i
        print(f"{skaitlis} x {i} = {rezultats}")

if __name__ == "__main__":
    izvedot_reizinasanas_tabulu()