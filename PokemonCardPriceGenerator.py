# import required libraries
import cv2
import numpy as np

drawing = False
ix,iy = -1,-1

# define mouse callback function to draw circle
def draw_rectangle(event, x, y, flags, param):
   global ix, iy, drawing, img
   if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix = x
      iy = y
   elif event == cv2.EVENT_LBUTTONUP:
      drawing = False
      cv2.rectangle(img, (ix, iy),(x, y),-1)
   copy_image = img

# Create a black image
img = cv2.imread('pikachu1.jpg')
copy_img = img.copy()

# Create a window and bind the function to window
cv2.namedWindow("Pokemon Window")

# Connect the mouse button to our callback function
cv2.setMouseCallback("Pokemon Window", draw_rectangle)

# display the window
while True:
   cv2.imshow("Pokemon Window", img)
   key = cv2.waitKey(1) & 0xFF
   if key == 27:
      break

   elif key == ord('d'):  # Press 'd' to delete the last drawn rectangle
      img = copy_img
cv2.destroyAllWindows()