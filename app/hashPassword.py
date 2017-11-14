from passlib.hash import sha256_crypt

def hashPassword(password):
    hashedPassword = sha256_crypt.using(rounds = 1100).hash(password)
    return hashedPassword