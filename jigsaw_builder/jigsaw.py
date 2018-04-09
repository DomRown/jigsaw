import numpy as npy
import cv2

__author__ = 'user'

img = cv2.imread("a.png")
img_dest = npy.zeros((int(img.shape[0]), int(img.shape[1]), 3), npy.uint8)
img_shape = img.shape
num_rows = 18
num_cols = 32
tile_size = (40, 40)
brown_thresh = [68, 79, 91]
green_thresh = [131, 222, 178]


def tile_image(img, num_rows, num_cols, input_coord):
    tile_height = int(img.shape[0] / num_rows)
    tile_width = int(img.shape[1] / num_cols)
    tiles = []
    locations = {}
    for row in range(num_rows):
        for col in range(num_cols):
            y0 = row * tile_height
            y1 = y0 + tile_height
            x0 = col * tile_width
            x1 = x0 + tile_width
            locations[row] = [(x0,y0), (x1,y1)]
            tiles.append(img[y0:y1, x0:x1])
            np_tile = img[y0:y1, x0:x1]
            #at ths point we have the src tile, then we need to PICK the dest loc.
            img_dest[input_coord[0][1]:input_coord[1][1], input_coord[0][0]:input_coord[1][0]] = img[y0:y1, x0:x1]
            cv2.imwrite('dest.jpg', img_dest)
            cv2.destroyAllWindows
    return tiles

input_coord=[(840, 560), (880, 600)]
tile_image(img, num_rows, num_cols, input_coord)

#840,560 880,600 nose1
#1080,320 1120, 360 nose2
#y0 = row * tile_height
#y1 = y0 + tile_height
#x0 = col * tile_width
#x1 = x0 + tile_width

