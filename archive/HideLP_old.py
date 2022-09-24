from pkgutil import ImpLoader
from jmespath import search
import win32gui
import pyautogui
import pytesseract
import time
import os
import tkinter

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def main():
    print("Working...")
    search_for = "C:/Users/2jonn/Dev/LoL noLP/images/honor.png"
    while True:
        im = pyautogui.locateOnScreen(search_for, confidence=0.8)
        print(im)
        if im:
            root = tkinter.Tk()
            root.title("LP?")
            root.wm_attributes("-topmost", 1)
            root.geometry("+380+450")
            root.geometry("180x100")
            root.configure(bg="#010E18")
            root.overrideredirect(True)
            root.mainloop()
        time.sleep(1)

def window():
    root = tkinter.Tk()
    root.title("LP?")
    root.wm_attributes("-topmost", 1)
    root.geometry("+380+450")
    root.geometry("180x100")
    root.configure(bg="#010E18")
    root.overrideredirect(True)
    root.mainloop()

if __name__ == "__main__":
    main()
