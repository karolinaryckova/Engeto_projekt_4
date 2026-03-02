"""
projekt_4.py: čtvrtý projekt do Engeto Online Python Akademie

author: Karolína Hřivnáč Rycková
email: karolihrivnac@gmail.com
"""
ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")


def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if nazev == "" or popis == "":
            print("Zadal/a jste prázdný vstup. Zkuste to znovu.")
            continue

        # uložíme jako dvojici (název, popis)
        ukoly.append((nazev, popis))
        print("Úkol byl přidán.")
        break


def zobrazit_ukoly():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for i, (nazev, popis) in enumerate(ukoly, start=1):
        print(f"{i}. {nazev} - {popis}")


def odstranit_ukol():
    if len(ukoly) == 0:
        print("Seznam úkolů je prázdný, není co mazat.")
        return

    while True:
        zobrazit_ukoly()
        volba = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()

        if not volba.isdigit():
            print("Neplatný vstup. Zadejte číslo úkolu.")
            continue

        index = int(volba) - 1

        if index < 0 or index >= len(ukoly):
            print("Takový úkol neexistuje. Zkuste to znovu.")
            continue

        ukoly.pop(index)
        print("Úkol byl odstraněn.")
        break


if __name__ == "__main__":
    hlavni_menu()
