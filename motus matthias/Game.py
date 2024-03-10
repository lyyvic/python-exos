"""
Header:
Classe qui gère le jeu "Motus"
Matthias Lapointe
18/12/2023
"""




from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random as r

class Game:
    def __init__(self):
        # Initialisation de la fenêtre et du jeu
        self.root = Tk()
        self.root.title('Motus')
        self.root.geometry("500x500")
        self.canva = Canvas(self.root, width=500, height=500, background='black',borderwidth=0, highlightthickness=0)
        self.quit_button = Button(self.root, text="Quitter", command=self.root.destroy)
        self.quit_button.place(relx=0.9, rely=0.05, anchor="e")
        self.Start = Button(self.root, text="Commencer une partie", command=self.startGame)
        self.Start.pack()
        """filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
        )
        # show the open file dialog
        f = filedialog.askopenfile(filetypes=filetypes)
        # read the text file and show its content on the Text
        print(f.readlines())"""
        self.words = ['banane', 'abolir', 'achats']
        self.ans = StringVar()
        self.guesses = []
        self.nbEssais = 1
        self.score = 0
        
    #Fonction qui choisit un mot et qui affiche le jeu
    def startGame(self):
        self.Start.destroy()
        self.champ = Entry(self.root, textvariable=self.ans)
        self.champ.focus_set()
        self.champ.pack()
        self.check = Button(self.root, text="Verif", command=self.check_word)
        self.check.pack()
        self.scoreLabel = Label(self.root, text="Votre Score: "+str(self.score), anchor="ne")
        self.scoreLabel.pack()
        self.word = self.words[r.randint(0,len(self.words)-1)]

        self.guess = Frame(self.root, borderwidth=2, relief="groove")
        texte = ""
        for t in self.word:
            if t == self.word[0]:
                texte += t+" "
            else :
                texte += "X "
        x = Label(self.guess,text=texte)
        self.guesses.append(x)
        x.pack()
        for i in range(6):
            x = Label(self.guess,text='X X X X X X')
            self.guesses.append(x)
            x.pack()
        self.guess.pack()


    #Fonction qui verifie si le mot entré est correct et l'utilise
    def check_word(self):
        self.currentWord = self.ans.get()
        if len(self.currentWord) == 6:
            texte = ""
            n = 0
            for i in self.currentWord:
                if i == self.word[n]:
                  texte += i+'g '
                if i in self.currentWord:
                    texte += i+'y '
                else:
                    texte += i+'r '
                    n += 1

                
            self.guesses[self.nbEssais].config(text=texte)
        else: 
            messagebox.showwarning('Error', "Le mot n'est pas correct \n Veuillez entrez un nouveau mot")