def hasCapital(password):
    temp = password.upper()
    if temp == password:
    	return True
    else:
    	return False

def hasNumeric(password):
    for index, c in enumerate(password):
    	if c.isdigit():
    		return True
    return False

def hasLowercase(password):
    temp = password.lower()
    if temp == password:
    	return True
    else:
    	return False

def hasSpecial(password):
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        index = password.find(specialChar)
        if index != -1:
        	return True
    return False

def correctLength(password, passwordLength):
    if passwordLength > len(password):
    	return False
    else:
        return True

def checkPasswordWithCompanySettings(settings, password):
   returnValue = True
   #whenever a requirement is not met return false
   if (correctLength(password, settings[0])):
       return False
   if ( settings[1] ):
       if not ( hasCapital(password) ):	
           return False
   if ( settings[2] ):
       if not ( hasLowercase ):
           return False
   if ( settings[3] ):
       if not ( hasNumeric ):
           return False
   if ( settings[4] ):
       if not ( hasSpecial ):
           return False
   return True	

