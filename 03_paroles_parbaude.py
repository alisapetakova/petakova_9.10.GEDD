#Pareizā parole ir saglabāta mainīgajā
pareiza_parole = "alisap228"
atlikušie_mēģinājumi = 3

while atlikušie_mēģinājumi > 0:
    ievadītā_parole = input("Ievadi paroli: ")
    
    if ievadītā_parole == pareiza_parole:
        print("Piekļuve atļauta")
        break
    else:
        atlikušie_mēģinājumi -= 1
        if atlikušie_mēģinājumi > 0:
            print(f"Nepareiza parole. Atlicis mēģinājumu: {atlikušie_mēģinājumi}")
        else:
            print("Piekļuve bloķēta")