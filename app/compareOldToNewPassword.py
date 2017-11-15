import collections
from passlib.hash import sha256_crypt
# import sys

#old passwords are hashed new password is not
def compareToOldPasswords(oldPasswords, newPassword):
    for password in oldPasswords:
        if ( sha256_crypt.verify(newPassword, password) ):
            return True
    return False

def rootWord(newPassword):
    charList = []
    for chars in newPassword:
        if chars.isalpha():
            charList.append(chars)
    password = ''.join(charList)
    password.lower()
    return password



#def main():
def newPasswordToOldPasswordComparison(newPassword, oldPassword, oldPasswords):
#    oldPassword = sys.argv[1]
#    newPassword = sys.argv[2]
    newPassword = newPassword.lower()
    oldPassword = oldPassword.lower()
    newPasswordLetters = collections.Counter(newPassword)
    oldPasswordLetters = collections.Counter(oldPassword)
    intersection = newPasswordLetters & oldPasswordLetters
    root = rootWord(newPassword)
#    print intersection
    count = 0 
    for item in intersection:
        count = count + intersection[item]
    percent = float(count)/len(newPassword)
    print percent
    if (percent > .7):
#        print False
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

#if __name__ == "__main__":
#    main()
