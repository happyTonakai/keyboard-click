#!/usr/bin/env python
# coding=UTF-8
'''
Author: Zerui Han <hanzr.nju@gmail.com>
Date: 2023-01-17 09:46:05
Description: Click mouse using keyboard
FilePath: /keyboard-click/keymouse.py
LastEditTime: 2023-01-19 14:17:57
'''

import keyboard
import mouse
import time


class Click:
    def __init__(self, hotkey='capslock+space', hotkey_left='d',
                 hotkey_right='f', hotkey_mid='g'):
        self.status = False
        self.hotkey_left = hotkey_left
        self.hotkey_right = hotkey_right
        self.hotkey_mid = hotkey_mid
        print('Hotkey: ', hotkey)
        print('Left: ', hotkey_left)
        print('Right: ', hotkey_right)
        print('Middle: ', hotkey_mid)

        while True:
            keyboard.wait(hotkey, suppress=True)  # only can suppress esc
            self.toggle()
            time.sleep(0.3)
            keyboard.press_and_release('capslock')  # reset capslock

    def toggle(self):
        self.status = not self.status
        print('Toggle status to %s' % self.status)
        if self.status:
            keyboard.on_press_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_release_key(self.hotkey_left, self.left_click, suppress=True)
            keyboard.on_press_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.on_release_key(self.hotkey_right, self.right_click, suppress=True)
            keyboard.add_hotkey(self.hotkey_mid, self.mid_click, suppress=True)
        else:
            keyboard.unhook_all()

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


if __name__ == '__main__':
    Click()
