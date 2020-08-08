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



def RunCloverMaker(mainGui):
    gui = Gui(
        ["CloverMaker!", ___, ___],
        ["Prepare your mystic forge window and make sure you have enough items for clovers in eq", ___, ___],
        ["How many times do you want to try to create Mystic Clover?", "__Input__", _],
        [["Start"], ___, ___]
    )

    gui.Start = make_cloves

    gui.run()

