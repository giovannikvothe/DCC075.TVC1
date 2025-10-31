import hashlib
import base64

message = input("Digite a mensagem a ser criptografada: ")
key = input("Digite a chave secreta: ")

message_bytes = message.encode('utf-8')
key_bytes = key.encode('utf-8')

hash_value = hashlib.sha256(message_bytes).hexdigest()

cipher = bytearray(len(message_bytes))
for i in range(len(message_bytes)):
    cipher[i] = message_bytes[i] ^ key_bytes[i % len(key_bytes)]

cipher_b64 = base64.b64encode(bytes(cipher)).decode('ascii')

content = f"---BEGIN HEADER---\n{hash_value}\n---END HEADER---\n{cipher_b64}"

with open("signedCryptMessage.txt", "w", encoding="utf-8") as f:
    f.write(content)