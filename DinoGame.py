from PIL import ImageGrab
import time
import pyautogui

def collision(data):
    for i in range(340, 410):
        for j in range(570, 660):
            if data[i, j] < 100:
                pyautogui.keyDown('up')
                return
    return

if __name__ == "__main__":
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        collision(data)

