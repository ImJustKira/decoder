import base64
from colorama import init
from colorama.ansi import Fore
init()

def logo ():
    print ( Fore.CYAN + "╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮")
    print ("╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃")
    print ("╱┃┃┃┣━━┳━━┳━━┳━╯┣━━┳━╮")
    print ("╱┃┃┃┃┃━┫╭━┫╭╮┃╭╮┃┃━┫╭╯")
    print ("╭╯╰╯┃┃━┫╰━┫╰╯┃╰╯┃┃━┫┃by kira")
    print ("╰━━━┻━━┻━━┻━━┻━━┻━━┻╯")

def stringcode ():
    jajant = input("deme el archivo a codificar")
    ver2 = jajant.encode('utf-8')
    ver3 = base64.b64encode(ver2)
    print (ver3)
    menu()
    

    


def menu ():
    print (Fore.BLUE+"precione a para codificar un texto en b64")
    print ("b para decodificar uno ")
    eleccion = input("que elige?")
    if eleccion == "a":
        stringcode()
    if eleccion == "b":
        stringdecode()




def stringdecode ():
    ekisde = input ("deme el archivo a decodificar")
    nose = ekisde.encode("utf-8")
    miheart = base64.b64decode(nose)
    print (miheart)
    menu ()

logo ()
menu ()
