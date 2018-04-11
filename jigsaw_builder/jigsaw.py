import numpy as npy
import cv2

__author__ = 'user'
"""
#src_coord = [(0, 0), (40, 40)]
#dest_coord = [(840, 560), (880, 600)]
"""

img = cv2.imread("a.png")
img_dest = npy.zeros((int(img.shape[0]), int(img.shape[1]), 3), npy.uint8)
img_shape = img.shape
num_rows = 18
num_cols = 32


def tile_image(img, num_rows, num_cols):
    tile_height = int(img.shape[0] / num_rows)
    tile_width = int(img.shape[1] / num_cols)
    tiles = []
    locations = {}
    for row in range(num_rows):
        for col in range(num_cols):
            src_c_x0 = input('Enter source tile src x0 such as 0: ')
            src_c_y0 = input('Enter source tile src y0 such as 0: ')
            src_coord = [(src_c_x0, src_c_y0), (src_c_x0 + 40, src_c_y0 + 40)]
            dest_c_x0 = input('Enter destination tile src x0 such as 840: ')
            dest_c_y0 = input('Enter destination tile src y0 such as 560: ')
            dest_coord = [(dest_c_x0, dest_c_y0), (dest_c_x0 + 40, dest_c_y0 + 40)]
            y0 = row * tile_height
            y1 = y0 + tile_height
            x0 = col * tile_width
            x1 = x0 + tile_width
            locations[row] = [(x0,y0), (x1,y1)]
            tiles.append(img[y0:y1, x0:x1])
            #The dest images' "dest_coordinates" are equal to the src images' "source_coordinates"
            img_dest[dest_coord[0][1]:dest_coord[1][1], dest_coord[0][0]:dest_coord[1][0]] = img[src_coord[0][1]:src_coord[1][1], src_coord[0][0]:src_coord[1][0]]
            cv2.imwrite('dest.jpg', img_dest)
            cv2.destroyAllWindows
    return tiles


tile_image(img, num_rows, num_cols)



