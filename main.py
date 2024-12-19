import time

import cv2

ASCII_CHAR = " .,:;+*?%S#@"


def resize_img(img, new_height=100):
    width = img.shape[1]
    height = img.shape[0]
    new_width = int(width * (new_height / height))
    resized_img = cv2.resize(img, (new_width, new_height))

    return resized_img


def image_to_ascii(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    width = img.shape[1]
    height = img.shape[0]

    ascii_img = []
    for y in range(height):
        for x in range(width):
            brightness = gray_img[y, x]
            char_index = round((brightness / 255) * (len(ASCII_CHAR) - 1))
            ascii_img += ASCII_CHAR[char_index]
            ascii_img.append(ASCII_CHAR[char_index])
        ascii_img.append("\n")

    ascii_img = "".join(ascii_img)

    return ascii_img


if __name__ == "__main__":

    cap = cv2.VideoCapture("./data/pepe.mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 30

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        resized_frame = resize_img(frame)
        ascii_img = image_to_ascii(resized_frame)

        print("\033[H\033[J", end="")  # clear screen
        print(ascii_img)
        print(len(ascii_img))
        # cv2.imshow("camera", frame)

        time.sleep(1 / fps)

        if cv2.waitKey(0) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
