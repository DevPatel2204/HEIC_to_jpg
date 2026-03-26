from logic import convert_folder_heic_to_jpg
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_folder_heic_to_jpg(input_folder, output_folder)
