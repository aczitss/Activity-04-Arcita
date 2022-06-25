import cv2 
filepath = 'john.jpg'
imgFlag = int(1)
img = cv2.imread(filepath,imgFlag)
cv2.imshow("ME", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

