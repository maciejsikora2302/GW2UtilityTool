import keyboard as k
import time
import numpy as np
import base64
import pygetwindow as gw
from guietta import Gui

main_key = None
chat_code = "I'm a stupid potato and forgot to pick which kp I want to ping."

dhuum_chat_code = "[&AoqBTgEA]"
quadim_v1_chat_code = "[&ApNFWgEA]"
quadim_v2_chat_code = "[&Al8nZAEA]"
unstable_cosmic_essence_chat_code = "[&AvpPPwEA]"
legendary_insight_chat_code = "[&Ag32LQEA]"


def rand_time(lower, upper):
    return (upper - lower) * np.random.random() + lower


def convert_chat_code_with_amount(cc, amount):
    print(cc[2:-1])
    hex_val = base64.b64decode(cc[2:-1]).hex()
    hex_val = str(hex_val)
    print(hex_val)
    ret = hex_val[:2]
    ret += str(hex(amount))[2:]
    ret += hex_val[4:]
    print(ret)
    print(bytearray.fromhex(ret))
    to_ret = base64.b64encode(bytearray.fromhex(ret))
    print(str(to_ret)[2:-1])
    print("[&" + str(to_ret)[2:-1] + "]")
    return "[&" + str(to_ret)[2:-1] + "]"


def activate_gw2():
    windows = gw.getWindowsWithTitle("Guild Wars 2")
    for window in windows:
        if window.title == "Guild Wars 2":
            window.activate()


def send_kp(gui):
    global chat_code

    activate_gw2()
    time.sleep(0.5)

    try:
        # print(int(gui.Amount))
        # if int(gui.Amount) < 1 or int(gui.Amount) > 250:
        #     raise ValueError
        chat_code = convert_chat_code_with_amount(chat_code, int(gui.Amount))
        print(chat_code)
    except ValueError:
        gui2 = Gui(["Wrong input in KP amount, try again"])
        gui2.run()
        return

    ping_times = 0

    try:
        ping_times = int(gui.Ping)
    except ValueError:
        gui2 = Gui(["Wrong input in ping times, try again"])
        gui2.run()
        return

    for _ in range(ping_times):
        k.send("enter")
        time.sleep(0.018)
        k.write(chat_code)
        time.sleep(0.018)
        k.send("enter")
        time.sleep(rand_time(0.1, 0.11))
