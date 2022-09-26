"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas.
-------------------------------------
"""
#######################################################################################################################
JOHN = "John Smith"
JANE = "Jane Smith"
john_win = JOHN + " *** WINS ***"
jane_win = JANE + " *** WINS ***"
john_x = JOHN + " (X): "
jane_o = JANE + " (O): "
tip = "Use the keyboard (1-9) to play, to declare a draw and play again press (0), " \
      "needed turn off choose (10)\n -- "
draw = "\n -- a Draw -- - play again:\n"
bye = "\n- Good bye ----"
#######################################################################################################################
tic = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])
tac = [" " for t in range(11)]


def toe():  # console frontend
    print()
    print("", tac[7], "|", tac[8], "|", tac[9])
    print("---|---|---")
    print("", tac[4], "|", tac[5], "|", tac[6])
    print("---|---|---")
    print("", tac[1], "|", tac[2], "|", tac[3], "")
    print()


def main(i):
    tac[smith] = i
    toe()


def filter_tic(x_or_o, j_win):  # defined filter
    i = 0
    while i < 8:
        win = list(tic[i])
        if tac[win[0]] == tac[win[1]] == tac[win[2]] == x_or_o:
            print(j_win)
            return True
        i += 1
    return False


def main_draw():
    if tac[1] != " " and tac[2] != " " and tac[3] != " " and tac[4] != " " and tac[5] != " " and tac[6] != " " \
            and tac[7] != " " and tac[8] != " " and tac[9] != " ":
        print(draw)


while True:
    # ---- trigger flow mode - ###############################
    smith = int(input(tip + john_x))
    main("X")
    if filter_tic("X", john_win):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
    # - separated player ---- ################################
    smith = int(input(tip + jane_o))
    main("O")
    if filter_tic("O", jane_win):
        break
    if 0 == smith:
        print(draw)
        tac = [" " for i in tac]
    if 10 == smith:
        print(bye)
        break
    main_draw()
