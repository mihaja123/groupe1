import tkinter as tk
from authentification import auth


root = tk.Tk()
root.title("MANIA HOTEL")
root.geometry("1000x1000")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH,expand=True)

def clear_frame(window):
    for widget in window.winfo_children():
        widget.destroy()

def page_auth(window):
    clear_frame()
    new_window = auth(window)

label = tk.Label(frame,text="Mania",font=("Arial",17,"bold"),anchor="center")
label.place(x=420,y=300)

button = tk.Button(frame,text="Hôtel",font=("Arial",17,"bold"),bg="#2c8feb",anchor="center",relief="flat",command=page_auth)
button.place(x=500,y=295)




root.mainloop()