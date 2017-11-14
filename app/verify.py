from passlib.hash import sha256_crypt

def verifyPassword(oldPasswords, newPassword){
	for password in oldPasswords:
        if (sha256_crypt.verify(newPassword, password)):
            return True
    return False
}