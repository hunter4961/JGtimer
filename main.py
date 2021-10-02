#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

class MainApplication(Frame):

    def __init__(self, master):
        self.master = master
        ttk.Frame.__init__(self, self.master)
        self.id_label = ttk.Label(self)
        self.id_entry = ttk.Entry(self)
        self.search_button = ttk.Button(self)
        self.result_box = Text(self)
        self.configure_gui()
        self.create_widgets()

    def get_matchdata(self, *args):
        print()
        # TODO

    def configure_gui(self): # Ebben a metódusban adjuk meg, hogyan nézzenek ki a widgeteink
        self.id_label.configure(text='Username')
        self.id_entry.configure(textvariable=id_var)
        self.search_button.configure(text='Search...')
        self.configure(width=300, height=300)  # Beállítja az ablak méretét pixelekben

    def create_widgets(self): # Ez a metódus tölti be őket a megfelelő helyre a gridben
        self.grid()
        self.id_label.grid(row=0, column=0)
        self.id_entry.grid(row=1, column=0)
        self.search_button.grid(row=1, column=1)
        self.result_box.grid(row=2, column=0, columnspan=2)


if __name__ == '__main__':
    root = Tk()
    id_var = StringVar()  # Sztringváltozó amiben a lekérendő felhasználó azonosítóját tartjuk
    main_app = MainApplication(root)
    root.mainloop()
