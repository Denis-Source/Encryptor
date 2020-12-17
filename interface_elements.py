import tkinter as tk

from int_sett import IntSett


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg=IntSett.bg_color)
        self.to_brute = tk.BooleanVar()
        self.interface_elements_dict = {
            "main_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 24, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="AES-128"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "key_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter key:"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "key_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=(IntSett.font, 20, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=15
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "vector_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                        text="Enter Initialisation Vector:"
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "vector_e": {
                "element":
                    tk.Entry(
                        self.root,
                        font=("Courier New", 14, "bold"),
                        fg=IntSett.text_color,
                        bg=IntSett.bg_color,
                        width=32
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "generate_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Generate",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "brute_check": {
                "element":
                    tk.Checkbutton(
                        text="Decrypt",
                        variable=self.to_brute,
                        font=(IntSett.font, 14, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "select_file_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Select file",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "select_dir_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Select directory",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },


            "start_b": {
                "element":
                    tk.Button(
                        self.root,
                        text="Start",
                        font=(IntSett.font, 20),
                        bg=IntSett.bu_color,
                        fg=IntSett.bg_color
                    ),
                "params":
                    {
                        "pady": 10,
                        "padx": 10,
                    }
            },
            "info_l": {
                "element":
                    tk.Label(
                        self.root,
                        font=(IntSett.font, 18, "bold"),
                        bg=IntSett.bg_color,
                        fg=IntSett.label_color,
                    ),
                "params":
                    {
                        "padx": 10,
                        "pady": 10,
                    }
            }
        }
