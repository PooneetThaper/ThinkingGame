import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')
import cv2
import os

i = 0
for file in os.listdir('images_raw'):
    print(file)

    # Load image
    image = cv2.imread(os.path.join('images_raw/',file))
    original = image

    print(image.shape[0],image.shape[1])
    r = 600.0 / image.shape[0]
    dim = (int(image.shape[1] * r),600)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    image = image[0:600,0:800]

    r = 300.0 / image.shape[0]
    dim = (int(image.shape[1] * r),300)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imshow("hi",image)
    cv2.waitKey(600)

    cv2.imwrite('images/{}'.format(str(i)+".jpg"),image)
    cv2.imwrite('images_raw/{}'.format(str(i)+".jpg"),image)

    i = i+1
