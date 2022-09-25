import pyautogui

def main():
    while(True):
        try:
            for i in range(0, 100):
                x, y = pyautogui.position()
                pyautogui.moveTo(x+4, y)
            for i in range(0, 100):
                x, y = pyautogui.position()
                pyautogui.moveTo(x-4, y)

        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    main()