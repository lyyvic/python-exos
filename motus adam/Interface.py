#HEADER
"""PARTIEL CS-DEV 
Fichier interface 
Adam KACHER
18/12/2023
To do : -Finir ce fichier eet le render compatible avec le main et le fichier motus """

from tkinter import *
from tkinter import messagebox
from Motus import Jeu

class Interface :
        
    def creation(): #Méthode qui permet de lancer le jeu

        global jeu

        if jeu: #Si le jeu est déjà en cours

            jeu.effacer_joueur()  # Efface l'ancien joueur s'il existe
            jeu = Jeu(canvas) #Appelle à la zone de jeu
            canvas.focus_set()
            return

        else: #Si le jeu n'a pas déjà été lancé

            jeu = Jeu(canvas)
            canvas.focus_set()

    def fermer(): # Crée une fenêtre qui demande au joueur s'il veut vraiment quitter et ferme le programme s'il répond oui
        
        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"): #Demande l'info au joueur par un petit texte

            Mafenetre.destroy() #Détruit la fenetre si oui


    # Création de la fenêtre principale
    Mafenetre=Tk()
    Mafenetre.title('Motus')
    Mafenetre.geometry('800x800')

    #Création du canvas
    canvas = Canvas(Mafenetre, width=800, height=800, bg='white')
    canvas.focus_set()
    canvas.pack(padx=10, pady=10)

    # Création des boutons
    boutonStart = Button(Mafenetre, text="Start", command=creation) #Bouton start
    canvas.create_window(10, 10, anchor=NW, window=boutonStart)

    boutonQuitter = Button(Mafenetre, text="Quitter le jeu", command=fermer) #Bouton quitter le jeu
    canvas.create_window(10, 40, anchor=NW, window=boutonQuitter)

    #Ajoute l'affichage du score
    score_label = canvas.create_text(10, 100, anchor=NW, text="Score: 0\nMeilleur Score: 0", fill="white", font=("Helvetica", 12))

    jeu = None 