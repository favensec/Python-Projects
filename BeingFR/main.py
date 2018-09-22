

import os
import face_recognition
from PIL import Image

image = face_recognition.load_image_file("test.jpg")
face_locations = face_recognition.face_locations(image)

def path_exists(path):
    dir = os.path.dirname(path)
    
    if not os.path.exists(dir):
        os.makedirs(dir)


print ("I found {} face(s) in this photograph.".format(len(face_locations)))

i = 0

for face_location in face_locations:
    
    top, right, bottom, left = face_location
    print("A face located at pixel Location: {}, Left: {}, Bottom: {}. Right: {}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("face-{}.jpg".format(i))
    i = i + 1
