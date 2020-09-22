import keyboard as k
import numpy as np
import base64
from guietta import Gui
from OverallUtilities import activate_gw2
from time import sleep

main_key = None
chat_code = "I'm a stupid potato and forgot to pick which kp I want to ping."

dhuum_chat_code = "[&AoqBTgEA]"
quadim_v1_chat_code = "[&ApNFWgEA]"
quadim_v2_chat_code = "[&Al8nZAEA]"
unstable_cosmic_essence_chat_code = "[&AgFPPwEA]"
legendary_insight_chat_code = "[&Ag32LQEA]"


def rand_time(lower, upper):
    return (upper - lower) * np.random.random() + lower


def convert_chat_code_with_amount(cc, amount):
    # print(cc[2:-1])
    hex_val = base64.b64decode(cc[2:-1]).hex()
    hex_val = str(hex_val)
    # print(hex_val)
    ret = hex_val[:2]
    ret += str(hex(amount))[2:]
    ret += hex_val[4:]
    # print(ret)
    # print(bytearray.fromhex(ret))
    to_ret = base64.b64encode(bytearray.fromhex(ret))
    # print(str(to_ret)[2:-1])
    # print("[&" + str(to_ret)[2:-1] + "]")
    return "[&" + str(to_ret)[2:-1] + "]"


def send_procedure(chat_code):
    sleep_time = rand_time(0.018, 0.020)
    k.send("enter")
    sleep(sleep_time)
    k.write(chat_code)
    sleep(sleep_time)
    k.send("enter")
    sleep(rand_time(0.1, 0.126))


def get_amounts(int_amount):
    amounts = []
    if 1 <= int_amount <= 250:
        amounts.append(int_amount)
    elif 251 <= int_amount <= 499:
        amounts.append(250)
        amounts.append(int_amount - 250)
    elif 500 <= int_amount <= 747:
        amounts.append(250)
        amounts.append(249)
        amounts.append(int_amount - 499)
    elif 748 <= int_amount <= 994:
        amounts.append(250)
        amounts.append(249)
        amounts.append(248)
        amounts.append(int_amount - 747)
    return amounts


def get_correct_chat_code(gui):
    global chat_code

    try:
        int_amount = int(gui.Amount)
        amounts = get_amounts(int_amount)
    except ValueError:
        gui2 = Gui(["Wrong amount of KP. Should be between 1 and 944. Please try again."])
        gui2.run()
        return

    if gui.Dhuum.isChecked():
        chat_code = dhuum_chat_code
    elif gui.Quadimv1.isChecked():
        chat_code = quadim_v1_chat_code
    elif gui.Quadimv2.isChecked():
        chat_code = quadim_v2_chat_code
    elif gui.UnstableCosmicEssence.isChecked():
        chat_code = unstable_cosmic_essence_chat_code
    elif gui.LegendaryInsight.isChecked():
        chat_code = legendary_insight_chat_code
    elif gui.YourOwn.isChecked():
        chat_code = gui.Inserted
    else:
        gui2 = Gui(["You have forgotten to pick what kp do you want to ping"])
        gui2.run()
        return None

    correct_chat_codes = []
    for amount in amounts:
        correct_chat_codes.append(convert_chat_code_with_amount(chat_code, amount))

    return correct_chat_codes


def send_kp(gui):
    try:
        ping_times_lower = int(gui.PingLower)
        ping_times_upper = int(gui.PingUpper)
        correct_chat_codes = get_correct_chat_code(gui)

    except ValueError:
        gui2 = Gui(["Something went wrong with converting ping times field to integer, "
                    "please check it if it is an integer."])
        gui2.run()
        return

    if correct_chat_codes is None:
        return

    activate_gw2()



    for cc in correct_chat_codes:
        ping_times = np.random.randint(ping_times_lower, ping_times_upper + 1)
        for _ in range(ping_times):
            send_procedure(cc)
        sleep(rand_time(0.18, 0.26))
