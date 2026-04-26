import time
import busio
import board
import usb_hid
import digitalio
import adafruit_ssd1306

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC

# kmk setup
Duodec = KMKKeyboard()

Duodec.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8)
Duodec.row_pins = (board.GP2, board.GP3, board.GP4)
Duodec.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
Duodec.modules.append(layers)

# Add your custom keymaps here and dont forget to add stuff to the modes list below!
keyMap = [
    # HOME
    [
        KC.LCTL(KC.LALT(KC.L)), KC.LCTL(KC.LALT(KC.S)), KC.LCTL(KC.LALT(KC.B)), KC.LCTL(KC.LALT(KC.G)),
        KC.LALT(KC.H), KC.LCTL(KC.LALT(KC.C)), KC.LCTL(KC.LALT(KC.K)), KC.LCTL(KC.LALT(KC.T)),
        KC.LCTL(KC.LALT(KC.M)), KC.LCTL(KC.LALT(KC.O)), KC.LCTL(KC.LALT(KC.P)), KC.LCTL(KC.LALT(KC.V))
    ],

    # BRAVE (I'm a brave user :3)
    [
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO
    ],

    # DEV
    [
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO
    ],

    # MEDIA
    [
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

Duodec.keymap = keyMap

# Edit this according to your keymaps
modes = ["HOME", "BROWSER", "DEV", "MEDIA"] 

# Display stuff
i2c = busio.I2C(board.GP1, board.GP0)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

cc = ConsumerControl(usb_hid.devices)

# Encoder stuff
a = digitalio.DigitalInOut(board.GP27)
b = digitalio.DigitalInOut(board.GP28)
btn = digitalio.DigitalInOut(board.GP29)

a.switch_to_input(pull=digitalio.Pull.UP)
b.switch_to_input(pull=digitalio.Pull.UP)
btn.switch_to_input(pull=digitalio.Pull.UP)

current_layer = 0
last_a = a.value

# State
muted = False
last_btn = btn.value
last_draw = None

# Layer Control
def set_layer(index):
    global current_layer
    current_layer = index % len(modes)
    Duodec.active_layers = [current_layer]

# init layer
set_layer(0)

# Switch Layer
def read_encoder():
    global last_a

    a_state = a.value
    b_state = b.value

    if a_state != last_a:
        if a_state:
            if b_state:
                set_layer(current_layer - 1)  # counter-clockwise
            else:
                set_layer(current_layer + 1)  # clockwise

        last_a = a_state

# Encoder Btn 
def read_button():
    global muted, last_btn

    if last_btn and not btn.value:
        muted = not muted
        cc.send(ConsumerControlCode.MUTE)

    last_btn = btn.value

# Display 
def draw():
    global last_draw

    display_value = "MUTED" if muted else "ACTIVE"
    screen = modes[current_layer] + display_value

    if screen == last_draw:
        return

    oled.fill(0)
    oled.text("DUODEC v1", 0, 0, 1)
    oled.text("MODE: " + modes[current_layer], 0, 10, 1)
    oled.text("STATUS: " + display_value, 0, 20, 1)
    oled.show()

    last_draw = screen

def after_matrix_scan():
    read_encoder()
    read_button()
    draw()

Duodec.after_matrix_scan = after_matrix_scan()

if __name__ == "__main__":
    Duodec.go()
