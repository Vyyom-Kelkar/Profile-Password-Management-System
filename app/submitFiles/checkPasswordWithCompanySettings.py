# This file creates the functions for checking if passwords meet the comapny requirements
# Vyyom Kelkar, Brett Boehmer, Dakota Duncan

# Function to check if the password has a capital letter
def hasCapital(password):
    for i in password:
        if( i.isupper() ):
            return True
    return False
 
# Function to check if the password has a numeric character       
def hasNumeric(password):
    for index, c in enumerate(password):
    	if c.isdigit():
    		return True
    return False

# Function to check if the password has a lowercase letter
def hasLowercase(password):
    for i in password:
        if( i.islower() ):
            return True
    return False

# Function to check if the password has a special character
def hasSpecial(password):
    specialCharsList = ["!", "@", "#", "$", "%", "?", "&"]
    for specialChar in specialCharsList:
        index = password.find(specialChar)
        if index != -1:
        	return True
    return False

# Function to check if the password has the required length
def correctLength(password, passwordLength):
    if (int(passwordLength) > int(len(password))):
    	return False
    else:
        return True

# Function to check if the password meets all requirements
def checkPasswordWithCompanySettings(settings, password):
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

