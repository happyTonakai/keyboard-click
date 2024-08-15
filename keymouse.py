#!/usr/bin/env python
# coding=UTF-8
"""
Author: Zerui Han <hanzr.nju@gmail.com>
Date: 2023-01-17 09:46:05
Description: Control mouse using keyboard
FilePath: /keyboard-click/keymouse.py
LastEditTime: 2024-08-15 13:03:45
"""
import os
import sys

import keyboard
import mouse
import pystray
from PIL import Image


class IconWorker:
    def __init__(self, hotkey, left, right, mid):
        self.images = [Image.open("switch-off.png"), Image.open("switch-on.png")]
        self.icon = pystray.Icon(
            "keymouse",
            self.images[1],
            "keymouse",
            pystray.Menu(
                # pystray.MenuItem("Reset", self.reset),
                pystray.MenuItem("Exit", self.exit),
            ),
        )
        self.click = Click(
            hotkey=hotkey,
            hotkey_left=left,
            hotkey_right=right,
            hotkey_mid=mid,
            worker=self,
        )
        self.icon.run()

    def exit(self):
        self.icon.stop()


def press_right():
    keyboard.press_and_release("right")


class Click:
    def __init__(
        self,
        hotkey: str,
        hotkey_left: str,
        hotkey_right: str,
        hotkey_mid: str,
        worker: IconWorker,
    ):
        self.status = False
        self.hotkey = hotkey
        self.hotkey_left = hotkey_left
        self.hotkey_right = hotkey_right
        self.hotkey_mid = hotkey_mid
        self.worker = worker
        self.toggle(None)

    def toggle(self, _):
        self.status = not self.status
        keyboard.unhook_all()
        keyboard.add_hotkey("alt+space", press_right, suppress=True)
        self.set_hotkey()
        if self.status:
            keyboard.on_press_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_release_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_press_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.on_release_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.on_press_key(self.hotkey_mid, self.mid_click, suppress=True)
            keyboard.on_release_key(self.hotkey_mid, self.mid_click, suppress=True)

        self.update_icon()

    def set_hotkey(self):
        suppress = "+" in self.hotkey
        keyboard.on_press_key(self.hotkey, self.toggle, suppress=suppress)

    def left_click(self, event: keyboard.KeyboardEvent):
        if event.event_type == "down":
            if not mouse.is_pressed("left"):
                mouse.press("left")
        else:
            mouse.release("left")

    def right_click(self, event: keyboard.KeyboardEvent):
        if event.event_type == "down":
            if not mouse.is_pressed("right"):
                mouse.press("right")
        else:
            mouse.release("right")

    def mid_click(self, event: keyboard.KeyboardEvent):
        if event.event_type == "down":
            if not mouse.is_pressed("middle"):
                mouse.press("middle")
        else:
            mouse.release("middle")

    def update_icon(self):
        self.worker.icon.icon = self.worker.images[self.status]


if __name__ == "__main__":
    # https://stackoverflow.com/questions/51060894/adding-a-data-file-in-pyinstaller-using-the-onefile-option
    try:
        os.chdir(sys._MEIPASS)
    except Exception:
        os.chdir(os.path.dirname(__file__))

    worker = IconWorker(hotkey="F4", left="F1", right="F2", mid="F3")
