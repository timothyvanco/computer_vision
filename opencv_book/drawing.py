import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)  # last number - thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1) # filled with color
cv2.imshow("Canvas", canvas)
canvas1 = canvas
cv2.waitKey(0)



canvas2 = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas2.shape[1] // 2, canvas2.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    # draw a circle in the center - based on coordinates with radius starting 0 end in 150, step 25
    cv2.circle(canvas2, (centerX, centerY), r, white)

cv2.imshow("Canvas2", canvas2)
cv2.waitKey(0)


# draw 25 random circles, random size 5 - 200, random color - size 3, center coordinates for circle 0 - 300 with size 2
canvas3 = np.zeros((300, 300, 3), dtype="uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high = 200)                       # 1 random radius
    color = np.random.randint(0, high = 256, size = (3,)).tolist()  # 3 random colors
    pt = np.random.randint(0, high = 300, size = (2,))              # 2 points - middle of circles
    cv2.circle(canvas3, tuple(pt), radius, color, -1)                # thickness = -1

cv2.imshow("Canvas3", canvas3)
cv2.waitKey(0)

stack = np.hstack((canvas1, canvas2, canvas3))
cv2.imwrite("drawing.jpg", stack)




