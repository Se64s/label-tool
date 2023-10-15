import sys
import os
import typer
from PIL import Image, ImageDraw, ImageFont

DEFAULT_WIDTH = 72
DEFAULT_HIGH = 12
DEFAULT_FONT = os.path.dirname(os.path.abspath(__file__)) + "/misc/xpaider.ttf"
DEFAULT_FONT_SIZE = 8
DEFAULT_FONT_SIZE_MULTILINE = 6
DEFAULT_BG_COLOR = "black"
DEFAULT_FG_COLOR = "white"


def ComputeLabelSize(text: str, fontpath: str, fontsize: int, fontsizemulti: int, draw: ImageDraw, maxwidth: int):
    label_str=text
    font = ImageFont.truetype(fontpath, fontsize)
    if draw.textlength(label_str, font=font) > maxwidth:
        label_str=""
        split_text = text.split()
        split_index = int(len(split_text)/2)
        # Process line 1
        for word in split_text[:split_index]:
            label_str += word + " "
        label_str = label_str + "\n"
        # Process line 2
        for word in split_text[split_index:]:
            label_str += word + ""
        font = ImageFont.truetype(fontpath, fontsizemulti)
    return (label_str, font)
 

def main(labeltext: str, 
         labelfont: str=DEFAULT_FONT, 
         width: int=DEFAULT_WIDTH, 
         high: int=DEFAULT_HIGH, 
         bg: str=DEFAULT_BG_COLOR, 
         fg: str=DEFAULT_FG_COLOR):
    """
    Generate a label image in ppm format.
    """
    # Generate base image
    im = Image.new("RGB", (width, high), bg)
    d = ImageDraw.Draw(im)
    d.fontmode="1"    
    # Compute font size
    (labeltext, font) = ComputeLabelSize(labeltext, labelfont, DEFAULT_FONT_SIZE, DEFAULT_FONT_SIZE_MULTILINE, d, width)
    # Add text label
    d.multiline_text((width/2, high/2), labeltext, fill=fg, anchor="mm", font=font, spacing=0, align="center")
    im.save(sys.stdout, "PPM")

if __name__ == "__main__":
    typer.run(main)

# EOF
