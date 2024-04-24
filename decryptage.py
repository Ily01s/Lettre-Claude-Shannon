#decryptage.py

def decrypt_vigenere(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    decrypted_text = []
    key_index = 0
    
    for char in ciphertext:
        # Assurez-vous que le caractère est dans l'alphabet avant de continuer
        if char.upper() in alphabet:
            alpha_index = alphabet.index(char.upper())
            key_char = key[key_index % len(key)]
            key_char_index = alphabet.index(key_char)
            
            # Calcul du nouvel index après décalage
            new_index = (alpha_index - key_char_index + 26) % 26
            decrypted_char = alphabet[new_index] if char.isupper() else alphabet[new_index].lower()
            
            decrypted_text.append(decrypted_char)
            key_index += 1  # Incrémenter key_index uniquement pour les lettres
        else:
            decrypted_text.append(char)  # Ajouter les non-lettres inchangées

    return ''.join(decrypted_text)




def binary_to_text(binary_list):
    text = ''
    # Convertir la liste d'entiers en chaîne de caractères binaires
    binary_str = ''.join(str(bit) for bit in binary_list)
    # Convertir chaque octet en caractère
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:  # Assurer qu'il s'agit d'un octet complet
            text += chr(int(byte, 2))  # Convertir le binaire en ASCII
    return text


