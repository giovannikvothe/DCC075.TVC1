import hashlib
import base64

message = input("Digite a mensagem a ser criptografada: ")
key = input("Digite a chave secreta: ")

messageBytes = message.encode('utf-8')
keyBytes = key.encode('utf-8')

hash_value = hashlib.sha256(messageBytes).hexdigest()

cipher = bytearray(len(messageBytes))
for i in range(len(messageBytes)):
    cipher[i] = messageBytes[i] ^ keyBytes[i % len(keyBytes)]

cipher_b64 = base64.b64encode(bytes(cipher)).decode('ascii')

content = f"---BEGIN HEADER---\n{hash_value}\n---END HEADER---\n{cipher_b64}"

with open("signedCryptMessage.txt", "w", encoding="utf-8") as f:
    f.write(content)