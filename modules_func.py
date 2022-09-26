"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas su moduliais
-------------------------------------
"""
from modules.data import tic, tac, tip, draw, bye, smith_win, smith_choise


def toe():  # console frontend
    print()
    print("", tac[7], "|", tac[8], "|", tac[9])
    print("---|---|---")
    print("", tac[4], "|", tac[5], "|", tac[6])
    print("---|---|---")
    print("", tac[1], "|", tac[2], "|", tac[3], "")
    print()


def filter_tic(x_or_o, js):  # defined filter
    i = 0
    while i < 8:
        win = list(tic[i])
        if tac[win[0]] == tac[win[1]] == tac[win[2]] == x_or_o:
            print(js)
            return True
        i += 1
    return False


def main(i):
    tac[smith] = i
    toe()


def main_draw():
    if tac[1] != " " and tac[2] != " " and tac[3] != " " and tac[4] != " " and tac[5] != " " and tac[6] != " " \
            and tac[7] != " " and tac[8] != " " and tac[9] != " ":
        print("real" + draw)


while True:
    # ---- trigger flow mode - ###############################
    j = "X"
    smith = int(input(tip + smith_choise[1]))
    main(j)
    if filter_tic(j, smith_win[1]):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
    # - separated player ---- ################################
    j = "O"
    smith = int(input(tip + smith_choise[1+1]))
    main(j)
    if filter_tic(j, smith_win[1+1]):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
