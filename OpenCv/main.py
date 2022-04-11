

import cv2

from controlling import controls
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

from calc import slope

keyboard = Controller()


cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    # hand1
    if hands:
        hand1 = hands[0]
        centerpoint1 = hand1["center"]
        type1 = hand1["type"]
        # print(centerpoint1 , type1)


    if len(hands)<=1:
        keyboard.release(Key.down)
        keyboard.release(Key.up)
        keyboard.release(Key.right)
        keyboard.release(Key.left)

    if len(hands) == 2:
        hand2 = hands[1]
        centerpoint2 = hand2["center"]
        type2 = hand1["type"]
        # print(centerpoint1, type2)
        length, info, img = detector.findDistance(centerpoint1, centerpoint2, img)
        # print(centerpoint1[0])
        slopeRes = slope(centerpoint1[0],centerpoint1[1],centerpoint2[0],centerpoint2[1])*1000

        controls(length ,slopeRes )


    cv2.imshow('segment', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break