import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

print("Camera opened:", cap.isOpened())

human_w, human_h = 358, 365
x, y = 793, 309   # from UI design (CORRECT)

while True:
    imgBG = cv2.imread("assets/bg2.jpg")
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)

    imgScaled = cv2.resize(img, (human_w, human_h))
    imgScaled = imgScaled[:, 50:human_w]   # crop left 50px

    # ✅ FIX: DO NOT offset x again
    imgBG[y:y+human_h, x:x+imgScaled.shape[1]] = imgScaled

    cv2.imshow("Image", img)
    cv2.imshow("BG", imgBG)
    cv2.imshow("Scaled", imgScaled)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
