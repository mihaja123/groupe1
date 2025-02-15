import tkinter as tk
from tkinter import PhotoImage
from authentification import auth

def show_home(window):
    """ Affiche l'interface de la page d'accueil avec un menu latéral """
    for widget in window.winfo_children():
        widget.destroy()

    # --- Conteneur principal ---
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # --- Barre latérale ---
    sidebar = tk.Frame(main_frame, bg="#2c8feb", width=250)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    # --- Contenu principal ---
    content = tk.Frame(main_frame, bg="white")
    content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # --- Affichage du logo ---
    logo = PhotoImage(file="E:\exo groupe\mania hotel")  
    logo_label = tk.Label(sidebar, image=logo, bg="#2c8feb")
    logo_label.image = logo  # Pour éviter la suppression par le garbage collector
    logo_label.pack(pady=20)

    # --- Menu de navigation ---
    buttons = [
        ("Accueil & Statistiques", show_home),
        ("Gestion des Clients", lambda: show_page(content, "Clients")),
        ("Gestion des réservations", lambda: show_page(content, "Réservations")),
        ("Gestion des Chambres", lambda: show_page(content, "Chambres")),
        ("Gestion des Paiements", lambda: show_page(content, "Paiements")),
        ("Utilisateurs", lambda: show_page(content, "Utilisateurs")),
        ("Déconnexion", lambda: auth(window))  # Retour à la connexion
    ]

    for text, command in buttons:
        btn = tk.Button(sidebar, text=text, font=("Arial", 12), fg="white", bg="#1d6ec0", relief="flat", command=command)
        btn.pack(fill=tk.X, pady=2)

    # --- Contenu par défaut ---
    show_page(content, "Bienvenue")

def show_page(content, page_name):
    """ Met à jour le contenu principal avec le texte de la page sélectionnée """
    for widget in content.winfo_children():
        widget.destroy()

    tk.Label(content, text=f"Page : {page_name}", font=("Arial", 20), bg="white").pack(pady=20)
