# import required libraries
import cv2
import numpy as np
import pytesseract

drawing = False
ix, iy = -1, -1
start_point = None
end_point = None
rectangles = []
squares = []
texts = []


# define mouse callback function to draw circle
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, start_point, end_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
        start_point = (x, y)
        print(f"Cordinates of selected square in down: ({x}, {y})")
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Append recrangle coordinates to the stack
        rectangles.append((ix, iy, x, y))
        cv2.rectangle(img, (ix, iy), (x, y), -1)
        end_point = (x, y)
        print(f"Cordinates of selected square in up: ({x}, {y})")

        width = abs(end_point[0] - start_point[0])
        height = abs(end_point[1] - start_point[1])

        square_info = {
            "x": start_point[0],
            "y": start_point[1],
            "width": width,
            "height": height,
        }

        squares.append(square_info)
        print(f"Width: {width}, Height: {height}")

    copy_image = img


# Redraw rectangles in every frame TODO Will be added rectangle count limitation or changing the this method otherwise with much retangle program will be crash or slower
def redraw_rectangle(img, rectangles):
    temp_image = img.copy()
    for rect in rectangles:
        cv2.rectangle(temp_image, (rect[0], rect[1]), (rect[2], rect[3]), -1)
    return temp_image


# Create a imaged
img = cv2.imread("pikachu1.jpg")

# Create a window and bind the function to windowd
cv2.namedWindow("Pokemon Window")

# Connect the mouse button to our callback function
cv2.setMouseCallback("Pokemon Window", draw_rectangle)

# display the window
while True:
    if rectangles:
        temp_image = redraw_rectangle(img=img, rectangles=rectangles)
        cv2.imshow("Pokemon Window", temp_image)
    else:
        cv2.imshow("Pokemon Window", img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Close the window with pressing 'esc'
        break
    elif key == ord("d"):  # Press 'd' to delete the last drawn rectangle
        if rectangles:
            rectangles.pop()

cv2.destroyAllWindows()

for i, square in enumerate(squares):
    print(f"Square {i + 1}: {square}")


for square in squares:
    x, y, width, height = square["x"], square["y"], square["width"], square["height"]

    # cropped image
    square_img = img[y : y + height, x : x + width]
    cv2.imshow("Square Window", square_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    pytesseract.pytesseract.tesseract_cmd = (
        "C:\\Users\\nadid\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
    )
    text = pytesseract.image_to_string(square_img)

    texts.append(text)

for i, text in enumerate(texts):
    print(f"Square {i + 1} Text: {text}")
