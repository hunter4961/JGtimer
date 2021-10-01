#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk


class MainApplication(Frame):

    def __init__(self, master):
        self.master = master
        ttk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()


    def congigure_gui(self):
    # ...

    def create_widgets(self):
    # ...

if __name__ == '__main__':
    root = Tk()
    main_app = MainApplication(root)
    root.mainloop()