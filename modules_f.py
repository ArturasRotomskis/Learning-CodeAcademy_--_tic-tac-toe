"""
-------------------------------------
Basic Python praktinė užduotis [PTU4].
Funkcinis programavimas su moduliais
-------------------------------------
"""
import modules.data


def toe():
    print()
    print("", modules.data.tac[7], "|", modules.data.tac[8], "|", modules.data.tac[9])
    print("---|---|---")
    print("", modules.data.tac[4], "|", modules.data.tac[5], "|", modules.data.tac[6])
    print("---|---|---")
    print("", modules.data.tac[1], "|", modules.data.tac[2], "|", modules.data.tac[3], "")
    print()


while True:
    john = int(input(modules.data.tip + modules.data.john_x))
    modules.data.tac[john] = "X"
    toe()
    if modules.data.filter_tic("X", modules.data.john_win):   # first filtered
        break
    if 0 == john:                                             # first refresh
        print(modules.data.draw)
        tac = [" " for i in modules.data.tac]
    if 10 == john:                                            # first end
        print(modules.data.bye)
        break
    jane = int(input(modules.data.tip + modules.data.jane_o))
    modules.data.tac[jane] = "O"
    toe()
    if modules.data.filter_tic("X", modules.data.jane_win):   # first filtered
        break
    if 0 == jane:                                             # first refresh
        print(modules.data.draw)
        tac = [" " for i in modules.data.tac]
    if 10 == jane:                                            # second end
        print(modules.data.bye)
        break
