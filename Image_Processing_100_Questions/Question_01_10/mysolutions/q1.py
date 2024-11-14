#!/usr/bin/env python3

import cv2
import numpy as np

img = cv2.imread("./assets/imori.png").astype(np.float32)

W, H, C = img.shape

grayscale = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
out = grayscale.astype(np.uint8)


max_sigma = 0
max_t = 0
