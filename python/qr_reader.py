from pyzbar import pyzbar
import cv2

def read_qr(image):
    im_gray = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    im_bw = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)[1]
    barcodes = pyzbar.decode(im_bw)
    return barcodes[0].data.decode('utf-8')
