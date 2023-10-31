# import required libraries
import cv2
import numpy as np

drawing = False
ix,iy = -1,-1
rectangles = []

# define mouse callback function to draw circle
def draw_rectangle(event, x, y, flags, param):
   global ix, iy, drawing, img
   if event == cv2.EVENT_LBUTTONDOWN:
      drawing = True
      ix = x
      iy = y
   elif event == cv2.EVENT_LBUTTONUP:
      drawing = False
      # Append recrangle coordinates to the stack
      rectangles.append((ix, iy,x, y))

# Redraw rectangles in every frame TODO Will be added rectangle count limitation or changing the this method otherwise with much retangle program will be crash or slower
def redraw_rectangle(img, rectangles):
   temp_image = img.copy()
   for rect in rectangles:
      cv2.rectangle(temp_image, (rect[0], rect[1]), (rect[2], rect[3]), -1)
   return temp_image

# Create a imaged
img = cv2.imread('pikachu1.jpg')

# Create a window and bind the function to windowd
cv2.namedWindow("Pokemon Window")

# Connect the mouse button to our callback function
cv2.setMouseCallback("Pokemon Window", draw_rectangle)

# display the window
while True:
   if(rectangles):
      temp_image = redraw_rectangle(img = img, rectangles = rectangles)
      cv2.imshow("Pokemon Window", temp_image)
   else:
      cv2.imshow("Pokemon Window", img)
   key = cv2.waitKey(1) & 0xFF
   if key == 27: # Close the window with pressing 'esc'
      break
   elif key == ord('d'):  # Press 'd' to delete the last drawn rectangle
      if(rectangles):
         rectangles.pop()

cv2.destroyAllWindows()