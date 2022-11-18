# ppm-display
 A simple tool that displays ppm/pgm files via OpenCV and saves the images in png format. The default maximum window size is 600x600.
## Usage
    ppm-disp -i
    ppm-disp -s <size> <file>...
    ppm-disp <file>...
## Options
    -i  about the tool
    -s  display images with a non-default maximum windows size
## Possible Use Case
    - Create a batch file/shell script with the following line:
    - (Windows) ppm-disp %*
    - (Linux)   ppm-disp $*
    - And now you can drag-and-drop ppm/pgm files into it and view the images instantly
    - A batch file example is included in the Github repo