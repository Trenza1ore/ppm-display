"""
Usage:
    ppm-disp -i
    ppm-disp [-d] <file>...
    ppm-disp [-s] <size> <file>...

Options:
    -i  about the tool
    -d  display ppm/pgm images (maximum windows size: 600x600)
    -s  display images with a set maximum windows size
"""

from docopt import docopt
import cv2 as cv

def show_img(id: int, filepath: str, size: int = 600) -> None:
    window_name = "img %d | %s" %(id, cut_string(filepath))
    img = cv.imread(filepath)
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    
    width, height, _ = img.shape
    if max(width, height) > size:
        ratio = width / height
        if width > height:
            cv.resizeWindow(window_name, size, size // ratio)
        else:
            cv.resizeWindow(window_name, round(size * ratio), size)
            
    cv.imshow(window_name, img)

def cut_string(x: str) -> None:
    if len(x) > 30:
        return x.split('/')[-1]
    return x

def parse_args(args: dict) -> list:
    paths = [i.replace("\\", "/") for i in args["<file>"]]
    return paths

def main():
    args = docopt(__doc__)
    if args["-i"] == True:
        print("This tool was written by Hugo in 2022 to display ppm and pgm files.")
    elif args["-s"] == True:
        data = parse_args(args=args)
        size = data[0]
        for i, val in enumerate(data[1:]):
            show_img(i, val, size);
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        data = parse_args(args=args)
        for i, val in enumerate(data):
            show_img(i, val);
        cv.waitKey(0)
        cv.destroyAllWindows()