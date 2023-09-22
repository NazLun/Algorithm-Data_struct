from tkinter import *
from Structural.decorator import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Decorator window")
        self.geometry("400x200")
        self.dry = Entity("clear sound")
        label = Label(self, bg="white", width=30, text=self.dry.play())
        label.pack()

        def result(self):
            if check_eq.get() and not check_compress.get():
                dec_eq = EQ(self.dry)
                label.config(text=dec_eq.play())
            elif check_compress.get() and not check_eq.get():
                dec_compress = Compressor(self.dry)
                label.config(text=dec_compress.play())
            elif check_eq.get() and check_compress.get():
                dec_eq_compress = EQ(Compressor(self.dry))
                label.config(text=dec_eq_compress.play())
            else:
                label.config(text=self.dry.play())

        check_eq = IntVar(value=0)
        check_compress = IntVar(value=0)
        check_eq = Checkbutton(self, text="EQ", variable=check_eq, command=result)
        check_eq.pack()
        check_compress = Checkbutton(self, text="Compress", variable=check_compress, command=result)
        check_compress.pack()
