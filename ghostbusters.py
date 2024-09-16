import random

def najdi_ducha():
    print("Vítejte ve hře 'Najdi Ducha'!")
    print("Za jedněmi ze tři dveří se skrývá duch.")
    print("Pokud najdete ducha, získáte bod a můžete pokračovat.")
    print("Pokud se netrefíte, hra končí.")
    print("Hodně štěsti!\n")

    score = 0

    while True:
        duch = random.randint(1, 3)

        while True:
            try: 
                volba = int(input("Vyberte dveře (1, 2 nebo 3): "))
                if volba in [1, 2, 3]:
                    break
                else:
                    print("Neplatná volba, prosím zadejte číslo 1, 2 nebo 3.")
            except ValueError:
                print("Neplatná volba, prosím zadejte číslo 1, 2 nebo 3.")                  

        if volba == duch:
            score += 1
            print(f"Gratulujeme! Našli jste ducha za dveřmi {duch}.")        
            print(f"Vaše aktuální skóre je: {score}")
            print("Pokračujete ve hře!\n")
        else:
            print(f"Bohužel, za dveřmi {volba} není duch. Duch byl za dveřmi {duch}.")
            print(f"Vaše konečné skóre je: {score}")
            print("Děkujeme za hru! Můžete to zkusit znovu.\n")
            break

najdi_ducha()
