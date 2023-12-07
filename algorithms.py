import re

# Метод Цезаря
def caesar_cipher_rus(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
    alphabet_length = len(alphabet)

    for char in text.lower():
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % alphabet_length
            result += alphabet[new_index]
        else:
            result += char
    return result

# Метод многоалфавитной замены
def create_vigenere_table():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
    table = []
    for i in range(len(alphabet)):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table.append(shifted_alphabet)
    return table

def preprocess_text(text):
    # Удаление пробелов и знаков препинания из текста
    return re.sub(r'\W+', '', text).lower()

def vigenere_encrypt(text, key):
    text = preprocess_text(text)  # Очищаем текст перед шифрованием
    table = create_vigenere_table()
    key = ''.join(key[i % len(key)] for i in range(len(text))).lower()
    encrypted_text = ""

    for char, key_char in zip(text, key):
        if char in table[0]:
            row = table[0].index(key_char)
            col = table[0].index(char)
            encrypted_text += table[row][col]
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    encrypted_text = preprocess_text(encrypted_text)  # Очищаем текст перед дешифрованием
    table = create_vigenere_table()
    key = ''.join(key[i % len(key)] for i in range(len(encrypted_text))).lower()
    decrypted_text = ""

    for char, key_char in zip(encrypted_text, key):
        if char in table[0]:
            row = table[0].index(key_char)
            col = table[row].index(char)
            decrypted_text += table[0][col]
        else:
            decrypted_text += char

    return decrypted_text

def preprocess_text_for_block_permutation(text):
    text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace(' ', '_')
    return text.strip()

def get_key_order(key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя_"
    alphabet_dict = {letter: index for index, letter in enumerate(alphabet)}
    alphabet_indexes = [alphabet_dict[letter] for letter in key.lower()]
    order_dict = {alphabet_index: i for i, alphabet_index in enumerate(sorted(alphabet_indexes))}
    order = [order_dict[alphabet_index] for alphabet_index in alphabet_indexes]
    return order

# Метод блочной перестановки
def block_permutation_encrypt(text, key):
    text = preprocess_text_for_block_permutation(text)
    key_order = get_key_order(key)
    key_length = len(key)

    if len(text) % key_length != 0:
        text += '_' * (key_length - len(text) % key_length)

    encrypted_text = ''
    for i in range(0, len(text), key_length):
        block = text[i:i+key_length]
        encrypted_block = [''] * key_length
        for j in range(key_length):
            encrypted_block[key_order[j]] = block[j]
        encrypted_text += ''.join(encrypted_block)

    return encrypted_text

def block_permutation_decrypt(encrypted_text, key):
    encrypted_text = preprocess_text_for_block_permutation(encrypted_text)
    key_order = get_key_order(key)
    key_length = len(key)

    decrypted_text = ''
    for i in range(0, len(encrypted_text), key_length):
        block = encrypted_text[i:i+key_length]
        decrypted_block = [''] * key_length
        for j in range(key_length):
            decrypted_block[j] = block[key_order[j]]
        decrypted_text += ''.join(decrypted_block)

    return decrypted_text.strip('_')
