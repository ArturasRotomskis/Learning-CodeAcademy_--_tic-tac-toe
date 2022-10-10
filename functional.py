"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas.
-------------------------------------
"""
#######################################################################################################################
smiths = ["", "John Smith", "Jane Smith"]
x_win = ("", (smiths[1] + " *** WINS ***"), (smiths[2] + " *** WINS ***"))
x_choise = ("", (smiths[1] + " (X): "), (smiths[2] + " (O): "))
tip = "Use the keyboard (1-9) to play, to declare a draw and play again press (0), " \
      "needed turn off choose (10)\n -- "
draw = "\n -- a Draw -- - play again:\n"
bye = "\n- Good bye ----"
#######################################################################################################################
tic = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])
tac = [" " for t in range(11)]
# -- triggers variables - ######################################
x_num = 1; o_num = 2
x = "X"; o = "O"


def toe():  # console frontend
    print()
    print("", tac[7], "|", tac[8], "|", tac[9])
    print("---|---|---")
    print("", tac[4], "|", tac[5], "|", tac[6])
    print("---|---|---")
    print("", tac[1], "|", tac[2], "|", tac[3], "")
    print()


def main(s):  # executions input
    tac[smith] = s
    toe()


def filter_tic(x_o, s_win):  # defined filter
    for s in range(0, 8):
        win = list(tic[s])
        if tac[win[0]] == tac[win[1]] == tac[win[2]] == x_o:
            print(s_win)
            return True
    return False


def main_draw():  # full gaming draw
    tac[0], tac[10] = ".", "."
    if " " in tac: pass
    else: toe(); print("real (full)" + draw)


while True:
    # ---- trigger flow mode - ################################
    smith = int(input(tip + x_choise[x_num]))
    main(x)
    if filter_tic(x, x_win[x_num]):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
    (x, o) = (o, x)
    (x_num, o_num) = (o_num, x_num)
