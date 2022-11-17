"""
Usage:
    ppm-disp -i
    ppm-disp -s <size> <file>...
    ppm-disp <file>...

Options:
    -i  about the tool
    -s  display images with a non-default maximum windows size
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
        print('s', data, args)
        try:
            size = int(args["<size>"])
        except:
            print(f"Size ({args['<size>']}) is not entered as an integer.")
            return
        for i, val in enumerate(data):
            show_img(i, val, size);
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        data = parse_args(args=args)
        print(data)
        for i, val in enumerate(data):
            show_img(i, val);
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()