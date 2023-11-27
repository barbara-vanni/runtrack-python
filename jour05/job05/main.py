def chiffrement(acrypter, decalage):
    message_crypte = ""
    for char in acrypter:
        if char != ' ':  
            asc = ord(char) + decalage
            message_crypte += chr((asc - 97) % 26 + 97)
        else:
            message_crypte += char 
    return message_crypte

acrypter = input("Votre message : ")
decalage = int(input("Décalage de combien de lettres ? "))
MessageCrypte = chiffrement(acrypter, decalage)
print("Message chiffré :", MessageCrypte)