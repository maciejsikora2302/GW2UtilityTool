from guietta import Gui, _, ___, Quit, R1, R2
from GroupCreatorBossConfiguration import BossConfiguration
from OverallUtilities import activate_gw2, move_and_click, is_key_pressed
import keyboard as kb
from time import sleep


def RunGroupCreator(mainGui):
    gui = Gui(
        ["Group Creator", _, _],
        ["Pick group:", R1("Fractal"), R1("Strike")],
        ["Select what you have", _, _],
        ["Dps", "__dps__", ___],
        ["Condidps", "__condidps__", ___],
        ["Bs", "__bs__", ___],
        ["Tank", "__tank__", ___],
        ["Druid", "__druid__", ___],
        ["Hfb", "__hfb__", ___],
        ["Alacrane", "__alacrane__", ___],
        ["How much kp?", "__kp__", ___],
        [["Start"], ___, ___],
        [Quit, ___, ___]
    )
    gui.dps = 0
    gui.condidps = 0
    gui.bs = 0
    gui.tank = 0
    gui.druid = 0
    gui.hfb = 0
    gui.alacrane = 0
    gui.kp = 250

    gui.Start = create_party
    gui.run()


def create_party(gui):
    party = None

    if gui.Fractal.isChecked():
        party = BossConfiguration("CMs + T4")
        party.add_configuration(dps=2, bs=1, hfb=1, alacrane=1)
    elif gui.Strike.isChecked():
        party = BossConfiguration("All Strike")
        party.add_configuration(dps=6, bs=1, hfb=2, alacrane=1)

    try:
        party.subtract_roles(dps=int(gui.dps), condidps=int(gui.condidps), bs=int(gui.bs), tank=int(gui.tank), druid=int(gui.druid), hfb=int(gui.hfb),
                             alacrane=int(gui.alacrane))
    except:
        gui2 = Gui(["Something went wrong"])
        gui2.run()
        return
    party_string = party.create_list(gui.kp)

    activate_gw2()
    kb.send("Y")
    sleep(1)
    if is_key_pressed("esc"): return
    move_and_click("left", "GroupCreatorImg/lfg.png")

    if is_key_pressed("esc"): return
    if gui.Fractal.isChecked():
        move_and_click("left", "GroupCreatorImg/fractals.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "GroupCreatorImg/t4.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "GroupCreatorImg/adv_group.png")
        if is_key_pressed("esc"): return
        sleep(0.15)
        kb.write(party_string)
        if is_key_pressed("esc"): return
    elif gui.Strike.isChecked():
        move_and_click("left", "GroupCreatorImg/strike_main.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "GroupCreatorImg/strike_inner.png")
        if is_key_pressed("esc"): return
        move_and_click("left", "GroupCreatorImg/adv_group.png")
        if is_key_pressed("esc"): return
        sleep(0.15)
        kb.write(party_string)
        if is_key_pressed("esc"): return