import pyautogui
import time
from testcv2 import getCoord
# Создание скриншота и сохранение в текущей директории
screenshot = pyautogui.screenshot()
screenshot.save("screenshot_1.png")
# Заданные координаты для нажатия
x_coordinate = 300
y_coordinate = 280
def to_int(x):
    return int(x)
# Задержка перед началом действия (например, 2 секунды)
time.sleep(2)
getCoord()


promegt =""
with open("writeCorrdinate.txt","r") as re:
    promegt  = re.read().split(",")
    # IntList = list(map(to_int, promegt))
    # X1,Y1 = IntList
X1 = 0
Y1 = 0
for it in promegt:
    if len(it) == 0:
        continue
    X1,Y1 = it.split("-")
    print(X1,Y1)
    X1 = int(X1)+5
    Y1 = int(Y1)-3
    # Нажатие на кнопку мыши по заданным координатам
    pyautogui.click(X1, Y1)

    # Дополнительно: можно добавить задержку после нажатия
    time.sleep(1)

# X1 = int(X1)+5
# Y1 = int(Y1)-3
# # Нажатие на кнопку мыши по заданным координатам
# pyautogui.click(X1, Y1)
#
# # Дополнительно: можно добавить задержку после нажатия
# time.sleep(1)
