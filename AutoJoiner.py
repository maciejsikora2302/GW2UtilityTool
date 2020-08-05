import keyboard
from time import sleep
from guietta import Gui, _, Quit, ___, R1
from OverallUtilities import activate_gw2, move_and_click, is_key_pressed


def move_and_click_with_type(type):
    if type == "commander":
        if is_key_pressed("esc"): return
        move_and_click("right", "AutoJoinerImg/commander.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "AutoJoinerImg/joinin.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "AutoJoinerImg/okbutton.png")
        if is_key_pressed("esc"): return
    elif type == "party":
        if is_key_pressed("esc"): return
        move_and_click("right", "AutoJoinerImg/avatar.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "AutoJoinerImg/joinin.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "AutoJoinerImg/okbutton.png")
        if is_key_pressed("esc"): return

def run_joiner(gui):
    activate_gw2()

    while True:
        if keyboard.is_pressed("esc"): break

        if gui.Commander.isChecked() or (not gui.Commander.isChecked() and not gui.Commander.isChecked()):
            move_and_click_with_type("commander")
        elif gui.Party.isChecked():
            move_and_click_with_type("party")


def RunAutoJoiner(mainGui):
    gui = Gui(
        ["AutoJoiner, Created By Magomir", ___, ___],
        ["Select if you are in squad with Commander or just in normal party, then just press \"Start\" button.", ___, ___],
        ["To stop the execution of this script just hold ESC button for a moment", ___ , ___],
        ["Join type:", R1("Commander"), R1("Party")],
        [["Start"], ___, ___],
        [Quit, ___, ___]
              )

    gui.Start = run_joiner


    gui.run()