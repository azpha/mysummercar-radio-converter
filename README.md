# mysummercar-radio-converter

Easily convert mp3 files to ogg files for use in My Summer Car's Radio system

## Prerequisites

- Python
- [FFmpeg](https://ffmpeg.org) (for conversion)

## Running

Create a `music` folder in the same directory as this script. Drop your .mp3 files into it. Run `python convert.py` and supply the required arguments when prompted;

- the **full** path to `steamapps/common/My Summer Car`

the script will automatically find your radio directory, convert the files to .ogg format & drop them in with the correct naming scheme.
