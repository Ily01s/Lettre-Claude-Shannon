import heapq
from collections import Counter, defaultdict


def binary_string_to_bytes(binary_string):
    """ Convertit une chaîne binaire en objet bytes. """
    # Assurez-vous que la longueur de la chaîne binaire est un multiple de 8
    if len(binary_string) % 8 != 0:
        # Ajoutez des zéros à gauche si nécessaire pour compléter le dernier byte
        binary_string = binary_string.zfill(len(binary_string) + 8 - (len(binary_string) % 8))
    
    return bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

def calculate_frequencies(data):
    """ Calcule les fréquences de chaque caractère dans les données. """
    return Counter(data)


def build_huffman_tree(frequencies):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def get_huffman_codes(tree):
    """ Retourne un dictionnaire des codes Huffman pour chaque symbole. """
    return {symbol: code for symbol, code in tree}

def encode_data(data, codes):
    return ''.join(codes[byte] for byte in data)


def huffman_encoding(data, huffman_tree):
    """ Encodage du message en utilisant l'arbre de Huffman. """
    huffman_code = {symbol: code for symbol, code in huffman_tree}
    return ''.join(huffman_code[char] for char in data)

def compress_data(data):
    frequencies = calculate_frequencies(data)
    huffman_tree = build_huffman_tree(frequencies)
    codes = get_huffman_codes(huffman_tree)
    encoded_data = encode_data(data, codes)
    return encoded_data, codes 