from modules.data import tac, toe, tip, draw, bye, \
    s, smith_num, smith_win, smith_choise, swap_s, swap_smith_num, \
    filter_tic, main_draw
"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas su moduliais
-------------------------------------
"""
toe()  # console frontend


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
