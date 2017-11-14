def hasCapital(password):
    for i in password:
        if( i.isupper() ):
            return True
    return False
        
def hasNumeric(password):
    for index, c in enumerate(password):
    	if c.isdigit():
    		return True
    return False

def hasLowercase(password):
    for i in password:
        if( i.islower() ):
            return True
    return False

def hasSpecial(password):
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        index = password.find(specialChar)
        if index != -1:
        	return True
    return False

def correctLength(password, passwordLength):
    if (int(passwordLength) > int(len(password))):
    	return False
    else:
        return True

def checkPasswordWithCompanySettings(settings, password):
   password = settings[]
   #whenever a requirement is not met return false
   if not (correctLength(password, settings[0])):
       return False
   if ( settings[1] ):
       if not( hasCapital(password) ):
           return False
   if ( settings[2] ):
       if not( hasLowercase(password) ):
           return False
   if ( settings[3] ):
       if not ( hasNumeric(password) ):
           return False
   if ( settings[4] ):
       if not ( hasSpecial(password) ):
           return False
   return True	

