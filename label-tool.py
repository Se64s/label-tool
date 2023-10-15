import sys
import os
import typer
from PIL import Image, ImageDraw, ImageFont

DEFAULT_WIDTH = 72
DEFAULT_HIGH = 12
DEFAULT_FONT = os.path.dirname(os.path.abspath(__file__)) + "/misc/retro.ttf"
DEFAULT_FONT_SIZE = 10
DEFAULT_BG_COLOR = "black"
DEFAULT_FG_COLOR = "white"


def main(labeltext: str, 
         labelfont: str=DEFAULT_FONT, 
         width: int=DEFAULT_WIDTH, 
         high: int=DEFAULT_HIGH, 
         bg: str=DEFAULT_BG_COLOR, 
         fg: str=DEFAULT_FG_COLOR,
         offset: int=DEFAULT_WIDTH/2, 
         getsize: bool=False):
    """
    Generate a label image in ppm format.
    """
    # Generate base image
    font = ImageFont.truetype(labelfont, DEFAULT_FONT_SIZE)
    im = Image.new("RGB", (width, high), bg)
    d = ImageDraw.Draw(im)
    d.fontmode="1"    
    # Add text label
    d.text((offset, high/2), labeltext, fill=fg, anchor="mm", font=font)
    # Check size option
    if getsize:
        print(f"{int(d.textlength(labeltext, font=font))}")
    else:
        im.save(sys.stdout, "PPM")

if __name__ == "__main__":
    typer.run(main)

# EOF
