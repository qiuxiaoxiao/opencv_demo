import cv2 as cv
import numpy as np

def inverse(image):
    print("read and write pixel by pixel")
    print(image.shape)
    print(image.size)
    print(image.dtype)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    #read once
    pixel_date = np.array(image, dtype=np.uint8)
    #loop pixel by pixel
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                level = pixel_date[row, col, c]
                pixel_date[row, col, c] = 255 - level

    #write once
    image[::] = pixel_date
    cv.imshow("inverse image", image)

def brightness(image):
    print("read and write pixel by pixel")
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(image.shape)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                level = image[row, col, c]
                pv = level + 30
                image[row, col, c] = (255 if pv > 255 else pv)
    cv.imshow("inverse image", image)

def to_gray(image):
    print("RGB to Gray Image")
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(image.shape)
    for row in range(height):
        for col in range(width):
            blue = image[row, col, 0]
            green = image[row, col, 1]
            red = image[row, col, 2]
            gray = (0.2989*red + 0.5870*green + 0.1140*blue)
            image[row, col, 0] = gray
            image[row, col, 1] = gray
            image[row, col, 2] = gray
    cv.imshow("gray image", image)

def gradient_image(image):
    gx = cv.Sobel(image, cv.CV_32F, 1, 0)
    gy = cv.Sobel(image, cv.CV_32F, 0, 1)
    dst = cv.addWeighted(gx, 0.5, gy, 0.5, 50)
    sobel_abs = np.absolute(dst)
    sobel_8u = np.uint8(sobel_abs)
    cv.imshow("gradient image", sobel_8u)

def clam(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    return pv

print("Image Pixel Operation Demo")
src = cv.imread("giraffe.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
gradient_image(src)
cv.waitKey(0)
cv.destroyAllWindows()
