from passlib.hash import sha256_crypt
import sys


def incrementNumber(newPassword, startAtFront):
    passwordRet = []
    if not (startAtFront):
        newPassword = newPassword[::-1]
    for index, c in enumerate(newPassword):
        if c.isdigit():
            indexNext = index + 1
            num = int(c)
            num = num + 1
            generatedPassword = newPassword[:index] + str(num) + newPassword[indexNext:]
            if not(startAtFront):
                generatedPassword = generatedPassword[::-1]
            passwordRet.append(generatedPassword)
            break
    return passwordRet

def decrementNumber(newPassword, startAtFront):
    passwordRet = []
    if not(startAtFront):
        newPassword = newPassword[::-1]
    for index, c in enumerate(newPassword):
        if c.isdigit():
            indexNext = index + 1
            num = int(c)
            num = num - 1
            generatedPassword = newPassword[:index] + str(num) + newPassword[indexNext:]
            if not(startAtFront):
                generatedPassword = generatedPassword[::-1]
            passwordRet.append(generatedPassword)
            break
    return passwordRet

#old passwords are hashed new password is not
def compareToOldPasswords(oldPasswords, newPassword):
    for password in oldPasswords:
        if ( sha256_crypt.verify(newPassword, str(password)) ):
            return True
    return False

def allPossibleNumberChanges(newPassword, startAtFront, numMaxCheck):
    passwordRet = []
    numCount = 0;
    if not(startAtFront):
        newPassword = newPassword[::-1]
    for index, c in enumerate(newPassword):
        if c.isdigit():
            numCount += 1
            if (numCount > numMaxCheck):
                break
            indexNext = index + 1
            for num in range(10):
                generatedPassword = newPassword[:index] + str(num) + newPassword[indexNext:]
                if not (startAtFront):
                    generatedPassword = generatedPassword[::-1]
                passwordRet.append(generatedPassword)
    return passwordRet

def rotationRight(newPassword, rotationFactor):
    passwordRet = []
    rotationFactor += 1
    for num in range(1, rotationFactor):
        password = newPassword[num:] + newPassword[:num]
        passwordRet.append(password)
    return passwordRet

def rotationLeft(newPassword, rotationFactor):
    passwordRet = []
    reversePass = newPassword[::-1]
    rotationFactor+=1
    for num in range(1, rotationFactor):
        temp = reversePass[num:] + reversePass[:num]
        password = temp[::-1]
        passwordRet.append(password)
    return passwordRet

def duplicateFront(newPassword):
    passwordRet =[]
    firstLetterDuplicate = newPassword[:1] + newPassword[:1] + newPassword[1:]
    passwordRet.append(firstLetterDuplicate)
    return passwordRet

def duplicateBack(newPassword):
    passwordRet = []
    lastLetterDuplicate = newPassword[:-1] + newPassword[-1:] + newPassword[-1:]
    passwordRet.append(lastLetterDuplicate)
    return passwordRet

def deleteFront(newPassword):
    passwordRet = []
    password = newPassword[1:]
    passwordRet.append(password)
    return passwordRet

def deleteBack(newPassword):
    passwordRet = []
    password = newPassword[:-1]
    passwordRet.append(password) 
    return passwordRet

def addSpecialCharacterToEnd(newPassword):
    passwordRet = []
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        password = newPassword + specialChar
        passwordRet.append(password)
    return passwordRet

def deleteLastSpecialChar(newPassword):
    passwordRet = []
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        index = newPassword.rfind(specialChar)
        if (index != -1):
            spliceStart = index
            spliceEnd = index + 1
            password = newPassword[:index] + newPassword[spliceEnd:]
            passwordRet.append(password)
            break
    return passwordRet

def addSpecialCharacterToFront(newPassword):
    passwordRet = []
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        password = specialChar + newPassword
        passwordRet.append(password)
    return passwordRet

def deleteFirstSpecialChar(newPassword):
    passwordRet = []
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        index = newPassword.find(specialChar)
        if (index != -1):
            spliceStart = index
            spliceEnd = index + 1
            password = newPassword[:index] + newPassword[spliceEnd:]
            passwordRet.append(password)
            break
    return passwordRet

def rootWord(newPassword):
    passwordRet = []
    charList = []
    for chars in newPassword:
        if chars.isalpha():
            charList.append(chars)
    password = ''.join(charList)
    password.lower()
    passwordRet.append(password)
    return passwordRet

def capitalizeALetter(newPassword, startAtFront, letters):
    passwordRet = []
    if not startAtFront:
        newPassword = newPassword[::-1]
    for index in range(letters):
        capitalized = newPassword[index].upper()
        nextIndex = index + 1
        tempPassword = newPassword[:index].lower() + capitalized + newPassword[nextIndex:].lower()
        passwordRet.append( tempPassword )
    return passwordRet

def lowercaseALetter(newPassword, startAtFront, letters):
    passwordRet = []
    if not startAtFront:
        newPassword = newPassword[::-1]
    for index in range(letters):
        capitalized = newPassword[index].lower()
        nextIndex = index + 1
        tempPassword = newPassword[:index].upper() + capitalized + newPassword[nextIndex:].upper()
        passwordRet.append( tempPassword )
    return passwordRet

#Main
def similar(newPassword, oldPasswords):

#set old passwords to input
    similarityDifficulty = 4
    numMaxCheck = 0
    generatedPasswords = []

    #process input args
    root = (rootWord(newPassword)) 
        

    if(similarityDifficulty == 4):
        numMaxCheck = 12
        generatedPasswords.append( (newPassword) )
        generatedPasswords.append( (root ) )
        generatedPasswords.extend( duplicateFront(newPassword))
        generatedPasswords.extend( deleteFirstSpecialChar(newPassword))
        generatedPasswords.extend( addSpecialCharacterToFront(newPassword))
        generatedPasswords.extend( deleteLastSpecialChar(newPassword))
        generatedPasswords.extend( addSpecialCharacterToEnd(newPassword))
        generatedPasswords.extend( deleteBack(newPassword))
        generatedPasswords.extend( deleteFront(newPassword))
        generatedPasswords.extend( duplicateBack(newPassword))
        generatedPasswords.extend( duplicateFront(newPassword))
        generatedPasswords.extend( rotationLeft(newPassword, 5))
        generatedPasswords.extend( rotationRight(newPassword, 5))
        generatedPasswords.extend( allPossibleNumberChanges(newPassword, True, numMaxCheck))
        generatedPasswords.extend( capitalizeALetter(newPassword, True, 5))
        generatedPasswords.extend( lowercaseALetter(newPassword, True, 5))
    elif (similarityDifficulty == 3):
        print "go"

    elif (similarityDifficulty == 2):
        print "cool"

    else: #must be (similarityDifficulty == 1):
        print "wow"
    print generatedPasswords
    for password in generatedPasswords:
        if (compareToOldPasswords(oldPasswords, str(password))):
            return [False, "Too similar", root]
    hashedNewPassword = sha256_crypt.using(rounds=1100).hash(newPassword)
    hashedRootWord = sha256_crypt.using(rounds=1100).using().hash(root)
    #print (True, hashedNewPassword, hashedRootWord, NewPassword, hashedRootWord)
    return [True, hashedNewPassword, hashedRootWord]
