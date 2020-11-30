import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)
        blue = np.uint8([[[255, 0, 0]]])
        hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
        print(hsv_blue)
        l_blue = np.array([110, 100, 100])
        u_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, l_blue, u_blue)

        part1 = cv2.bitwise_and(back, back, mask=mask)

        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("cloak", part1+part2)
        if cv2.waitKey(5) == ord('q'):

            break

cap.release()
cv2.destroyAllWindows()
