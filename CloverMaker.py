from guietta import Gui, _, Quit, ___
from OverallUtilities import move_and_click, activate_gw2, is_key_pressed
from time import sleep


def make_cloves(gui):
    amount = 0

    try:
        amount = int(gui.Input)
    except ValueError:
        Gui(["Wrong input"]).run()
        return

    activate_gw2()


    for _ in range(amount):
        w_time = 0.05
        if is_key_pressed("esc"): break
        move_and_click("left", "CloverMakerImg/coin.png", clicks=2, wait_time=w_time)
        if is_key_pressed("esc"): break
        move_and_click("left", "CloverMakerImg/ecto.png", clicks=2, wait_time=w_time)
        if is_key_pressed("esc"): break
        move_and_click("left", "CloverMakerImg/shard.png", clicks=2, wait_time=w_time)
        if is_key_pressed("esc"): break
        move_and_click("left", "CloverMakerImg/stone.png", clicks=2, wait_time=w_time)
        if is_key_pressed("esc"): break
        move_and_click("left", "CloverMakerImg/forge.png", wait_time=w_time)
        if is_key_pressed("esc"): break
        sleep(1.3)


def make_cloves_using_refill_button(gui):
    amount = 0

    try:
        amount = int(gui.Input)
    except ValueError:
        Gui(["Wrong input"]).run()
        return

    activate_gw2()

    w_time = 0.05

    if is_key_pressed("esc"): return
    move_and_click("left", "CloverMakerImg/coin.png", clicks=2, wait_time=w_time)
    if is_key_pressed("esc"): return
    move_and_click("left", "CloverMakerImg/ecto.png", clicks=2, wait_time=w_time)
    if is_key_pressed("esc"): return
    move_and_click("left", "CloverMakerImg/shard.png", clicks=2, wait_time=w_time)
    if is_key_pressed("esc"): return
    move_and_click("left", "CloverMakerImg/stone.png", clicks=2, wait_time=w_time)
    if is_key_pressed("esc"): return
    move_and_click("left", "CloverMakerImg/forge.png", wait_time=w_time)
    if is_key_pressed("esc"): return
    sleep(2)


    for _ in range(amount-1):
        if is_key_pressed("esc"): return
        move_and_click("left", "CloverMakerImg/accept.png", clicks=1, wait_time=w_time)
        if is_key_pressed("esc"): return
        move_and_click("left", "CloverMakerImg/refill.png", clicks=1, wait_time=w_time)
        if is_key_pressed("esc"): return
        move_and_click("left", "CloverMakerImg/forge.png", clicks=1, wait_time=w_time)
        if is_key_pressed("esc"): return
        sleep(2)



def RunCloverMaker(mainGui):
    gui = Gui(
        ["CloverMaker!", ___, ___],
        ["Prepare your mystic forge window and make sure you have enough items for clovers in eq", ___, ___],
        ["How many times do you want to try to create Mystic Clover? 41 is max per 250 P. Stone", "__Input__", _],
        [["Start Refill"], ___, ___],
        [["Start Old"], ___, ___]
    )

    gui.StartRefill = make_cloves_using_refill_button
    gui.StartOld = make_cloves

    gui.run()

