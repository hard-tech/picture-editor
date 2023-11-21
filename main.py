from PIL import Image
import os

original_picture = './original_picture/'
modify_picture = './original_picture/'

def ls_original_pic():
    fichiers = os.listdir(original_picture)

    print(f'\nListe des fichier dans {original_picture} :')
    for fichier in fichiers:
        print(fichier)

def ls_modify_pic():
    fichiers = os.listdir(modify_picture)

    print(f'\nListe des fichier dans {modify_picture} : ')
    for fichier in fichiers:
        print(fichier)

# Storie 1 :
def convert_black_and_white():
    # Demmander à l'utilisateur le nom de l'image à modifier
    image_nom = input('\nQuelle est le nom de vôtre image ? : ')

    try:
        # Charger l'image
        image = Image.open(f'./original_picture/{image_nom}')

        # Convertire l'image en Noir & Blanc
        image_noir_et_blanc = image.convert('L')
        # image_noir_et_blanc.show()

        # Sauvegarder l'image dans ./modify_picture
        image_noir_et_blanc.save(f'./modify_picture/{image_nom}')
        
        # Retourner à l'utilisateur l'états de l'action (si err la retourné)
        print("\nL'image a bien été transformé. \n")
        ls_modify_pic()
    except:
        print("nous n'avons pas pu ouverire le fichier (nom d'image incorrect).")
        ls_original_pic()
        print('\n')

convert_black_and_white()