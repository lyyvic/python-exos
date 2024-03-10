# -*- coding: utf-8 -*-

"""
 * @author : Parriault Lyse 
 * @email : lyse.parriault@cpe.fr
 * @date : 11/03/2024, lundi
 * TODO : Game viewer
 * writing preset : snake_case
"""

import tkinter as tk
from rectangle import Rectangle as rct


class app(tk.Tk):
    def __init__(self):
        #Initialisation de la fênetre de jeu
        super().__init__()
        self.title("Game")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(background='White')

        # Création et positionnement du bouton Quitter
        quit_button = tk.Button(self, text="Quitter", command=self.quit, bg="White")  
        quit_button.pack(side='left', padx=10, pady=10)

        self.bind("<Right>", self.create_rectangle)         # bind affecter une touche 
    


    def create_rectangle(self, event):
        self.rect = rct(self)
        

    def quit(self):
        #Fonction pour fermer l'application.
        self.destroy()