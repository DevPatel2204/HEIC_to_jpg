from pillow_heif import register_heif_opener
from PIL import Image
from pathlib import Path
import os
import sys
import io



register_heif_opener()

# Can use for single file conversion.  

def convert_heic_to_jpg(input_path, output_path, quality=85):

    #output_path = Path(output_folder) / (Path(input_path).stem +'.jpg')
    
    with Image.open(input_path) as img:
        rgb_image = img.convert('RGB')
        rgb_image.save(output_path,'JPEG', quality=quality)
        print(f"COnverted{input_path} to {output_path}with quality {quality}")

'''
# convert_heic_to_jpg('photo.heic','photo.jpg').   
Add the above line to test or if using single file conversion
'''

# Convert all HEiC files in a folder to jpg, can also manipulate quality by adjusing quality parameter.
def convert_folder_heic_to_jpg(input_folder, output_folder, quality=85):
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True,exist_ok=True)

    heic_files = list(input_folder.glob('*.heic')) + list(input_folder.glob('*.HEIC')) # I have added both lower and upper case HEIC as macos and ios can save in both formats.

    if not heic_files:
        print(f"No HEIC files found in {input_folder}")
        return
    for heic_file in heic_files:
        output_path = output_folder / (heic_file.stem+'.jpg')
        convert_heic_to_jpg(heic_file,output_path,quality)
    
def convert_heic_bytes_to_jpg(file_bytes,quality=85):
    img = Image.open(io.BytesIO(file_bytes))
    rgb_image = img.convert('RGB')
    output = io.BytesIO()
    rgb_image.save(output, 'JPEG', quality=quality)
    output.seek(0)
    return output


# This code moved to main.py to allow for CLI usage.

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <input_folder> <output_folder>")
#         sys.exit(1)

#     input_folder = sys.argv[1]
#     output_folder = sys.argv[2]

#     convert_folder_heic_to_jpg(input_folder, output_folder)

