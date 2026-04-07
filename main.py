import cv2
import numpy as np

img_row = 700
img_col = 500
least_sig = 4
first_sig = 256 / least_sig

# func 1 watermark
def watermark(gray_main_img, gray_hidden_img):
    for i in range(img_col):
        for j in range(img_row):
            gray_main_img[i][j] = gray_main_img[i][j] - \
                (gray_main_img[i][j] % least_sig)
            gray_main_img[i][j] = gray_main_img[i][j] + \
                (gray_hidden_img[i][j] // first_sig)
    return gray_main_img


# func 2 remove background
def removeBackground(img):

    pass

def edgeDetection(img):

    pass


def run_watermark():
    main_img = cv2.imread("image/main_img.jpg")
    hidden_img = cv2.imread("image/hidden_img.jpg")

    main_img = cv2.resize(main_img, (img_row, img_col))
    hidden_img = cv2.resize(hidden_img, (img_row, img_col))

    gray_main_img = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    gray_hidden_img = cv2.cvtColor(hidden_img, cv2.COLOR_BGR2GRAY)

    print("BEFORE:", gray_main_img[100][300])
    print("HIDDEN:", gray_hidden_img[100][300])

    result = watermark(gray_main_img, gray_hidden_img)

    print("AFTER:", result[100][300])
    return result


def run_removeBackground():
    main_img = cv2.imread("image/main_img.jpg")
    main_img = cv2.resize(main_img, (img_row, img_col))
    result = removeBackground(main_img)
    return result

def run_edgeDetection():
    main_img = cv2.imread("image/main_img.jpg")
    main_img = cv2.resize(main_img, (img_row, img_col))
    result = edgeDetection(main_img)
    return result

def main(mode):
    if mode == 1:
        print("===func 1 watermark===")
        run_watermark()
    elif mode == 2:
        print("===func 2 remove background===")
        run_removeBackground()
    elif mode == 3:
        print("===func 3 edge detection===")
        run_edgeDetection()


if __name__ == "__main__":
    main(mode=1)