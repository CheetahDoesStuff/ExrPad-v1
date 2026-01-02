from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

keyboard = KMKKeyboard()

keyboard.direct_pins = (
    board.GP28,
    board.GP29,
    board.GP3,
    board.GP4,
    board.GP2,
    board.GP1,
)

keyboard.coord_mapping = [0, 1, 2, 3, 4, 5]

keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
    ]
]

encoder = EncoderHandler()
encoder.pins = (
    (board.GP26, board.GP27, board.GP0),
)
encoder.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),
]
keyboard.modules.append(encoder)

displayio.release_displays()

i2c = busio.I2C(board.GP7, board.GP6)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_ssd1306.SSD1306(
    display_bus,
    width=128,
    height=32,
)

group = displayio.Group()
display.show(group)

text = label.Label(
    terminalio.FONT,
    text="hello world!",
    color=0xFFFFFF,
    x=0,
    y=16,
)

group.append(text)

while True:
    keyboard.go()
