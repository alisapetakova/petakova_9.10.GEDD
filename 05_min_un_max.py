def main():
    # Pieprasām, cik skaitļus lietotājs ievadīs
    try:
        n = int(input("Ievadi skaitļu skaitu: "))
    except ValueError:
        print("Kļūda: lūdzu ievadi veselu skaitli!")
        return

    # Korekti apstrādājam gadījumu, ja skaitļu skaits ir 0 vai negatīvs
    if n <= 0:
        print("Skaitļu skaitam jābūt lielākam par 0.")
        return

    # Ievadām pirmo skaitli, lai inicializētu mazāko un lielāko vērtību
    try:
        pirmais = float(input("Ievadi 1. skaitli: "))
    except ValueError:
        print("Kļūda: lūdzu ievadi derīgu skaitli!")
        return

    mazakais = pirmais
    lielakais = pirmais

    # Cikls atlikušo skaitļu ievadei un salīdzināšanai
    for i in range(2, n + 1):
        try:
            skaitlis = float(input(f"Ievadi {i}. skaitli: "))
        except ValueError:
            print("Kļūda: lūdzu ievadi derīgu skaitli!")
            return

        # Salīdzinām katru jauno skaitli ar pašreizējo mazāko un lielāko
        if skaitlis < mazakais:
            mazakais = skaitlis
        if skaitlis > lielakais:
            lielakais = skaitlis

    # Izvadām rezultātus
    print("\n--- Rezultāti ---")
    print(f"Mazākā vērtība: {mazakais}")
    print(f"Lielākā vērtība: {lielakais}")


if __name__ == "__main__":
    main()