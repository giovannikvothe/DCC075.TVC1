Alunos:
    Giovanni Almeida Dutra - 202465035AC
    Guilherme Roldão dos Reis Pimenta - 202435001

Criptografia

1) O usuário digita uma mensagem e uma chave secreta.

2) A mensagem é convertida para bytes (utf-8) e XOR é aplicado com a chave repetida.

3) Um hash SHA-256 da mensagem original é gerado como assinatura.

4) O resultado XOR é codificado em Base64.

5) Tudo é salvo em signedCryptMessage.txt com o formato

---BEGIN HEADER---
<assinatura>
---END HEADER---
<mensagem criptografada em Base64>


Descriptografia

 1) O programa lê signedCryptMessage.txt, separando a assinatura e a mensagem criptografada.

2) O usuário fornece a chave para descriptografar.

3) O programa converte a mensagem de caracteres para bytes

4) Aplica XOR novamente para recuperar os bytes originais da mensagem.

5) Converte os bytes de volta para texto (utf-8).

6) Calcula o hash da mensagem decodificada e compara com a assinatura. Caso sejam iguais, a assinatura é legítima

7) Cria um novo arquivo signedDecryptMessage.txt contendo a mensagem decodificada e sua assinatura, seguindo o mesmo formato do arquivo anterior