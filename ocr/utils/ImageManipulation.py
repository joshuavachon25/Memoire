import cv2
import os


def segmentation(folder):
    os.mkdir(os.path.join(os.getcwd(), "output", "images", "segmenter", folder))
    for file in os.listdir("input/" + folder):
        print(f"▪️ Traitement de {file}")
        path = os.path.join("input", folder, file)
        image = cv2.imread(path)

        bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(bw, (7, 7), 0)
        thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
        dilate = cv2.dilate(thresh, kernel, iterations=1)
        cv2.imwrite("output/images/segmenter/" + folder + "/" + file[0:4] + "_blurred.png", blurred)
        cv2.imwrite("output/images/segmenter/" + folder + "/" + file[0:4] + "_dilate.png", dilate)

        contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

        for idx, box in enumerate(contours):
            x, y, w, h = cv2.boundingRect(box)
            if h > 150 and w > 25:
                zone = image[y:y+h, x:x+w]
                cv2.imwrite("output/images/segmenter/" + folder + "/" + file[0:4] + "_" + str(idx) + ".png", zone)
                print(f"▪️▪️  Ajout d'une zone")