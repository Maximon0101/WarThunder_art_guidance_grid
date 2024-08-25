import cv2

from features import points_to_sections_reduced

# Place your photo into project's directory and replace 'example.jpg' to your photo's name
my_photo = cv2.imread('example.jpg')
img_grey = cv2.cvtColor(my_photo, cv2.COLOR_BGR2GRAY)

# set a thresh
thresh = 180
# get threshold image
ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
# find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contours[number of counter][number of point in counter][filler zero][0 - x, 1 - y]


# transformation of list of points to list of sections
sections = points_to_sections_reduced(contours, 4000)


# print into file
with open("example.txt", encoding='utf8') as f:
    file = f.read()

file += "\n"
for section in sections:
    file += "line{\n"
    file += f"line: p4 = {section[0]}, {section[1]}, {section[2]}, {section[3]}\n"
    file += "move: b = no\n"
    file += "thousandth: b = yes\n"
    file += "}\n"
file += "}"

with open("test.txt", 'w', encoding='utf8') as f:
    f.write(file)
