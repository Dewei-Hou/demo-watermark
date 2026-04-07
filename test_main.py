import cv2
import numpy as np
import main as m
from main import watermark


def test_watermark():
    main_img = np.zeros((500, 700), dtype=np.uint8)
    main_img[100][300] = 200

    hidden_img = np.zeros((500, 700), dtype=np.uint8)
    hidden_img[100][300] = 148

    original_value = main_img[100][300]
    result = watermark(main_img.copy(), hidden_img)

    assert result[100][300] != original_value, "watermark failed"
    print("watermark successed")


def test_removeBackground():
    test_img = np.ones((500, 700, 3), dtype=np.uint8) * 100
    result = m.removeBackground(test_img.copy())

    assert not np.array_equal(result, test_img), "removeBackground failed"
    print("removeBackground successed")


def test_edgeDetection():
    result = m.edgeDetection(np.zeros((500, 700, 3), dtype=np.uint8))
    assert result is None, "edgeDetection failed"
    print("test_edgeDetection successed")



if __name__ == "__main__":
    print("===test start===\n")

    print("---func 1---")
    test_watermark()

    print("---func 2---")
    test_removeBackground()

    print("---func 3---")
    test_edgeDetection()

    print("\n===all test successed===")