# Image processing

[![Codeac](https://static.codeac.io/badges/2-274741179.svg "Codeac.io")](https://app.codeac.io/github/tinazhouhui/image_procesing)

All about discovery of computer vision and Open CV.

## Run
```bash
python3 start.py [insert argument]
```
#### Available arguments
- draw - basic manipulation with images
- blend - blending two images together (addWeighted)
- bitwise operations
- convolution - will run all available convolutions
- gamma correction - gamma adjustment via linear stretching
- coin recognition

## Requirements
- Open CV
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