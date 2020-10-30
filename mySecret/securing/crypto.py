from cryptography.fernet import Fernet


def _encodeMessage(message):
    return message.encode()


def _decodeMessage(message):
    return message.decode()


def generateEncrypterAndDecrypter(key=None):
    '''return encryptMessage, decryptMessage functions '''
    if key is not None:
        key = _encodeMessage(key[2:])
    else:
        key = key if key else Fernet.generate_key()
    f = Fernet(key)

    def getKey():
        return key

    def encryptMessage(message):
        message = _encodeMessage(message)
        return f.encrypt(message)

    def decryptMessage(encryptedMessage):
        if isinstance(encryptedMessage, str):
            encryptedMessage = _encodeMessage(encryptedMessage[2:])
        encryptedMessage = f.decrypt(encryptedMessage)
        return _decodeMessage(encryptedMessage)

    return encryptMessage, decryptMessage, getKey
