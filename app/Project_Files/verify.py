from passlib.hash import sha256_crypt

def verifyPassword(oldPassword, newPassword):
    if (sha256_crypt.verify(newPassword, oldPassword)):
        return True
    return False
