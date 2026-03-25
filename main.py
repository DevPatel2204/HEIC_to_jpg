from pillow_heif import register_heif_opener
from PIL import Image
from pathlib import Path
import os
import sys

register_heif_opener()

def convert_heic_to_jpg(input_path, output_path, quality=85):

    #output_path = Path(output_folder) / (Path(input_path).stem +'.jpg')
    
    with Image.open(input_path) as img:
        rgb_image = img.convert('RGB')
        rgb_image.save(output_path,'JPEG', quality=quality)
        print(f"COnverted{input_path} to {output_path}with quality {quality}")
    
convert_heic_to_jpg('photo.heic','photo.jpg')