import hashlib

message = input("Digite a mensagem a ser criptografada: ")
key = input("Digite a chave secreta: ")

assignature = hashlib.sha256(message.encode()).hexdigest()

cryptMessage = ""
for i in range(len(message)):
    cryptMessage += chr(ord(message[i]) ^ ord(key[i % len(key)]))

with open("cryptMessage.txt", "w") as f:
    f.write(cryptMessage)

with open("assignature.txt", "w") as f:
    f.write(assignature)