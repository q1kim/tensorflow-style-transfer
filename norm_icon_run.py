import cv2
import os
import sys
import numpy as np

def main(argv):
    content = argv[0]
    style = argv[1]
    output = argv[2]
    loss_ratio = "1"
    interim_content = "img_without_alpha.jpg"
    interim_output = "interim_" + output
    exec_format = "python run_main.py --loss_ratio {} --content {} --style {} --output {}"

    norm_icon_w, norm_icon_h = (256, 256)
    norm_frame_w, norm_frame_h = (512, 512)
    icon_x = (norm_frame_w - norm_icon_w) >> 1;
    icon_y = (norm_frame_h - norm_icon_h) >> 1;

    img_with_alpha = cv2.imread(content, -1);
    norm_with_alpha = cv2.resize(img_with_alpha, (norm_icon_w, norm_icon_h), cv2.INTER_CUBIC)
    black_frame = np.zeros((norm_frame_w, norm_frame_h, 3), np.uint8)

    height, width, channels = norm_with_alpha.shape

    if channels >= 4:
        alpha = norm_with_alpha[:,:,3]
        img_without_alpha = norm_with_alpha[:,:,:3]
    else:
        img_without_alpha = norm_with_alpha

    black_frame[icon_y:icon_y+norm_icon_h, icon_x:icon_x+norm_icon_w] = img_without_alpha
    cv2.imwrite(interim_content, black_frame);
    exec_string = exec_format.format(loss_ratio, interim_content, style, interim_output)
    print(exec_string)
    os.system(exec_string)

    processed = cv2.imread(interim_output)
    processed = processed[icon_y:icon_y+norm_icon_h, icon_x:icon_x+norm_icon_w]

    try:
        os.remove(interim_content)
        os.remove(interim_output)
    except:
        pass

    original_resized = cv2.resize(processed, (width, height), cv2.INTER_CUBIC)

    if channels >= 4:
        merged = cv2.merge((original_resized, alpha))
    else:
        merged = original_resized

    cv2.imwrite(output, merged)

if __name__ == "__main__":
    main(sys.argv[1:])

