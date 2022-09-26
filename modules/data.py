"""
    Data is being exchanged
"""
#######################################################################################################################
JOHN = "John Smith"
JANE = "Jane Smith"
john_win = JOHN + " *** LAIMĖJO ***"
jane_win = JANE + " *** LAIMĖJO ***"
john_x = JOHN + " (X): "
jane_o = JANE + " (O): "
tip = "Žaisdami naudokitės klavišais (1-9), " \
      "norėdami paskelbt lygiąsias ir žaist iš naujo - surinkite 0, " \
      "norėdami išeit - surinkite 10\n -- "
draw = "\n -- Lygiosios-- - žaiskite iš naujo:\n"
bye = "\n- Viso gero ----"
#######################################################################################################################
"""
    DateLine end
"""
tic = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])
tac = [" " for t in range(11)]


def filter_tic(x_or_o, jwin):
    i = 0
    while i < 8:
        win = list(tic[i])
        if tac[win[0]] == tac[win[1]] == tac[win[2]] == x_or_o:
            print(jwin)
            return True
        i += 1
    return False
