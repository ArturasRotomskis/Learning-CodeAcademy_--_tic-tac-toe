from modules.data import tac, tip, draw, bye, s, smith_num, smith_win, smith_choise, swap_s, swap_smith_num, \
    filter_tic, main_draw

"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas su moduliais
-------------------------------------
"""


def toe():  # console frontend
    print()
    print("", tac[7], "|", tac[8], "|", tac[9])
    print("---|---|---")
    print("", tac[4], "|", tac[5], "|", tac[6])
    print("---|---|---")
    print("", tac[1], "|", tac[2], "|", tac[3], "")
    print()


while True:
    # ---- trigger flow mode - ###############################
    smith = int(input(tip + smith_choise[smith_num]))
    tac[smith] = s
    toe()
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
