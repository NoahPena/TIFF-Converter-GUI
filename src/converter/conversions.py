
from PIL import Image
import customtkinter as ctk

import os

def convert_tiff_images(input_files: list[str], output_format: str, output_directory: str, progress_bar: ctk.CTkProgressBar, output_text_box: ctk.CTkTextbox, recreate_directory_structure: bool = False, recreate_directory_base: str = ""):
    """
    Convert a list of TIFF images to the specified format and save them to the output directory.

    :param input_files: List of paths to input TIFF files.
    :param output_format: Desired output format (e.g., 'PNG', 'JPEG').
    :param output_directory: Directory where converted files will be saved.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    step_size = 1 / len(input_files)
    current_progress = 0

    for file_path in input_files:
        try:
            with Image.open(file_path) as img:

                if recreate_directory_structure:
                    relative_path = os.path.relpath(os.path.dirname(file_path), recreate_directory_base)
                    target_directory = os.path.join(output_directory, relative_path)
                    if not os.path.exists(target_directory):
                        os.makedirs(target_directory)
                    output_directory = target_directory

                base_name = os.path.basename(file_path)
                name_without_ext = os.path.splitext(base_name)[0]
                output_file_path = os.path.join(output_directory, f"{name_without_ext}.{output_format.lower()}")

                match output_format.upper():
                    case 'JPEG':
                        convert_to_jpeg(img, output_file_path)
                    case 'PNG':
                        convert_to_png(img, output_file_path)
                    case 'BMP':
                        convert_to_bmp(img, output_file_path)
                    case _:
                        output_text_box.configure(state="normal")
                        output_text_box.insert("end", f"Unsupported output format: {output_format}\n")
                        output_text_box.configure(state="disabled")
                        raise ValueError(f"Unsupported output format: {output_format}")

                current_progress += step_size
                progress_bar.set(current_progress)

                output_text_box.configure(state="normal")
                output_text_box.insert("end", f"Converted {file_path} to {output_file_path}\n")
                output_text_box.configure(state="disabled")
        except Exception as e:
            output_text_box.configure(state="normal")
            output_text_box.insert("end", f"Failed to convert {file_path}: {e}\n")
            output_text_box.configure(state="disabled")

def convert_to_jpeg(input_image: Image.Image, output_file: str):
    """
    Convert an image to JPEG format.

    :param input_image: PIL Image object.
    :return: Converted PIL Image object in JPEG format.
    """
    rgb_image = input_image.convert('RGB')
    rgb_image.save(output_file, format='JPEG')

def convert_to_png(input_image: Image.Image, output_file: str):
    """
    Convert an image to PNG format.

    :param input_image: PIL Image object.
    :return: Converted PIL Image object in PNG format.
    """
    input_image.save(output_file, format='PNG')

def convert_to_bmp(input_image: Image.Image, output_file: str):
    """
    Convert an image to BMP format.

    :param input_image: PIL Image object.
    :return: Converted PIL Image object in BMP format.
    """
    input_image.save(output_file, format='BMP')