import time
import numpy as np
from pywinauto import Application
from PIL import ImageGrab
import cv2


# may be decorator for some function... but it doesn't work correctly
def loop_time(sfunc):
    last_time = time.time()
    while True:
        sfunc()
        print(time.time() - last_time)
        last_time = time.time()


# simple test for getting printscreen of windowed app (but with borders)
def eye_test_1():
    app = Application().connect(title_re=".*Блокнот")
    hwin = app.top_window()
    hwin.set_focus()
    img = hwin.capture_as_image()
    # print(img)
    img.save('notepad_screenshot.png')


# stay frosty
def win_func():
    print("BINGO, BANGO, BONGO! BISH, BASH, BOSH!")


# some action if image screen box are equal to sample image
def action_on_screen_event(my_func, *args):
    lt = time.time()
    base_img = np.load("eyetest_sample.npy")
    while True:
        prtsc_pil = ImageGrab.grab(bbox=(15, 37, 150, 55))       #135x18
        prtsc_np = np.array(prtsc_pil)
        # cv2.imshow("eyetest2_IMG", prtsc_np)
        if np.allclose(base_img, prtsc_np, 1, 0):
            my_func(*args)
            break
        print(time.time() - lt)
        lt = time.time()
        # cv2.waitKey(10)


# Collect new samples for comparing
def save_new_anchor_pic():
    print("Collecting new samples...")
    i = 0
    while i < 10:
        prtsc_pil = ImageGrab.grab(bbox=(15, 37, 150, 55))
        prtsc_pil.save('new_samples\\eyetest2_{}.png'.format(i))
        prtsc_np = np.array(prtsc_pil)
        np.save('new_samples\\eyetest2_{}.npy'.format(i), prtsc_np)
        print(i)
        i += 1
        time.sleep(1)
    print("Done.")


# just testing PIL for grab image from screen using coords
def pil_image_grab():
    prtsc_pil = ImageGrab.grab(bbox=(0, 0, 800, 600))
    prtsc_np = np.array(prtsc_pil)
    cv2.imshow("pil_image_grab", prtsc_np)
    cv2.waitKey(0)


# just testing PIL for show image
def test_cv2():
    image = cv2.imread("eyetest2.png")
    cv2.imshow("Original image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    save_new_anchor_pic()
