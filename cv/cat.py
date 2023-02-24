import cv2

img = cv2.imread("assets/cat.jpg")
while True:
    cv2.imshow("Cat",img)
    if cv2.waitKey(1) & 0xFF == 27: # wait for at least 1ms and press esc key
        break