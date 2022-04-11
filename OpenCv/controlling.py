
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key , Controller
import time
from calc import slope

keyboard = Controller()



def controls(length , slopeRes) :
    if length <200:
        keyboard.release(Key.up)
        keyboard.press(Key.down)
        print("DOWN")
        if (slopeRes > 150):
            keyboard.press(Key.left)
            print("left")
        elif slopeRes < -150:
            keyboard.press(Key.right)
            print("right")
        else:
            print("key released")
            keyboard.release(Key.right)
            keyboard.release(Key.left)



    elif(length > 400):
        keyboard.release(Key.down)
        keyboard.press(Key.up)
        # time.sleep(.09)
        # keyboard.release("b")q

        print("UP")
        if (slopeRes > 150):
            keyboard.press(Key.left)
            print("left")
        elif slopeRes < -150:
            keyboard.press(Key.right)
            print("right")
        else:
            print("key released")
            keyboard.release(Key.right)
            keyboard.release(Key.left)


    else:
        keyboard.release(Key.up )
        keyboard.release(Key.down)
        if (slopeRes > 150):
            keyboard.press(Key.left)
            print("left")
        elif slopeRes < -150:
            keyboard.press(Key.right)
            print("right")
        else:
            print("key released")
            keyboard.release(Key.right)
            keyboard.release(Key.left)


