import qrcode
import customtkinter as ctk
import pyperclip

def qr_generator(link, save):
    link = qrcode.make(link)
    link.save(save)

def close():
    exit()
    
def pegar():
    entrada_link.delete(0, "end")
    entrada_link.insert(0, app.clipboard_get())


def generar():
    enlace = entrada_link.get()
    nombre = entrada_nombre.get()

    if enlace == "" or nombre == "":
        label_estado.configure(text="fill in the fields",font=fuente, text_color="red")
        return

    archivo = nombre + ".png"
    qr_generator(enlace, archivo)
    label_estado.configure(text=f"Saved as {archivo}",font=fuente, text_color="green")

# --- Interfaz ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("QReator by arepa")
app.geometry("400x300")
app.resizable(False, False)

fuente = ctk.CTkFont(family="Arial", size=15)
ctk.CTkLabel(app, text="QReator", font=fuente, text_color="white").pack(pady=10)

entrada_link = ctk.CTkEntry(app, width=300,font=fuente, placeholder_text="Paste your link")
entrada_link.pack(pady=10)

entrada_nombre = ctk.CTkEntry(app, width=300,font=fuente, placeholder_text="File Name")
entrada_nombre.pack(pady=10)

ctk.CTkButton(app, text="Create QR", font=fuente, width=200, command=generar).pack(pady=20)

ctk.CTkButton(app, text="Exit", font=fuente, width=200, command=close).pack(pady=2)

label_estado = ctk.CTkLabel(app, text="")
label_estado.pack()

app.mainloop()