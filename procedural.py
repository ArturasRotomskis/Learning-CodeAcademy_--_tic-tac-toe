"""
Basic Python praktinė užduotis [PTU4].
Procedūrinis programavimas.
-------------------------------------
"""

JOHN = "JOHN Smith **LAIMĖJO**"  # Pirmo žaidėjų pranešimas
JANE = "JANE Smith **LAIMĖJO**"  # Antro žaidėjų pranešimas

tic = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
tac = tic


def toe():  # standartinis print objekto šablonas, žaidimo emuliacijai
    print()
    print("", tac[7], "|", tac[8], "|", tac[9])
    print("---|---|---")
    print("", tac[4], "|", tac[5], "|", tac[6])
    print("---|---|---")
    print("", tac[1], "|", tac[2], "|", tac[3], "")
    print()


while True:  # Leidžiamas ciklas per šabloną
    john = int(input(  # informacijos įvedimas
        "Žaisdami naudokitės klavišais (1-9), "
        "norėdami paskelbt lygiąsias ir žaist iš naujo - surinkite 0, "
        "norėdami išeit - surinkite 10\n -- John Smith (X): "))
    tac[john] = "X"
    toe()
    if 0 == john:  # masyvo išvalymas
        print("\n -- Lygiosios-- - žaiskite iš naujo:\n")
        tic = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        tac = tic
    if tac[1] == tac[2] == tac[3] == "X":  # filtrų blokas
        print(JOHN)
        break
    if tac[4] == tac[5] == tac[6] == "X":
        print(JOHN)
        break
    if tac[7] == tac[8] == tac[9] == "X":
        print(JOHN)
        break
    if tac[1] == tac[4] == tac[7] == "X":
        print(JOHN)
        break
    if tac[2] == tac[5] == tac[8] == "X":
        print(JOHN)
        break
    if tac[3] == tac[6] == tac[9] == "X":
        print(JOHN)
        break
    if tac[1] == tac[5] == tac[9] == "X":
        print(JOHN)
        break
    if tac[3] == tac[5] == tac[7] == "X":
        print(JOHN)
        break
    if 10 == john:  # programos uždarymas
        print("\n- Viso gero ----")
        break
    if tac[1] != " " and tac[2] != " " and tac[3] != " " and tac[4] != " " and tac[5] != " " and tac[6] != " " \
            and tac[7] != " " and tac[8] != " " and tac[9] != " ":  # pilnos lygiosios
        print("\n -- Baigtos lygiosios-- - paspauskit (0) ir žaiskite iš naujo:\n")
# tas pats kodas paleidžiamas oponentui
    jane = int(input(
        "Žaisdami naudokitės klavišais (1-9), "
        "norėdami paskelbt lygiąsias ir žaist iš naujo - surinkite 0, "
        "norėdami išeit - surinkite 10\n -- Jane Smith (O): "))
    tac[jane] = "O"
    toe()
    if 0 == jane:
        print("\n --Lygiosios-- - žaiskite iš naujo:\n")
        tic = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        tac = tic
    if tac[1] == tac[2] == tac[3] == "O":
        print(JANE)
        break
    if tac[4] == tac[5] == tac[6] == "O":
        print(JANE)
        break
    if tac[7] == tac[8] == tac[9] == "O":
        print(JANE)
        break
    if tac[1] == tac[4] == tac[7] == "O":
        print(JANE)
        break
    if tac[2] == tac[5] == tac[8] == "O":
        print(JANE)
        break
    if tac[3] == tac[6] == tac[9] == "O":
        print(JANE)
        break
    if tac[1] == tac[5] == tac[9] == "O":
        print(JANE)
        break
    if tac[3] == tac[5] == tac[7] == "O":
        print(JANE)
        break
    if 10 == jane:
        print("\n- Viso gero ----")
        break
    if tac[1] != " " and tac[2] != " " and tac[3] != " " and tac[4] != " " and tac[5] != " " and tac[6] != " " \
            and tac[7] != " " and tac[8] != " " and tac[9] != " ":
        print("\n -- Baigtos lygiosios-- - paspauskit (0) ir žaiskite iš naujo:\n")
        tic = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        tac = tic
