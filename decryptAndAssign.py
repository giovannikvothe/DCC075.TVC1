import hashlib

with open("cryptMessage.txt", "r") as f:
    cryptMessage = f.read()

with open("assignature.txt", "r") as f:
    originalAssignature = f.read()

key = input("Digite a chave: ")

message = ""
for i in range(len(cryptMessage)):
    message += chr(ord(cryptMessage[i]) ^ ord(key[i % len(key)]))

actualAssignature = hashlib.sha256(message.encode()).hexdigest()

print("\nMensagem decodificada: ", message)