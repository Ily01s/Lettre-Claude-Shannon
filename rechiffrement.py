# main.py

import correction_err
import decryptage
import rechiffrement
import compression

def main():
    # Étape 1: Lire le message codé et corriger les erreurs
    corrected_message = correction_err('./lettre.txt')
    
    # Étape 2: Décrypter le message corrigé
    decrypted_message = decryptage.decrypt_message(corrected_message)
    
    # Étape 3: Rechiffrer le message décrypté
    reencrypted_message = rechiffrement.reencrypt_message(decrypted_message)
    
    # Étape 4: Compresser le message rechiffré
    compressed_message = compression.compress_message(reencrypted_message)
    
    # Étape 5: Enregistrer ou afficher le résultat final
    print("Message final:", compressed_message)

if __name__ == '__main__':
    main()
