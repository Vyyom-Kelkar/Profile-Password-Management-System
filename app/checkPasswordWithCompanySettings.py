import datetime, timedelta
now = datetime.today()


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

def isExpired(password, daysUntilExpiration, passwordLastSet):
    datetimeDifference = now - timedelta(days = daysUntilExpiration)
    if datetimeDifference < passwordLastSet:
        return False
    return True 


def correctLength(password, passwordLength):
    if passwordLength > len(password):
    	return False
    else:
        return True

def checkPasswordWithCompanySettings(passwordLength, reqCap, reqLower, reqSpecial, reqNumeric, daysUntilExpiration, passwordLastSet, password):
   returnValue = True
   #whenever a requirement is not met return false
   if not(correctLength(password, passwordLength)):
       return False
   if not(isExpired(password, daysUntilExpiration, passwordLastSet)):
       return False
   if ( reqCap ):
       if not ( hasCapital(password) ):	
           return False
   if ( reqLower ):
       if not ( hasLowercase ):
           return False
   if ( reqNumeric ):
       if not ( hasNumeric ):
           return False
   if ( reqSpecial ):
       if not ( hasSpecial ):
           return False
   return True	

