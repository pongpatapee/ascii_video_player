import math

import cv2

ascii_char = "@#S%?*+;:,. "
# ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
img_path = (
    "/mnt/c/Users/pongp/OneDrive/Pictures/Screenshots/Screenshot_20221026_012358.png"
)


img = cv2.imread(img_path)

width = img.shape[1]
height = img.shape[0]
new_height = 100
new_width = int(width * (new_height / height))


img = cv2.resize(img, (new_width, new_height))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ascii_img = []
for y in range(new_height):
    for x in range(new_width):
        brightness = gray_img[y, x]
        # print(brightness)
        char_index = (len(ascii_char) - 1) - round(
            (brightness / 255) * (len(ascii_char) - 1)
        )
        # print(brightness, char_index)
        ascii_img += ascii_char[char_index]
        ascii_img.append(ascii_char[char_index])
    ascii_img.append("\n")


ascii_img = "".join(ascii_img)

print(ascii_img)
print(len(ascii_img))


print(new_width)
print(new_height)
cv2.imwrite("./output/test.png", gray_img)
