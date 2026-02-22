import qrcode

def qr_generator(link,save):
    link = qrcode.make(link)
    type(link)
    link.save(save)

print("""                  
  █████   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▓  ██▒▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██▒  ██░▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░██  █▀ ░▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒███▒█▄ ░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ▒░  ░   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
   ░   ░   ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░       ░        ░  ░     ░  ░            ░ ░     ░     
                                                            

""")
while True:
    print("---- MENU ----")
    print("1.Create QR")
    print("2.Exit")

    op = input("Select Option: ")


    if op == "1":
        enlace = input("Paste your link: ")
        guardar = input("File name: ")
        archivo = guardar + ".png"
        qr_generator(enlace, archivo)
        print("Saved as",archivo)
    elif op == "2":
        break
    else:
        print("Invalid Option")




