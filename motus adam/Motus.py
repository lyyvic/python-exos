#HEADER
"""PARTIEL CS-DEV 
Fichier Motus
Adam KACHER
18/12/2023
To do : - Le système de couleur (vert si correct, jaune si mal placées, rouge si absente du mot )
        - Compatibilité avec le fichier main """

from tkinter import *
import random
from colorama import Back, Style

class Jeu :


    def choix_mot(): # Fonction qui permet de choisir un mot alétoire depuis le fichier
        fich=open('MotsDeSixLettres.txt','r') # Ouvre le fichier texte MotsDeSixLettres
        mots = fich.readlines() # Lit une ligne du fichier et la renvoie sous forme de chaîne de listes
        return random.choice(mots).strip() # Choisit un mot aléatoire depuis le fichier

    def affiche_mot(mot, lettres_devinees): # Fonction qui affiche le mot à trouver
        mot_affiche = "" 
        for lettre in mot:
            if lettre in lettres_devinees:
                mot_affiche += lettre # Pour chaque lettre dévinée, elle remplace le vide à sa pace dans le mot
            else:
                mot_affiche += "_" # Laisse un espace lorsque la lettre n'appartient pas au mot
        return mot_affiche
    
    def jeu():
        print("Jeu du motus, vous avez 6 essais, bonne chance !") # message de présentation 
        mot_recherche = choix_mot() # identifie le mot à trouver grâce a la foncion choix_mot
        lettres_devinees = [mot_recherche[0]] # Donne la première lettre du mot à deviner
        essais = 6 # Définie le nombre d'essais qu'à le joueur
        while essais > 0: # Boucle qui se répète tant que le joueur a des essais
            mot_affiche = affiche_mot(mot_recherche, lettres_devinees)
            print("Mot actuel: " + mot_affiche) # Affiche le mot à trouver avec sa première lettre
            lettre = input("Devinez une lettre : ").lower() 
            if len(lettre) == 1 : # Vérifie que le joueur rentre bien une unique lettre
                if lettre in lettres_devinees:
                    print("Vous avez déjà deviné cette lettre.") # Empeche le joueur de remettre une lettre qu'il a déja trouvé 
                if lettre in mot_recherche:
                    print("Bien joué !") # Félicite le joueur d'avoir trouvé une lettre
                    lettres_devinees.append(lettre) # Ajoute la lettre dans le mot à déviner 
                    if mot_affiche == mot_recherche:
                        print("Félicitations, vous avez gagné ! Le mot était : " + mot_recherche) # Message de victoire
                        break # quitte la boucle de force afin de ne pas rester coincé
                else:
                    essais -= 1 # Enleve une chance d'essais
                    print("Mauvaise choix. Chances restantes : " + str(essais)) #Message montrant quele joueur a eu faux 
                    if essais == 0:
                        print("Désolé, vous avez perdu. Le mot était : " + mot_recherche) # Message de défaite
            else:
                print("Entrez une lettre valide.") # Demande au joueur de bine rentrer une unique lettre valide