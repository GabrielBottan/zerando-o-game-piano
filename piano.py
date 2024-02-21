import pyautogui as py
from time import sleep
import pyscreeze
import keyboard
import win32api
import win32con
 
py.click(1437,516, duration=1)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    

    
while keyboard.is_pressed('1') == False:


    if py.pixelMatchesColor(1296,516, (0,0,0)):
        click(1296,516)
        
    if py.pixelMatchesColor(1384,513,(0,0,0)):
        click(1384,513)
        
        
    if py.pixelMatchesColor(1474,512,(0,0,0)):
        click(1474,512)
        
    if py.pixelMatchesColor(1558,513,(0,0,0)):
        click(1558,513)
        