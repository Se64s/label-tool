import sys
import os
import typer
from PIL import Image, ImageDraw, ImageFont

DEFAULT_WIDTH = 72
DEFAULT_HIGH = 12
DEFAULT_FONT = os.path.dirname(os.path.abspath(__file__)) + "/misc/VCR_OSD_MONO.ttf"
DEFAULT_BG_COLOR = "black"
DEFAULT_FG_COLOR = "white"


def main(labeltext: str, 
         labelfont: str=DEFAULT_FONT, 
         width: int=DEFAULT_WIDTH, 
         high: int=DEFAULT_HIGH, 
         bg: str=DEFAULT_BG_COLOR, 
         fg: str=DEFAULT_FG_COLOR):
    """
    Generate a label image in ppm format.
    """

    font = ImageFont.truetype(labelfont, high-1)
    im = Image.new("RGB", (width, high), bg)
    d = ImageDraw.Draw(im)
    d.fontmode="1"
    d.text((width/2, high/2), labeltext, fill=fg, anchor="mm", font=font)
    im.save(sys.stdout, "PPM")

if __name__ == "__main__":
    typer.run(main)

# EOF
