from tkinter import Toplevel, Button

from Creational.singleton import *
from Creational.abstract_factory import *


class Extra(Toplevel, Singleton):

    def init(self):
        super().__init__()
        self.title("EQs")
        self.geometry("900x600")
        self.button = Button(self, text="Show EQs", command=self.show_EQs)
        self.button.pack(expand=True)

    def __init__(self):         # При этой реализации
        pass

    def show_EQs(self):
        eqsFactory = EQsFactory()
        eqs = eqsFactory.eqs

        for e in eqs:       # Именно в этом цикле при нескольких нажатиях на Show_eqs выводятся кнопки
            self.button = Button(self, text=f"{e.name}")
            self.button.pack(expand=True)

    def del_window(self):   # Удалять объект окна перехватывая кнопку закрытия
        pass                # чтобы можно было его создавать заново   destroy()

