from random import randint

phrase = "I love didgeridoos"

def convertPhraseToBinary(phrase):
    binaryPhrase = ""
    for i in phrase:
        binaryPhrase += str(convertToBinary(ord(i)))
    return binaryPhrase

def convertToBinary(number):
    binaryNumber = ""
    while number > 0:
        binaryNumber = str((number % 2)) + binaryNumber
        number = number // 2
    while len(binaryNumber) < 7:
        binaryNumber = "0" + binaryNumber
    return binaryNumber

def generateKey(keyLength):
    key = ""
    for i in range(0,keyLength):
        key += str(randint(0,1))
    return key

def encrypt(binaryPhrase,key):
    encryptedMessage = ""
    for i in range(0,len(binaryPhrase)):
        if binaryPhrase[i] != key[i]:
            encryptedMessage += "1"
        else:
            encryptedMessage += "0"
    return encryptedMessage

binaryPhrase = convertPhraseToBinary(phrase)
key = generateKey(len(binaryPhrase))
encryptedMessage = encrypt(binaryPhrase,key)
print(binaryPhrase)
print(key)
print(encryptedMessage)    
