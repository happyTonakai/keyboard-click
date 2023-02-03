#!/usr/bin/env python
# coding=UTF-8
'''
Author: Zerui Han <hanzr.nju@gmail.com>
Date: 2023-01-17 09:46:05
Description: Click mouse using keyboard
FilePath: /keyboard-click/keymouse.py
LastEditTime: 2023-02-03 15:27:43
'''

import os
import sys
import keyboard
import mouse
import time
import pystray
from PIL import Image


class Click:
    def __init__(self, hotkey, hotkey_left, hotkey_right, hotkey_mid):
        self.status = False
        self.hotkey = hotkey
        self.hotkey_left = hotkey_left
        self.hotkey_right = hotkey_right
        self.hotkey_mid = hotkey_mid
        self.images = [Image.open('switch-off.png'), Image.open('switch-on.png')]
        self.icon = pystray.Icon('keymouse', self.images[1], 'keymouse',
                                 pystray.Menu(pystray.MenuItem('Exit', self.exit)))
        keyboard.add_hotkey(self.hotkey, self.toggle, suppress=True)
        self.toggle()
        self.icon.run()

    def toggle(self):
        self.status = not self.status
        if self.status:
            keyboard.on_press_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_release_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_press_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.on_release_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.add_hotkey(self.hotkey_mid, self.mid_click, suppress=True)
        else:
            keyboard.unhook_all()
            keyboard.add_hotkey(self.hotkey, self.toggle, suppress=True)

        self.update_icon()
        if 'capslock' in self.hotkey:
            time.sleep(0.3)
            keyboard.press_and_release('capslock')  # reset capslock

    def left_click(self, event):
        if event.event_type == 'down':
            if not mouse.is_pressed('left'):
                mouse.press('left')
        else:
            mouse.release('left')

    def right_click(self, event):
        if event.event_type == 'down':
            if not mouse.is_pressed('right'):
                mouse.press('right')
        else:
            mouse.release('right')

    def mid_click(self):
        mouse.click('middle')

    def update_icon(self):
        self.icon.icon = self.images[self.status]

    def exit(self):
        self.icon.stop()


if __name__ == '__main__':
    os.chdir(sys._MEIPASS)  # https://stackoverflow.com/questions/51060894/adding-a-data-file-in-pyinstaller-using-the-onefile-option
    click = Click(hotkey='shift+space', hotkey_left='d',
                  hotkey_right='f', hotkey_mid='g')
