import hashlib
import base64

with open("signedCryptMessage.txt", "r", encoding="utf-8") as f:
    data = f.read()

signature = data.split("---BEGIN HEADER---\n")[1].split("\n---END HEADER---")[0].strip()
cipher_b64 = data.split("---END HEADER---\n", 1)[1].strip()

key = input("Digite a chave para descriptografar: ")
keyBytes = key.encode('utf-8')

cipher_bytes = base64.b64decode(cipher_b64)

messageInBytes = bytearray(len(cipher_bytes))
for i in range(len(cipher_bytes)):
    messageInBytes[i] = cipher_bytes[i] ^ keyBytes[i % len(keyBytes)]

message = messageInBytes.decode('utf-8')

actualSignature = hashlib.sha256(message.encode('utf-8')).hexdigest()

if actualSignature == signature:
    print("\nAssinatura legítima!")
else:
    print("\nAssinatura não legítima!")

print("\nMensagem decodificada:", message)

content = f"---BEGIN HEADER---\n{actualSignature}\n---END HEADER---\n{message}"

with open("signedDecryptMessage.txt", "w", encoding="utf-8") as f:
    f.write(content)