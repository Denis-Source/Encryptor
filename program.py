import threading
from interface_elements import Interface
from cypher import *
import tkinter as tk
from Cryptodome.Random import get_random_bytes
from tkinter import filedialog as fd


class Program:
    def __init__(self):
        self.i = Interface()
        self.path = ""
        self.dirpath = ""
        self.iv = b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
        self.elements = self.i.interface_elements_dict
        self.to_brute = self.i.to_brute

    def pack_elements(self):
        for key in self.elements.keys():
            elem = self.elements[key]["element"]
            params = self.elements[key]["params"]
            elem.pack(**params)
            if "list" in key:
                list_params = self.elements[key]["list_params"]
                list_items = self.elements[key]["list_items"]
                for list_item in list_items:
                    elem.insert(0, list_item)
                elem.select_set(0)
                elem.configure(**list_params)

    def select_file(self, event):
        self.path = fd.askopenfilename()

    def select_dir(self, event):
        self.dirpath = fd.askdirectory()

    def generate(self, event):
        self.elements["vector_e"]["element"].delete(0, tk.END)
        self.elements["vector_e"]["element"].insert(0, get_random_bytes(16).hex())

    def set_vector(self):
        string_iv = self.elements["vector_e"]["element"].get()
        if len(string_iv) > 32:
            string_iv = string_iv[:32]
        elif len(string_iv) < 32:
            string_iv += "f" * (32 - len(string_iv))
        self.iv = bytes.fromhex(string_iv)

    def encdenc(self):
        self.elements["info_l"]["element"]["text"] = ""
        key = self.elements["key_e"]["element"].get()
        self.set_vector()
        if self.to_brute.get():
            decrypt(
                self.path,
                self.dirpath,
                key,
                self.iv
            )
        else:
            encrypt(
                self.path,
                self.dirpath,
                key,
                self.iv
            )
        self.elements["info_l"]["element"]["text"] = "Done!"

    def start(self, event):
        threading.Thread(target=self.encdenc).start()

    def mainloop(self):
        self.elements["vector_e"]["element"].insert(0, self.iv.hex())
        self.elements["select_file_b"]["element"].bind("<Button-1>", self.select_file)
        self.elements["select_dir_b"]["element"].bind("<Button-1>", self.select_dir)
        self.elements["generate_b"]["element"].bind("<Button-1>", self.generate)
        self.elements["start_b"]["element"].bind("<Button-1>", self.start)
        self.pack_elements()
        self.i.root.mainloop()
