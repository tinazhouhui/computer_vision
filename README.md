# Image processing

[![Codeac](https://static.codeac.io/badges/2-274741179.svg "Codeac.io")](https://app.codeac.io/github/tinazhouhui/image_procesing)

All about discovery of computer vision and Open CV.

## Run
```bash
python3 start.py [insert argument]
```
#### Available arguments
- blend - blending two images together (using addWeighted)
- bitwise operations - creates a logo that is inserted to a picture
- convolution - will run all available convolutions
- ~~edge detection - shows different methods of edge detection~~
- gamma correction - gamma adjustment via linear stretching
- coin detection - compares outputs of manual and Hough detection of circles (coins)

## Requirements
- Open CV
- NumPy
```bash
pip3 install -r requirements.txt
```

## Remote Ubuntu access
- PyCharm terminal:
```bash
ssh -p 2222 tina@127.0.0.1
```
- If you are using Windows, Ubuntu and PyCharm community edition together
```bash
sudo service ssh start
```