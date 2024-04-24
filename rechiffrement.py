import os

def string_to_binary(message):
    """ Convertit un message string en une chaîne de bits. """
    return ''.join(format(ord(char), '08b') for char in message)

def generate_binary_key(length):
    """ Génère une clé binaire aléatoire de la longueur spécifiée. """
    return ''.join(str(os.getrandom(1)[0] % 2) for _ in range(length))

def xor_binary_data(data, key):
    """ Applique XOR entre les données binaires et la clé binaire. """
    return ''.join(str(int(data[i]) ^ int(key[i])) for i in range(len(data)))

# Conversion du message en binaire
message_text = "Bonjour, monde!"
message_binary = string_to_binary(message_text)

# Générer une clé binaire aléatoire de la même taille que le message
key_binary = generate_binary_key(len(message_binary))

# Chiffrement
encrypted_binary = xor_binary_data(message_binary, key_binary)
print("Encrypted Binary:", encrypted_binary)
print("Binary Key:", key_binary)
