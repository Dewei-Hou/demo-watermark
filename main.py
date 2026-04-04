import cv2
import numpy as np

"""
def RGB_to_GRAY(img, gray_img):
    for i in range(img_row):
        for j in range(img_col):
            for k in range(len(img[i][j])):
                gray_img[i][j] += img[i][j][k]
            gray_img[i][j] /= len(img[i][j])
    return gray_img
"""


def watermark(gray_main_img, gray_hidden_img):
    for i in range(img_col):
        for j in range(img_row):
            gray_main_img[i][j] = gray_main_img[i][j] - \
                (gray_main_img[i][j] % least_sig)
            gray_main_img[i][j] = gray_main_img[i][j] + \
                (gray_hidden_img[i][j]//first_sig)
    return gray_main_img


def main():
    # ------parameter-------
    global img_row
    global img_col
    global least_sig
    global first_sig
    # ---------------------
    main_img = cv2.imread("image/main_img.jpg")
    hidden_img = cv2.imread("image/hidden_img.jpg")
    img_row = 700
    img_col = 500
    main_img = cv2.resize(main_img, (img_row, img_col))
    hidden_img = cv2.resize(hidden_img, (img_row, img_col))
    least_sig = 4
    first_sig = 256/least_sig
    # ------change to gray-----
    #gray_main_img = np.zeros((img_row, img_col))
    #gray_main_img = RGB_to_GRAY(main_img, gray_main_img)
    #gray_hidden_img = np.zeros((img_row, img_col))
    #gray_hidden_img = RGB_to_GRAY(hidden_img, gray_hidden_img)
    gray_main_img = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    print("BEFORE:")
    print(gray_main_img[100][300])
    gray_hidden_img = cv2.cvtColor(hidden_img, cv2.COLOR_BGR2GRAY)
    print("HIDDEN:")
    print(gray_hidden_img[100][300])
    # -------------------------
    gray_main_img = watermark(gray_main_img, gray_hidden_img)

    print("AFTER:")
    print(gray_main_img[100][300])

    """
    cv2.imshow("Original Image", gray_main_img)
    cv2.waitKey(0)
    cv2.imshow("Hidden Image", gray_hidden_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """


if __name__ == "__main__":
    main()
