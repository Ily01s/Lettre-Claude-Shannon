# main.py

import correction_err
import decryptage
import rechiffrement
import compression
import hamming_codec

def main():
    # Étape 1: Lire le message codé et corriger les erreurs
    encoded_message_path = './lettre.txt'
    bytes_entree = correction_err.lire_et_preparer_fichier(encoded_message_path)
    corrected_binary = correction_err.appliquer_correction(bytes_entree)
    corrected_binary= correction_err.extraire_donnees_utiles(corrected_binary)
    text_output = decryptage.binary_to_text(corrected_binary)
    decrypted_text = decryptage.decrypt_vigenere(text_output, 'PYTHON')  # Remplacez 'SNAKE' par la clé réelle
    print(text_output)
    print("___________________________________________________________________________")
    print(decrypted_text)
    

if __name__ == '__main__':
    main()
