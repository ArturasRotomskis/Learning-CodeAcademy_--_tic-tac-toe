"""
    Data is being exchanged
"""
#######################################################################################################################
smiths = ["", "John Smith", "Jane Smith"]
smith_win = ("", (smiths[1] + " *** WINS ***"), (smiths[2] + " *** WINS ***"))
smith_choise = ("", (smiths[1] + " (X): "), (smiths[2] + " (O): "))
tip = "Use the keyboard (1-9) to play, to declare a draw and play again press (0), " \
      "needed turn off choose (10)\n -- "
draw = "\n -- a Draw -- - play again:\n"
bye = "\n- Good bye ----"
#######################################################################################################################
"""
    DateLine end
"""
tic = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])
tac = [" " for t in range(11)]

smith_num = 1
s = "X"
swap_smith_num = 2
swap_s = "O"