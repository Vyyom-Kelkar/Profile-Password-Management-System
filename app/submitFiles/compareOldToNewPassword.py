# This file creates the functions for the comparison of passwords
# Jacob Shoaf, Yaman Alslaiti

import collections
from passlib.hash import sha256_crypt

#old passwords are hashed, new password is not
def compareToOldPasswords(oldPasswords, newPassword):
    print oldPasswords
    print newPassword
    for password in oldPasswords:
        if ( sha256_crypt.verify(newPassword, str(password)) ):
            return True
    return False

# extract the "root" word in the password
def rootWord(newPassword):
    charList = []
    for chars in newPassword:
        if chars.isalpha():
            charList.append(chars)
    password = ''.join(charList)
    password.lower()
    return password

# compare new password to old and current passwords
def newPasswordToOldPasswordComparison(newPassword, oldPassword, oldPasswords):
    newPassword = newPassword.lower()
    oldPassword = oldPassword.lower()
    newPasswordLetters = collections.Counter(newPassword)
    oldPasswordLetters = collections.Counter(oldPassword)
    intersection = newPasswordLetters & oldPasswordLetters
    root = rootWord(newPassword)
    count = 0 
    for item in intersection:
        count = count + intersection[item]
    percent = float(count)/len(newPassword)
    print percent
    if (percent > .7):
        return [False, "Too similar", root]
    else:
        newPassword = str(newPassword)
        if (compareToOldPasswords(oldPasswords, newPassword)):
            return [False, "Too similar", root]
        if (compareToOldPasswords(oldPasswords, root)):
            return [False, "Too similar", root]
        hashedNewPassword = sha256_crypt.using(rounds=1100).hash(newPassword)
        hashedRootWord = sha256_crypt.using(rounds=1100).using().hash(root)
        return [True, hashedNewPassword, hashedRootWord]
