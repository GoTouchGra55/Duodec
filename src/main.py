from duodec import Duodec
from kmk.keys import KC
from kmk.modules.layers import Layers

layers = Layers()
Duodec.modules.append(layers)

# Placeholder functions for now
keyMap = [
  [
    KC.F1,  KC.F2,  KC.F3,  KC.F4,
    KC.F5,  KC.F6,  KC.F7,  KC.F8,
    KC.F9,  KC.F10, KC.F11, KC.F12
  ]
]

if __name__ == "__main__":
  Duodec.go()