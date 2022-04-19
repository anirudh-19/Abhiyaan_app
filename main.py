# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import numpy as np

def nothing(): #dummy function
    pass


cap = cv2.VideoCapture("/Users/anirudh/Downloads/bolt_test_pothole.mp4") #loading the video onto the dev

cv2.namedWindow("Frame")
cv2.createTrackbar("L-H", "Frame", 0, 180, nothing) #customisation options setup
cv2.createTrackbar("L-S", "Frame", 0, 255, nothing)
cv2.createTrackbar("L-V", "Frame", 0, 255, nothing)
cv2.createTrackbar("U-H", "Frame", 180, 180, nothing)
cv2.createTrackbar("U-S", "Frame", 255, 255, nothing)
cv2.createTrackbar("U-V", "Frame", 255, 255, nothing)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos("L-H","Frame") #customisation options
    ls = cv2.getTrackbarPos("L-S", "Frame")
    lv = cv2.getTrackbarPos("L-V", "Frame")
    uh = cv2.getTrackbarPos("U-H", "Frame")
    us = cv2.getTrackbarPos("U-S", "Frame")
    uv = cv2.getTrackbarPos("U-V", "Frame")





    lower_gray = np.array([lh,14,ls])
    upper_gray = np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_gray,upper_gray) #creating the mask
    kernel=np.ones((4,4), np.uint8)
    mask=cv2.erode(mask, kernel)  #noise removal using erode function

    #contours detection

    contours, hirearchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area=cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt,0.009*cv2.arcLength(cnt,True), True)
        x=approx.ravel()[0]
        y=approx.ravel()[1]

        if area>700 and area<10000: #creating the threshold for which we can call it a circle (a pothole in this case)
            cv2.drawContours(frame, [approx], 0, (0,0,0), 3)
            if 14<len(approx)<20:
                print("POTHOLE")
                cv2.putText(frame, "POTHOLE", (x,y), cv2.FONT_ITALIC, 1, (0,0,128))

    cv2.imshow("Frame" , frame)
    cv2.imshow("Mask",mask)

    key = cv2.waitKey(1)

    if key == 27: #27 = esc key
        break

cap.release()
cv2.destroyAllWindows()


