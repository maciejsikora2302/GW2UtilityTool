import numpy as np
import cv2
import pyautogui as agui
import keyboard
from time import sleep
from guietta import Gui, _, Quit, ___, R1
import pygetwindow as gw


def take_screeshot(ss_name = None):
    if ss_name is None:
        ss_name = "AutoJoinerImg/ss.png"

    ss = agui.screenshot()
    img = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGR)
    cv2.imwrite(ss_name, img)
    return ss_name

def get_position_of_template(template_name, img_name = None, threshold = 0.9, save = False):
    if img_name is None:
        img_name = "AutoJoinerImg/ss.png"

    img_bgr = cv2.imread(img_name)
    img_grey = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    template = cv2.imread(template_name, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_grey, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    points = list(zip(*loc[::-1]))

    if save:
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

        cv2.imwrite("AutoJoinerImg/detected.png", img_bgr)
    try:
        return points[0]
    except IndexError:
        return None


def move_point_a_little_bit(point):
    return (point[0]+20, point[1]+10)

def move_mouse_to_center():
    center = agui.size()
    agui.moveTo(center[0]/2, center[1]/2)

def activate_gw2():
    windows = gw.getWindowsWithTitle("Guild Wars 2")
    for window in windows:
        if window.title == "Guild Wars 2":
            window.activate()

def move_and_click(button, template):
    name = take_screeshot()
    p = get_position_of_template(template, name)
    if p is not None:
        agui.moveTo(move_point_a_little_bit(p))
        sleep(0.01)
        agui.click(button=button)
        sleep(0.01)
        move_mouse_to_center()
        sleep(0.1)

def move_and_click_with_type(type):
    if type == "commander":
        move_and_click("right", "AutoJoinerImg/commander.png")
        move_and_click("left", "AutoJoinerImg/joinin.png")
        move_and_click("left", "AutoJoinerImg/okbutton.png")
    elif type == "party":
        move_and_click("right", "AutoJoinerImg/avatar.png")
        move_and_click("left", "AutoJoinerImg/joinin.png")
        move_and_click("left", "AutoJoinerImg/okbutton.png")



def run_joiner(gui):
    activate_gw2()
    sleep(0.1)

    while True:
        if keyboard.is_pressed("esc"):
            break
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