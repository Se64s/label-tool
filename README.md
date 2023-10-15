#  Label generator tool

Tool to generate label images in format ppm.

## Requirements

```
python==3.10
typer==0.9.0
Pillow==10.0.1
```

## Install instructions

```
python -m pip install -r requirements.txt 
```

## Usage

```
Usage: label-tool.py [OPTIONS] LABELTEXT

  Generate a label image in ppm format.

Arguments:
  LABELTEXT  [required]

Options:
  --labelfont TEXT  [default: /home/smg/Proyectos/06_panel_img_gen/misc/VCR_OS
                    D_MONO.ttf]
  --width INTEGER   [default: 72]
  --high INTEGER    [default: 12]
  --bg TEXT         [default: black]
  --fg TEXT         [default: white]
  --help            Show this message and exit.
```
