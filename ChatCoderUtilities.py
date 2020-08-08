import keyboard as k
import time
import numpy as np
import base64
from guietta import Gui
from OverallUtilities import activate_gw2

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


def send_procedure(chat_code):
    k.send("enter")
    time.sleep(0.018)
    k.write(chat_code)
    time.sleep(0.018)
    k.send("enter")
    time.sleep(rand_time(0.1, 0.11))


def send_kp(gui):
    global chat_code
    chat_code2 = ""

    try:
        #TODO Correct input amount of chatcode

        # print(int(gui.Amount))
        # if int(gui.Amount) < 1 or int(gui.Amount) > 250:
        #     raise ValueError
        chat_code = convert_chat_code_with_amount(chat_code, int(gui.Amount))
        if gui.Amount2 != "0" and gui.Ping2 != "0":
            chat_code2 = convert_chat_code_with_amount(chat_code, int(gui.Amount2))
        print(chat_code)
    except ValueError:
        gui2 = Gui(["Wrong input in KP amount, try again"])
        gui2.run()
        return

    ping_times = 0

    try:
        ping_times = int(gui.Ping)
        ping_times2 = int(gui.Ping)

    except ValueError:
        gui2 = Gui(["Wrong input in ping times, try again"])
        gui2.run()
        return

    activate_gw2()

    for _ in range(ping_times):
        send_procedure(chat_code)

    if gui.Amount2 != "0" and gui.Ping2 != "0":
        time.sleep(0.3)
        for _ in range(ping_times2):
            send_procedure(chat_code2)
