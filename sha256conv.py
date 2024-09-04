import hashlib

texto = input("Introduce el texto a encriptar: ")

sha256 = hashlib.sha256()

sha256.update(texto.encode('utf-8'))

hash_encriptado = sha256.hexdigest()

print(f"Texto encriptado en SHA-256: {hash_encriptado}")