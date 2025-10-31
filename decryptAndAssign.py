import hashlib
import base64

with open("signedCryptMessage.txt", "r", encoding="utf-8") as f:
    data = f.read()

start_tag = "---BEGIN HEADER---\n"
mid_tag = "\n---END HEADER---\n"

_, after_start = data.split(start_tag, 1)
signature, _, cipher_b64 = after_start.partition(mid_tag)
signature = signature.strip()
cipher_b64 = cipher_b64.strip()

key = input("Digite a chave para descriptografar: ")
key_bytes = key.encode('utf-8')

cipher_bytes = base64.b64decode(cipher_b64)

message_bytes = bytearray(len(cipher_bytes))
for i in range(len(cipher_bytes)):
    message_bytes[i] = cipher_bytes[i] ^ key_bytes[i % len(key_bytes)]

message = message_bytes.decode('utf-8')

actual_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()

if actual_hash == signature:
    print("\nAssinatura legítima!")
else:
    print("\nAssinatura não legítima!")

print("\nMensagem decodificada:", message)