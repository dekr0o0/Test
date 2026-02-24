# 🟩 🌳 🌊 🔥 🚁 🪣 ❤️ ☁️ 🏥 🔧 ⬛ = 🏆

from Map import Map
import time
import os
from Helicopter import Helicopter as Helico


TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 10, 10

field = Map(MAP_W, MAP_H)
field.generate_forest(3, 10)
field.generate_river(10)
field.generate_river(20)

helico = Helico(MAP_W, MAP_H)

from pynput import keyboard

def on_press(key, injected):
    try:
        print('alphanumeric key {} pressed; it was {}'.format(
            key.char, 'faked' if injected else 'not faked'))
    except AttributeError:
        print('special key {} pressed'.format(
            key))

def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


tick = 1

while True:
    os.system('cls')
    print("TICK", tick)
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()