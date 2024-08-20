import string;
import random;

chars = " " + string.digits + string.punctuation + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)

plainText = input("Escreva a mensagem p/ ser criptografada: \n")
cipherText = ""


# Processo de criptografia:

for letter in plainText:
    index = chars.index(letter)
    cipherText += key[index]

print(f"Criptografada: {cipherText}")

plainText = ""

# Processo de descriptografia:

for letter in cipherText:
    index = key.index(letter)
    plainText += chars[index]

print(f"Descriptografada: {plainText}")