#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk

#ez egy komment

class MainApplication(Frame):

    def __init__(self, master):
        self.master = master
        ttk.Frame.__init__(self, self.master)
        self.id_var = StringVar()  # Sztringváltozó amiben a lekérendő felhasználó azonosítóját tartjuk
        self.id_label = ttk.Label(self)  # A címke amin a bemeneti doboz felett jelenítünk meg szöveget
        self.id_entry = ttk.Entry(self)  # A bemeneti doboz amiben a felhasználó az azonosítóját adhatja meg
        self.search_button = ttk.Button(self)  # A gomb aminek a megnyomásával lefut a keresés
        self.result_box = Text(self)  # Textbox amibe majd megy a megformázott meccsadat
        self.configure_gui()
        self.create_widgets()

    def get_matchdata(self, *args):
        self.result_box.insert('1.0', self.id_entry.get())  # Teszt cucc...
        # A result_box insert metódusával tehetjuk majd bele a szöveget sorosával
        # az első paraméter a 'hanyadik sor. hanyadik karakter' formátumban
        # a második pedig a beillesztendő szöveg
        # TODO

    def configure_gui(self):  # Ebben a metódusban adjuk meg, hogyan nézzenek ki a widgeteink
        # Ablakon beluli widgetek:
        self.master.title('JGtimer')
        self.id_label.configure(text='Username:')
        self.id_entry.configure(textvariable=self.id_var)
        self.search_button.configure(text='Search...', command=self.get_matchdata)
        self.result_box.configure()
        #
        # Grid layout varázslás:
        self.master.geometry("300x450")
        # Ha azt akarom itt lehet "width x height" formátumban megadni az ablak méretét
        # pixelekben lesz megadva
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        # Ez a két sor kell ahhoz, hogy az ablak méretét lehessen dinamikusan változtatni
        # Ha azt végül nem akarjuk akkor nem kell
        for col in range(0, 2):
            self.columnconfigure(col, weight=1)
        for row in range(0, 2):
            self.rowconfigure(row, weight=1)
        self.rowconfigure(2, weight=2)
        # Súlyokat oszt a soroknak és oszlopoknak, még nem jó majd játsz vele nyugodtan
        # -Peti

    def create_widgets(self):  # Ez a metódus tölti be őket a megfelelő helyre a gridben
        self.grid(sticky=(N, W, E, S))  # "Ragadás"
        self.id_label.grid(row=0, column=0, sticky=W)  # A "Username:" labelt balra igazitja, a 0/0-as cellaban
        self.id_entry.grid(row=1, column=0, sticky=(W, E))  # A bemeneti box-ot átméretezi hogy a 1/0-as cellát kitöltse
        self.search_button.grid(row=1, column=1, sticky=W)  # A Kereső gombot odaragasztja az 1/1-es cella bal oldalára
        self.result_box.grid(row=2, column=0, columnspan=2, sticky=(N, W, E, S))
        # TODO:
        # - A result boxnak kéne kitalálni valami fix méretet, hogy köré igazítsam a dolgokat


if __name__ == '__main__':
    root = Tk()
    main_app = MainApplication(root)
    root.mainloop()
