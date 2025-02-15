import tkinter as tk
from tkinter import messagebox
import mysql.connector



def verifier_login(email, password):
    """ Vérifie les identifiants dans la base de données MySQL. """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="", 
        database="mania_hotel"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = %s AND mot_de_passe = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    print(user)

    cursor.close()
    conn.close()

    return user is not None

def login(window, email_entry, password_entry):
    """ Vérifie les identifiants et affiche un message. """
    email = email_entry.get()
    password = password_entry.get()

    if verifier_login(email, password):
        from accueil import show_home
        messagebox.showinfo("Succès", "Connexion réussie !")
    else:
        messagebox.showerror("Erreur", "Identifiants incorrects")

def auth(window):
    # Effacer le contenu précédent
    for widget in window.winfo_children():
        widget.destroy()


    # Ajouter les widgets de l'authentification
    tk.Label(window, text="Connexion", font=("Arial", 20)).pack(pady=100)

    tk.Label(window, text="Email:",font=("Arial",12)).place(x=280,y=230)
    email_entry = tk.Entry(window,width=25,font=("Arial",12))
    email_entry.place(x=400,y=230)

    tk.Label(window, text="Mot de passe:",font=("Arial",12)).place(x=280,y=290)
    password_entry = tk.Entry(window, show="*",width=25,font=("Arial",12))
    password_entry.place(x=400,y=290)

    tk.Button(window, text="Se connecter",font=("Arial",12),bg="#2c8feb",fg="white",relief="flat",command=lambda: login(window, email_entry, password_entry)).pack(pady=150)
