from tkinter import *

UseTkinter = True    # Défini le fait qu'on utilise l'interface Tkinter ou non

def Conver(x=0, c=32, tku=True):
    
    if tku is False:    # On vérifie l'état de la variable "tku" pour se servir ou non de l'interface
        x = input("Donnez un chiffre décimal --> ")
        try:
            c = int(input("\nEn combien de bits ? Dites 32 ou 64 -->"))
        except ValueError:
            c = 12
            pass
        while c != 32 and c != 64:
            print("\nRéponse invalide, veuillez réhitérer :\n")
            try:
                c = int(input("En combien de bits ? Dites 32 ou 64 -->"))
            except ValueError:
                c = 12
                pass

    try:    # On vérifie que x est inclu dans l'enssemble des réels.
        x = float(x)
    except ValueError:    # Sinon on le précise
        return "Il faut entrer un nombre ! Et rien d'autre !"

    print(x)
    if c == 32:    # Si la longueur est 32 bits
        w = 23
        y = 126
    else:          # Si la longueur est 64 bits
        w = 52
        y = 1022

    if x > 0 or x == 0:    #    On défini la partie du signe
        sign = "0"         #
    elif x < 0:            #
        sign = "1"         #

    def frac(x):    # On génère la partie fractionnée
        fract = ""
        y = x - int(x)
        y = abs(y)
        for i in range(w):
            y = y * 2
            if y >= 1:
                y -= 1
                fract += "1"
            else:
                fract += "0"
        return fract

    def exp(x):    # On génère la partie de l'exposant
        e = int(abs(x))
        expo = ""
        while e != 0:
            expo = str(e % 2) + expo
            e = e // 2
        return expo

    expo = exp(x)                         # On génère l'exposant sans le décalage
    expo2 = exp(len(expo) + y)            # On génère l'exposant avec le décalage
    fract = (expo[1:32] + frac(x))[:w]    # On génère la mantisse
    tot = sign + expo2 + fract            # On concatène tout

    return tot        # On renvoie la valeur finale

def Conv_32():        # On converti en 32 bits
    x = Conver(valeur.get())
    value.set(x)
    if len(x) != 44:
        root.clipboard_clear()
        root.clipboard_append(x)

def Conv_64():        # On converti en 64 bits
    x = Conver(valeur.get(), 64)
    value.set(x)
    if len(x) != 44:
        root.clipboard_clear()
        root.clipboard_append(x)

if UseTkinter is True:    # On créer l'interface

    root = Tk()
    root.config(bg="#006EB1")
    root.title("Conversion Binaire 32/64 bits")
    root.minsize(800, 512)
    root.geometry("1920x1080")
    root.iconbitmap("icologo.ico")

    center_frame = Frame(root, bg="#006EB1")

    Titre = Label(center_frame, text="Bienvenue", bg="#006EB1", fg="white", font=("Courrier", 55))
    Titre.pack()

    Sous_titre = Label(center_frame, text="Merci de rentrer un nombre :", fg="white", bg="#006EB1", font=("Courrier", 30))
    Sous_titre.pack()

    valeur = StringVar()
    champ = Entry(center_frame, textvariable=valeur, fg="white", bg="#006EB1", font=("Courrier", 25))
    champ.pack(fill=X, pady=25)
    champ.focus()

    value = StringVar()
    reponseLab = Label(center_frame, textvariable=value, bg="#006EB1", fg="white", font=("Courrier", 15))
    reponseLab.pack(pady=10)

    Bouton_32 = Button(center_frame, text="Convertir sous 32 bits", fg="white", bg="#006EB1", font=("Courrier", 25), command=Conv_32)
    Bouton_32.pack(side="left")

    Bouton_64 = Button(center_frame, text="Convertir sous 64 bits", fg="white", bg="#006EB1", font=("Courrier", 25), command=Conv_64)
    Bouton_64.pack(side="right")

    center_frame.pack(expand=YES)

    Quitte = Button(root, text="Quitter le convertisseur", fg="white", bg="#006EB1", font=("Courrier", 25), command=root.quit)
    Quitte.pack(side="bottom", pady=20)

    root.mainloop()
else:
    print(Conver(tku=False))
