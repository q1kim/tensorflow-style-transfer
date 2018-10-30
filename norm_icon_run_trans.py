import cv2
import os
import sys
import numpy as np

def main(argv):
    content = argv[0]
    style = argv[1]
    output = argv[2]

    norm_icon_w, norm_icon_h = (256, 256)
    norm_frame_w, norm_frame_h = (512, 512)
    img_with_alpha = cv2.imread(content, -1);
    norm_with_alpha = cv2.resize(img_with_alpha, (norm_icon_w, norm_icon_h), cv2.INTER_CUBIC)

    height, width, channels = norm_with_alpha.shape

    if channels >= 4:
        alpha = norm_with_alpha[:,:,3]
        alpha = cv2.multiply(alpha, 0.7)
        img_without_alpha = norm_with_alpha[:,:,:3]
    else:
        img_without_alpha = norm_with_alpha

    original_resized = img_without_alpha

    if channels >= 4:
        merged = cv2.merge((original_resized, alpha))
    else:
        merged = original_resized

    cv2.imwrite(output, merged)

if __name__ == "__main__":
    main(sys.argv[1:])

