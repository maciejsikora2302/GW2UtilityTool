import cv2
import pyautogui as agui
import numpy as np
import pygetwindow as gw
import keyboard as kb
from time import sleep


def activate_gw2():
    windows = gw.getWindowsWithTitle("Guild Wars 2")
    for window in windows:
        if window.title == "Guild Wars 2":
            window.activate()
            sleep(0.1)

def is_key_pressed(key):
    return kb.is_pressed(key)


def move_point_a_little_bit(point):
    return (point[0]+20, point[1]+10)


def take_screeshot(ss_name = None):
    if ss_name is None:
        ss_name = "TmpArea/ss.png"

    ss = agui.screenshot()
    img = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGR)
    cv2.imwrite(ss_name, img)
    return ss_name


def get_position_of_template(template_name, img_name = None, threshold = 0.9, save = False):
    if img_name is None:
        img_name = "TmpArea/ss.png"

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

        cv2.imwrite("TmpArea/detected.png", img_bgr)
    try:
        return points[0]
    except IndexError:
        return None

def move_mouse_to_center():
    center = agui.size()
    agui.moveTo(center[0]/2, center[1]/2)

def move_and_click(button, template_to_find, clicks = 1, wait_time = 0.1):
    name = take_screeshot()
    p = get_position_of_template(template_to_find, name)
    if p is not None:
        agui.moveTo(move_point_a_little_bit(p))
        # sleep(0.01)
        agui.click(button=button, clicks= clicks)
        # sleep(0.01)
        move_mouse_to_center()
        sleep(wait_time)
