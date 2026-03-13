import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation

Duodec = KMKKeyboard()

# 4 columns
Duodec.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8)

# 3 rows
Duodec.row_pins = (board.GP2, board.GP3, board.GP4)

Duodec.diode_orientation = DiodeOrientation.COL2ROW