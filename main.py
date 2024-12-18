import cv2

ASCII_CHAR = "@#S%?*+;:,. "
# ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


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
            char_index = (len(ASCII_CHAR) - 1) - round(
                (brightness / 255) * (len(ASCII_CHAR) - 1)
            )
            ascii_img += ASCII_CHAR[char_index]
            ascii_img.append(ASCII_CHAR[char_index])
        ascii_img.append("\n")

    ascii_img = "".join(ascii_img)

    return ascii_img


if __name__ == "__main__":
    img_path = "/mnt/c/Users/pongp/OneDrive/Pictures/Screenshots/Screenshot_20221026_012358.png"

    img = cv2.imread(img_path)
    resized_img = resize_img(img)
    ascii_img = image_to_ascii(resized_img)

    print(ascii_img)
    print(len(ascii_img))

    # print(new_width)
    # print(new_height)
    # cv2.imwrite("./output/test.png", gray_img)
