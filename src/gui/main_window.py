
import customtkinter as ctk

ctk.set_widget_scaling(1.2)
ctk.set_window_scaling(1.2)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TIFF Converter GUI")
        self.geometry("800x600")

        self._setup_ui()

    def _setup_ui(self):
        label = ctk.CTkLabel(self, text="Welcome to the TIFF Converter GUI!")
        label.pack(pady=20)

        button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        button.pack(pady=10)

    def on_button_click(self):
        print("Button was clicked!")