
from PIL import Image
import customtkinter as ctk

import os
import glob

ctk.set_widget_scaling(1.2)
ctk.set_window_scaling(1.2)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TIFF Converter GUI")
        # self.geometry("1200x600")

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self._setup_ui()

    def _setup_ui(self):

        # Upper Frame
        self.upper_frame = ctk.CTkFrame(self)
        self.upper_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Input Frame
        self.input_frame = ctk.CTkFrame(self.upper_frame)
        self.input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.input_label = ctk.CTkLabel(self.input_frame, text="Input Files:")
        self.input_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_files_textbox = ctk.CTkTextbox(self.input_frame, width=400, height=200)
        self.input_files_textbox.configure(state="disabled")
        self.input_files_textbox.grid(row=1, column=0, padx=10, pady=10)

        self.input_button_frame = ctk.CTkFrame(self.input_frame)
        self.input_button_frame.grid(row=2, column=0, padx=10, pady=10)
        self.input_button_frame.configure(fg_color="transparent")

        self.input_file_browse_button = ctk.CTkButton(master=self.input_button_frame, text="Browse Files", command=self.input_file_picker)
        self.input_file_browse_button.grid(row=2, column=0, padx=10, pady=10)

        self.input_directory_browse_button = ctk.CTkButton(master=self.input_button_frame, text="Browse Directories", command=self.input_directory_picker)
        self.input_directory_browse_button.grid(row=2, column=1, padx=10, pady=10)

        self.do_recursive_checkbox = ctk.CTkCheckBox(self.input_frame, text="Process directories recursively", command=self.recursive_directory_disabler)
        self.do_recursive_checkbox.grid(row=3, column=0, padx=5, pady=10)

        # Conversion Frame
        self.conversion_frame = ctk.CTkFrame(self.upper_frame)
        self.conversion_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.file_type_picker_label = ctk.CTkLabel(self.conversion_frame, text="Convert To:")
        self.file_type_picker_label.grid(row=0, column=0, padx=10, pady=10)

        self.arrow_image = ctk.CTkImage(light_image=Image.open("assets/arrow.png"), dark_image=None, size=(100, 100))
        self.arrow_label = ctk.CTkLabel(self.conversion_frame, image=self.arrow_image, text="")
        self.arrow_label.grid(row=1, column=0, padx=10, pady=10)

        self.file_type_picker = ctk.CTkOptionMenu(self.conversion_frame, values=["PNG", "JPEG", "BMP"])
        self.file_type_picker.grid(row=2, column=0, padx=10, pady=10)

        # Output Frame
        self.output_frame = ctk.CTkFrame(self.upper_frame)
        self.output_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.output_label = ctk.CTkLabel(self.output_frame, text="Output Directory:")
        self.output_label.grid(row=0, column=8, padx=10, pady=10)

        self.output_directory_textbox = ctk.CTkTextbox(self.output_frame, width=400, height=50)
        self.output_directory_textbox.configure(state="disabled")
        self.output_directory_textbox.grid(row=1, column=8, padx=10, pady=10)

        self.output_directory_browse_button = ctk.CTkButton(self.output_frame, text="Browse", command=self.output_directory_picker)
        self.output_directory_browse_button.grid(row=2, column=8, padx=10, pady=10)

        self.recreate_folder_structure_checkbox = ctk.CTkCheckBox(self.output_frame, text="Recreate folder structure in output directory")
        self.recreate_folder_structure_checkbox.configure(state="disabled")
        self.recreate_folder_structure_checkbox.grid(row=3, column=8, padx=10, pady=10)

        # Lower Frame
        self.lower_frame = ctk.CTkFrame(self)
        self.lower_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.lower_frame.grid_columnconfigure(0, weight=1)

        self.convert_button = ctk.CTkButton(self.lower_frame, text="Convert", width=200)
        self.convert_button.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

    def input_file_picker(self):
        filenames = ctk.filedialog.askopenfilenames(title="Select files", filetypes=[("TIFF files", "*.tiff *.tif"), ("All files", "*.*")])
        self.input_files_textbox.configure(state="normal")
        self.input_files_textbox.delete("0.0", "end")
        self.input_files_textbox.configure(state="disabled")
        for filename in filenames:
            self.input_files_textbox.configure(state="normal")
            self.input_files_textbox.insert("end", f"{filename}\n")
            self.input_files_textbox.configure(state="disabled")
        print(f"Selected files: {filenames}")

    def input_directory_picker(self):
        directory = ctk.filedialog.askdirectory(title="Select directory")
        search_pattern = os.path.join(directory, '**', '*.tiff')
        tiff_files = glob.glob(search_pattern, recursive=self.do_recursive_checkbox.get())
        for file in tiff_files:
            self.input_files_textbox.configure(state="normal")
            self.input_files_textbox.insert("end", f"{file}\n")
            self.input_files_textbox.configure(state="disabled")
        print(f"Selected directory: {directory}")

    def recursive_directory_disabler(self):
        if self.do_recursive_checkbox.get():
            self.recreate_folder_structure_checkbox.configure(state="normal")
        else:
            self.recreate_folder_structure_checkbox.deselect()
            self.recreate_folder_structure_checkbox.configure(state="disabled")

    def output_directory_picker(self):
        directory = ctk.filedialog.askdirectory(title="Select output directory")
        self.output_directory_textbox.configure(state="normal")
        self.output_directory_textbox.insert("end", f"{directory}\n")
        self.output_directory_textbox.configure(state="disabled")
        print(f"Selected directory: {directory}")
