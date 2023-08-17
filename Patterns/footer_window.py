from tkinter import *
from Creational.factoty_method import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Footer bar")
        self.geometry("700x400")

        self.entry = Entry(self, width=15, textvariable=StringVar())
        self.entry.pack()

        self.button = Button(self, text="Show plugins", command=self.show_plugins)
        self.button.pack(expand=True)

    def show_plugins(self):
        drop = self.entry.get()
        effect = Creator().Factory(drop)

        if effect:
            label = Label(self, text=f"You dropped {effect.type}")
            label.pack()

