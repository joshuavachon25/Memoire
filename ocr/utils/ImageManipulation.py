import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


def enhance(folder, config):
    params = config["enhance"]
    if not os.path.exists(os.path.join(os.getcwd(), folder["src"], "enhance")):
        os.mkdir(os.path.join(os.getcwd(), folder["src"], "enhance"))
    for file in os.listdir(folder["src"]):
        print(f"▪️ Traitement de {file}")
        path = os.path.join(folder["src"], file)
        image = cv2.imread(path)
        gray_image = grayscale(image)
        thresh, bw_image = binarization(gray_image, params)
        clean_image = noise_reducer(bw_image, params)
        #align_image = deskew(clean_image, params)
        cv2.imshow("preview", clean_image)
        cv2.waitKey(0)
        return -1


def inverted(image):
    return cv2.bitwise_not(image)


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def binarization(image, params): #retourne 2 éléments
    return cv2.threshold(image, int(params["thresh_min"]), int(params["thresh_max"]), cv2.THRESH_BINARY)


def noise_reducer(image, params):
    kernel = np.ones((int(params["kw"]), int(params["kh"])), np.uint8)
    image = cv2.dilate(image, kernel, iterations=int(params["iterations"]))
    kernel = np.ones((int(params["kw"]), int(params["kh"])), np.uint8)
    image = cv2.erode(image, kernel, iterations=int(params["iterations"]))
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, int(params["blur"]))
    return image


def erode(image, params):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


def dilation(image, params):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return image


def get_skew_angle(image):
    new_image = image.copy()
    gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x, y, w, h = rect
        cv2.rectangle(new_image, (x, y), (x+w,y+h), (0, 255, 0), 2)

    largest_contour = contours[0]
    print(len(contours))
    min_area_rect = cv2.min_area_rect(largest_contour)
    cv2.imwrite("temp/boxes.jpg", new_image)
    
    angle = min_area_rect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle


def rotate_image(image, angle):
    new_image = image.copy()
    (h, w) = new_image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    new_image = cv2.warpAffine(new_image, rotation_matrix, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return new_image


def deskew(image, params):
    # https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df
    angle = get_skew_angle(image)
    return rotate_image(image, -1.0 * angle)


def add_borders(image, s):
    return cv2.copyMakeBorder(image, s, s, s, s, cv2.BORDER_CONSTANT, value=[255, 255, 255])


def remove_borders(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=lambda x: cv2.contourArea(x))
    cnt = sorted_contours[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y + h, x:x + w]
    return crop


def show(image):
    dpi = 80
    im_data = plt.imread(image)
    height, width = im_data.shape[:2]
    fsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=fsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.imshow(im_data, cmap='gray')
    plt.show()


def segment(folder, config):
    if not os.path.exists(os.path.join(os.getcwd(), folder["src"], "bound")):
        os.mkdir(os.path.join(os.getcwd(), folder["src"], "bound"))
    for file in os.listdir(folder["src"]):
        print(f"▪️ Traitement de {file}")
        path = os.path.join(folder["src"], file)
        image = cv2.imread(path)

        bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(bw, (7, 7), 0)
        thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
        dilate = cv2.dilate(thresh, kernel, iterations=1)

        contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

        for idx, box in enumerate(contours):
            x, y, w, h = cv2.boundingRect(box)
            if h > 150 and w > 25:
                zone = image[y:y+h, x:x+w]
                cv2.imwrite(folder["src"] + "/bound/" + file[0:4] + "_" + str(idx) + ".png", zone)
                print(f"▪️▪️  Ajout d'une zone")