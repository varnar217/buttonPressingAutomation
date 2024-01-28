import cv2
import numpy as np
def getCoord():
    # Загрузите изображение и шаблон
    image = cv2.imread('screenshot_1.png')
    imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('db/douwlonad.png')
    templateGrey = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Произведите шаблонное сопоставление
    result = cv2.matchTemplate(imageGrey, templateGrey, cv2.TM_CCOEFF_NORMED)

    # Установите порог для определения совпадений
    threshold = 0.8
    locations = np.where(result >= threshold)

    # Извлеките координаты совпадений
    coordinates = list(zip(*locations[::-1]))

    # Отрисуйте прямоугольники вокруг найденных областей
    for coord in coordinates:
        bottom_right = (coord[0] + template.shape[1], coord[1] + template.shape[0])
        cv2.rectangle(image, coord, bottom_right, (0, 255, 0), 2)

    # Выведите изображение с отмеченными областями
    # cv2.imshow('Matches', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Верните координаты найденных областей
    print("Coordinates of matches:", coordinates)
    with open("writeCorrdinate.txt","w") as wr:
        for itCor in coordinates:
            wr.write(f"{itCor[0]}-{itCor[1]},")

# # Загрузите изображение и шаблон
# image = cv2.imread('screenshot_1.png')
# imageGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# template = cv2.imread('db/douwlonad.png')
# templateGrey = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#
# # Произведите шаблонное сопоставление
# result = cv2.matchTemplate(imageGrey, templateGrey, cv2.TM_CCOEFF_NORMED)
#
# # Установите порог для определения совпадений
# threshold = 0.8
# locations = np.where(result >= threshold)
#
# # Извлеките координаты совпадений
# coordinates = list(zip(*locations[::-1]))
#
# # Отрисуйте прямоугольники вокруг найденных областей
# for coord in coordinates:
#     bottom_right = (coord[0] + template.shape[1], coord[1] + template.shape[0])
#     cv2.rectangle(image, coord, bottom_right, (0, 255, 0), 2)
#
# # Выведите изображение с отмеченными областями
# # cv2.imshow('Matches', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Верните координаты найденных областей
# print("Coordinates of matches:", coordinates)
# with open("writeCorrdinate.txt","w") as wr:
#     for itCor in coordinates:
#         wr.write(f"{itCor[0]}-{itCor[1]},")
