
import os
import platform
from infi.systray import SysTrayIcon

def switch2ten(systray):
    os.system('bcdedit /default {1e80bffe-1028-11ec-80bd-9358656ede0d}')
    os.system("shutdown /r /t 0")

def switch2eleven(systray):
    os.system('bcdedit /default {013de086-263f-11ec-a5c2-d872ac418499}')
    os.system("shutdown /r /t 0")


if __name__ == '__main__':

    menu_options = (("to10", None, switch2ten),) if platform.win32_ver()[1] == '10.0.22000' else (("to11", None, switch2eleven),)

    systray = SysTrayIcon("icon2.ico", "OS Switcher", menu_options)
    systray.start()