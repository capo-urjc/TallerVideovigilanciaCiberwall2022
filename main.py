import os
import cv2

class_names = ['pistol', 'smartphone', 'knife', 'monedero', 'billete', 'tarjeta']

base_path = '/media/archivos/TallerVideovigilanciaCiberwall2022/OD-WeaponDetection-master/Weapons and similar handled objects/Sohas_weapon-Detection-YOLOv5/obj_train_data'
img_path = os.listdir(base_path+'/images/test/')
labels_path = os.listdir(base_path+'/labels/test/')

img_path.sort()
labels_path.sort()

for (img, label) in zip(img_path, labels_path):
    im = cv2.imread(base_path+'/images/test/'+img)
    l = open(base_path+'/labels/test/'+label, "r")
    l = l.read()

    l = l.split(" ")

    clase = class_names[int(l[0])]

    font = cv2.FONT_HERSHEY_SIMPLEX
    x1 = float(l[1]) - float(l[3])/2.
    y1 = float(l[2]) - float(l[4])/2.
    x1 = int(float(x1) * im.shape[1])
    y1 = int(float(y1) * im.shape[0])

    x2 = float(l[1]) + float(l[3])/2.
    y2 = float(l[2]) + float(l[4])/2.
    x2 = int(float(x2) * im.shape[1])
    y2 = int(float(y2) * im.shape[0])

    org = (x1, y1)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    im = cv2.putText(im, clase, org, font,
                        fontScale, color, thickness, cv2.LINE_AA)

    cv2.rectangle(im, (x1, y1), (x2, y2), (255, 0, 0), 2)
    #
    # x1, y1 - -----
    # | |
    # | |
    # | |
    # --------x2, y2

    cv2.imshow('image', im)
    cv2.waitKey(0)
