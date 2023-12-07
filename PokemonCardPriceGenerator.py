# import required libraries
import cv2
import numpy as np
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Set TESSDATA_PREFIX environment variable, if not tesseract give an error
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files (x86)\Tesseract-OCR'

drawing = False
ix, iy = -1, -1
start_point = None
end_point = None
rectangles = []
squares = []
texts = []


# define mouse callback function to draw circle
def DrawRectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, start_point, end_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Append recrangle coordinates to the stack
        rectangles.append((ix, iy, x, y))

        end_point = (x, y)
        width = abs(end_point[0] - start_point[0])
        height = abs(end_point[1] - start_point[1])

        square_info = {
            "x": start_point[0],
            "y": start_point[1],
            "width": width,
            "height": height,
        }
        squares.append(square_info)



# Redraw rectangles in every frame TODO Will be added rectangle count limitation or changing the this method otherwise with much retangle program will be crash or slower
def RedrawRectangle(img, rectangles):
    temp_image = img.copy()
    for rect in rectangles:
        cv2.rectangle(temp_image, (rect[0], rect[1]), (rect[2], rect[3]), -1)
    return temp_image

def ScrappingFromWeb():
    pass


try:
    # Create a image size
    img = cv2.resize(cv2.imread("./Photos/weedle.jpg"), (720,900))
except Exception as e:
    print(f"Image cant loaded to app, Exception: {e}")

# Create a window and bind the function to windowd
cv2.namedWindow("Pokemon Window")

# Connect the mouse button to our callback function
cv2.setMouseCallback("Pokemon Window", DrawRectangle)

# If text extracted, have to pop extracted texts from the set
is_text_extracted = False

# display the window
while True:
    if rectangles:
        temp_image = RedrawRectangle(img=img, rectangles=rectangles)
        cv2.imshow("Pokemon Window", temp_image)
    else:
        cv2.imshow("Pokemon Window", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Close the window with pressing 'esc'
        break
    elif key == ord("d"):  # Press 'd' to delete the last drawn rectangle
        if rectangles:
            rectangles.pop()
        if squares:
            squares.pop()
        if is_text_extracted:
            texts.pop()

    elif key == ord("a"):
        for square in squares:
            x, y, width, height = square["x"], square["y"], square["width"], square["height"]

            # cropped image
            square_img = img[y : y + height, x : x + width]
            text = pytesseract.image_to_string(square_img)
            texts.append(text)
            is_text_extracted = True

        for i, text in enumerate(texts):
            print(f"Square {i + 1} Text: {text}")

cv2.destroyAllWindows()

