import win32gui
import win32process
import win32api
import win32con
import pyautogui
import pytesseract
import time
import os
import tkinter
import pywintypes

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



# def window():
#     root = tkinter.Tk()
#     root.title("LP?")
#     root.wm_attributes("-topmost", 1)
#     root.geometry("+380+450")
#     root.geometry("180x100")
#     root.configure(bg="#010E18")
#     root.overrideredirect(True)
#     root.mainloop()


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.lol_window_hwnd = []
        def callback(hwnd, _):
            text = win32gui.GetWindowText(hwnd)
            if "League of Legends" not in text:
                return
            rect = win32gui.GetWindowRect(hwnd)

            # 1024, 576
            # 1280, 720
            # 1600, 900

            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            
            if w in [1024, 1280, 1600]:
                print("Found Lol Window")
                self.lol_window_hwnd.append(hwnd)
            else:
                return
            
        win32gui.EnumWindows(callback, None)
        if len(self.lol_window_hwnd) == 0:
            print("Couldn't find lol window...")
            self.destroy()
        else:
            self.lol_window_hwnd = self.lol_window_hwnd[0]

        rect = win32gui.GetWindowRect(self.lol_window_hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        # print("\tLocation: (%d, %d)" % (x, y))
        # print("\t    Size: (%d, %d)" % (w, h))

        #220, 380
        self.target_x = x + w // 7.27
        self.target_y = y + h // 2.37
        self.loc_str = f"+{int(self.target_x)}+{int(self.target_y)}"

        self.target_w = w//9
        self.target_h = h//9
        self.target_str = f"{self.target_w}x{self.target_h}"

        self.title("LP?") # set title of window
        self.wm_attributes("-topmost", 1) # always on top
        self.geometry(self.loc_str) # location
        self.geometry(self.target_str) # size
        #self.configure(bg="#32cd32")
        self.configure(bg="#010E18")
        self.overrideredirect(True)

        self.button = tkinter.Button(self,  text = 'Close the window',
                                            command = self.close,
                                            background = "#010E18",
                                            foreground = '#FFFFFF',
                                            activebackground= '#212E28',)
        self.button.pack(pady = 10)
        self.update_loc()


    def close(self):
        print("a")
        self.destroy()

    def update_loc(self):
        rect = win32gui.GetWindowRect(self.lol_window_hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y

        #220, 380
        target_x = x + w // 7.27
        target_y = y + h // 2.37
        loc_str = f"+{int(target_x)}+{int(target_y)}"

        target_w = w//9
        target_h = h//9
        target_str = f"{target_w}x{target_h}"
        self.geometry(loc_str) # location
        self.geometry(target_str) # size
        self.after(10, self.update_loc)

def look_for(search_timer=1):
    search_for = ["images/honor-big.png",
                    "images/honor-regular.png",
                    "images/honor-small.png"]
    while True:
        im1 = pyautogui.locateOnScreen(search_for[0])#, confidence=0.8)
        im2 = pyautogui.locateOnScreen(search_for[1])#, confidence=0.8)
        im3 = pyautogui.locateOnScreen(search_for[2])#, confidence=0.8)
        if im1 or im2 or im3:
            return True
        time.sleep(search_timer)

def main_loop():
    while True:
        print(look_for(2))
        a = App()
        #a.after(10, a.update_loc)
        a.mainloop()

def main():
    main_loop()


if __name__ == "__main__":
    main()
