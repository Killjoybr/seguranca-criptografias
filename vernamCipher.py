import random;

text = input("Insira o texto p/ criptografar: \n");

key = ""
ciphertext = ""
plaintext = ""

# Gerando a chave p/ criptografia e descriptografia

for _ in range(len(text)):    
  random_char = chr(random.randint(0, 255))
  key += random_char

# operacao XOR em cada caractere criptografando

for i in range(len(text)):
  text_char = ord(text[i])
        
  key_char = ord(key[i])
        
  encrypted_char = text_char ^ key_char  # Operacao XOR
        
  ciphertext += chr(encrypted_char)

# operacao XOR descriptografando

for i in range(len(ciphertext)):
  ciphertext_char = ord(ciphertext[i])
        
  key_char = ord(key[i])
        
  decrypted_char = ciphertext_char ^ key_char  # Operacao XOR
        
  plaintext += chr(decrypted_char)

print(f"Cifra: {ciphertext}")
print(f"Texto descriptografado: {plaintext}")
