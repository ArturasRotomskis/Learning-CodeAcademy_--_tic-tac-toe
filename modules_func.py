"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas su moduliais
-------------------------------------
"""
from modules.data import tic, tac, tip, draw, bye, smith_win, smith_choise, s, smith_num, swap_s, swap_smith_num


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


def main(i):  # executions input
    tac[smith] = i
    toe()


def main_draw():  # full gaming draw
    if tac[1] != " " and tac[2] != " " and tac[3] != " " and tac[4] != " " and tac[5] != " " and tac[6] != " " \
            and tac[7] != " " and tac[8] != " " and tac[9] != " ":
        print("real (full)" + draw)


while True:
    # ---- trigger flow mode - ###############################
    smith = int(input(tip + smith_choise[smith_num]))
    main(s)
    if filter_tic(s, smith_win[smith_num]):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
    (smith_num, swap_smith_num) = (swap_smith_num, smith_num)
    (s, swap_s) = (swap_s, s)
