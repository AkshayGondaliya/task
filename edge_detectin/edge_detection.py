# lib. import
import cv2

import argparse


def find_edge(image_name):

    # Reading an image
    try:

        image = cv2.imread(image_name)
        
        # Make a copy
        new_image = image.copy()
        
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert the grayscale image to binary
        ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)

        # To detect object contours, we want a black background and a white 
        # foreground, so we invert the image (i.e. 255 - pixel value)
        inverted_binary = ~binary

        # Find the contours on the inverted binary image, and store them in a list
        # Contours are drawn around white blobs.
        # hierarchy variable contains info on the relationship between the contours
        contours, hierarchy = cv2.findContours(inverted_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        # Draw the contours (in red) on the original image and display the result
        # Input color code is in BGR (blue, green, red) format
        # -1 means to draw all contours
        with_contours = cv2.drawContours(image, contours, -1,(0,255,0),3,)

        #Save Image
        cv2.imwrite("edge.png",with_contours)
    
    except Exception as e:
        print(e)


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-I", "--image", required=True,help="name of the user")
    args = vars(ap.parse_args())
    # display a friendly message to the user
    print("your image name is : {}".format(args["image"]))
    find_edge(args["image"])


if __name__ == "__main__":
    main()
