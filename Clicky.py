import pyautogui
import keyboard
import tkinter as tk


class GUI:
    ##
    # __init__()
    # Initializes and opens the window.
    #
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Autoclicker")
        self.window.geometry("700x500")

        lbl = tk.Label(self.window, text="Click to Start. Press 1 to start, and ` to stop")
        lbl.grid(column=1, row=1)

        self.lbl2 = tk.Label(self.window)
        self.lbl2.grid(column=2, row=2)

        btn = tk.Button(self.window, text="Start", command= self.clickedRED)
        btn.grid(column=1, row=2)


    def clickedRED(self):
        while True:
            if keyboard.is_pressed('='):
                break
            x = False
            if keyboard.is_pressed('1'):
                x = not x
            while x:
                click()
                if keyboard.is_pressed('`'):
                   x = not x
                   break

    ##
    #run()
    #runs GUI
    #
    def run(self):
        self.window.mainloop()
def click():
    pyautogui.mouseDown()
    pyautogui.mouseUp()



if __name__ == '__main__':
    app = GUI()
    app.run()

