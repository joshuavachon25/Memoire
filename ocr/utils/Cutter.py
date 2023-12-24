from InquirerPy import prompt
import utils.Prompt as Q
from utils.Settings import get_config
import cv2
import numpy as np
from PIL import Image
import os


def menu():
    folder = prompt(Q.choose_folder)
    for filename in os.listdir(folder["src"]):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder["src"], filename)
            cropped_images = draw_polygon_and_crop(image_path)
            for idx, img in enumerate(cropped_images):
                if not os.path.exists(os.path.join(os.getcwd(), folder["src"], "cropped")):
                    os.mkdir(os.path.join(os.getcwd(), folder["src"], "cropped"))
                img.save(f"{folder['src']}/cropped/{filename.split('.')[0]}_{idx}.jpg")


def draw_polygon_and_crop(image_path):
    # Lire l'image et obtenir les dimensions de l'écran
    image = cv2.imread(image_path)
    screen_res = 1728, 972  # Exemple de résolution d'écran
    scale_width = screen_res[0] / image.shape[1]
    scale_height = screen_res[1] / image.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(image.shape[1] * scale)
    window_height = int(image.shape[0] * scale)

    resized_image = cv2.resize(image, (window_width, window_height))
    clone = resized_image.copy()

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", window_width, window_height)

    polygons = []
    current_polygon = []

    def draw_shape(event, x, y, flags, param):
        nonlocal current_polygon, polygons

        if event == cv2.EVENT_LBUTTONDOWN:
            current_polygon.append((x, y))

            # Dessiner les points et les lignes
            cv2.circle(resized_image, (x, y), 5, (0, 255, 0), -1)
            if len(current_polygon) > 1:
                cv2.line(resized_image, current_polygon[-2], current_polygon[-1], (255, 0, 0), 2)
            cv2.imshow("Image", resized_image)

    cv2.setMouseCallback("Image", draw_shape)

    while True:
        cv2.imshow("Image", resized_image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            resized_image = clone.copy()
            current_polygon = []
        elif key == ord("n"):  # Nouveau polygone
            if current_polygon:
                polygons.append(current_polygon)
                current_polygon = []
        elif key == ord("c"):  # Terminer la saisie
            if current_polygon:
                polygons.append(current_polygon)
            break

    cv2.destroyAllWindows()

    cropped_images = []
    for poly in polygons:
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        poly_scaled = [(int(x / scale), int(y / scale)) for x, y in poly]
        cv2.fillPoly(mask, np.array([poly_scaled], dtype=np.int32), (255))

        bbox = cv2.boundingRect(np.array([poly_scaled]))
        x, y, w, h = bbox
        cropped = image[y:y+h, x:x+w]

        cropped_images.append(Image.fromarray(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)))

    return cropped_images