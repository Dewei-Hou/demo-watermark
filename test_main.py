import cv2
import numpy as np
import main as m
from main import watermark

def test_watermark():
    m.img_row = 700
    m.img_col = 500
    m.least_sig = 4
    m.first_sig = 256 / m.least_sig

    main_img = np.zeros((500, 700), dtype=np.uint8)
    main_img[100][300] = 200

    hidden_img = np.zeros((500, 700), dtype=np.uint8)
    hidden_img[100][300] = 148

    result = watermark(main_img.copy(), hidden_img)

    assert result[100][300] != main_img[100][300], "img not change"
    print("test passed！")

test_watermark()