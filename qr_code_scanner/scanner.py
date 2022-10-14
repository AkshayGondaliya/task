import glob
import cv2
#import pandas as pd
#import pathlib
import argparse


def read_qr_code(filename):

    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        print(value)
        print(points)
        print(straight_qrcode)
        
        return value
    except Exception as e:
        print(e)

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()

    ap.add_argument("-I", "--image", required=True,help="name of the image")

    args = vars(ap.parse_args())

    print("your image name is : {}".format(args["image"]))

    value = read_qr_code(args["image"])
    
    print("image {} is contain {} .".format(args["image"],value))

if __name__ == "__main__":
    main()
