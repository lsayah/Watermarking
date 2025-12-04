from PIL import Image
import numpy as np 



# IMPORT IMAGE
image = Image.open("C:/Users/Amazi/Downloads/image_steganographie.png")
#*************************************************************************************************************************************

text = "Il faut cultiver son jardin"

# TRANFORMATION IMAGE EN TABLEAU
image_array = np.array(image)
#*************************************************************************************************************************************


# IMAGE EN PAIR
def get_image_even(image_array):
    return image_array - image_array % 2 

# ici je vais rendre tout les pixel de l'image pair en supprimant 1 bit par pixel le LSB1
# je soustrait le modulo 2 de chaque pixel (donc 1 si impair ou 0 si pair) --> tableau de pixel totalement pair
# valeur entre 0 et 255 pour R, V et B  mais tous pair
#*************************************************************************************************************************************





# CONVERTIR TEXTE EN BINAIRE
def convert_text_to_binary(text):
    list_of_binary_ordinals = [bin(ord(char))[2:].zfill(21) for char in text]
    bits_str = "".join(list_of_binary_ordinals)
    list_of_bits = [int(bit) for bit in bits_str]
    return list_of_bits

# Fonction pour convertir le texte à cacher en binaire
# pour chaque lettre dans le texte je transfome en son code ascii que je retransforme en bianire je suprimme 0b (slicing) et je rajoute autant de 0 pour completr les 21 bit maximum pour un caractère ascii
# ensuite je concatene la liste transformer en binaire en préparer pour des pack de 21 bit en une chaine de caractère
# je transforme la chaine de caractère en liste  d'entier  (lié au concept muable(liste) immuable(chaine de caractère))
# je retourne la liste de bit => le texte sous forme de liste binaire chaque lettre en pack de 21 bit
#*************************************************************************************************************************************


# INSERTION DU MOT DANS L'IMAGE
def watermarking(image_array, text):
    number_rows, number_columns, number_canals= image_array.shape  
    even_array_image = get_image_even(image_array)
    binary_message = convert_text_to_binary(text)

    bit_index = 0 
    total_size_image = number_rows * number_columns * number_canals
    if len(binary_message) > total_size_image:
        print("Ecrit pas un roman le sang") 

    for row in range(0, number_rows):
        for col in range(0, number_columns):
            for canal in range(0, number_canals):
                if bit_index < len(binary_message):
                    even_array_image[row][col][canal] += binary_message[bit_index]  
                    bit_index += 1

    Image.fromarray(even_array_image).save('image_watermarked.png')              
    

watermarking(image_array, text)
print("Le message est bien caché dans image_watermarked.png") 
             
            #**************************************************       
                        # counter = 0
                     # list_of_bits[counter]
                #   counter += 1
                    #  if counter == len(list_of_bits):
                    #     break
            #**************************************************
    
    
# je prend l'image en tableau et le texte en binaire en parametre
# je recupère les coordonnées du tableau (image) et je les variabilise (peut etre pas le bon terme)
# je recupère l'image en pair et le texte en binaire (list de bit)
#  j'utilise un index pour parcourir le tableau
# j'utiliser rasterscan via les boucle imbriquer pour ajouter ou non 1 ou 0 bit a chaque valeur R V B de chaque pixel en fonction du bianary_message
    # problème rasterscan --> le message sera toujours en haut a guache de l'image ? (facilement identifiable)
# je retourne le tableau modifier quand l'index arrive au bout du texte
# je sauvegarde l'image





# def get_message_from_watermarking_image(image_array):
#     initial_binary_message = image_watermerked_array.flatten() % 2


            
        




