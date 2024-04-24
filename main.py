# main.py

import correction_err
import decryptage
import rechiffrement
import compression


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
    decrypted_text_bin= rechiffrement.string_to_binary(decrypted_text)
    key_binary = rechiffrement.generate_binary_key(len(decrypted_text_bin))
    # Chiffrement
    encrypted_binary = rechiffrement.xor_binary_data(decrypted_text_bin, key_binary)
    print("Encrypted Binary:", encrypted_binary)
    print("Binary Key:", key_binary)
    #Compresser le message chiffré
    byte_data = compression.binary_string_to_bytes(encrypted_binary)
    compressed_data, huffman_codes = compression.compress_data(byte_data)
    print("Compressed Data:", compressed_data)

if __name__ == '__main__':
    main()
