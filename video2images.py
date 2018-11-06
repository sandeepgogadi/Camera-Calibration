import cv2
import os
import glob


def video_to_frames(video, path_output_dir):

    vidcap = cv2.VideoCapture(video)
    count = 0
    c = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2.imwrite(os.path.join(path_output_dir, '{}.{}.png'.format(c, count)), image)
            count += 1
            if count == 30:
                count = 0
                c += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()


def create_dir(file_path):
    if not os.path.isdir(file_path):
        os.mkdir(file_path)


paths = ['./data', './data/test/', './data/test/rgb']

for path in paths:
    create_dir(path)

video_to_frames('video.mkv', './data/test/rgb')

images_list = sorted(glob.glob('./data/test/rgb/*'))

with open('./data/test/rgb.txt', 'w') as f:
    for img in images_list:
        f.write(img.split('/')[-1][:-4] + ' ' + img + '\n')
