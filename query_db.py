from sqlalchemy import create_engine

from test import api


# ToDo Frontend communicator to redirect when multiple pages are possible
frontend = frontend.javascript()
# Function to query database for existence of company and return appropriate settings and page, return -1 and error
# if user is not admin and company doesn't exist.
def getcompanysettings(company, isadmin):
    # Query database for company, return boolean value
    api.resource(Users,'/users')

    companyquery = connection.execute("Database_has_company", company)
    settings = -1
    # Load password settings admin page and current settings, to adjust password requirements
    if isadmin and companyquery:
        settings = connection.execute("Load_company_settings")
        frontend.loadpage("Admin_settings")
    # Load password settings admin page and create new company in db, to adjust password requirements
    elif isadmin and not companyquery:
        connection.execute("Create_new_company", company)
        frontend.loadpage("Admin_settings")
    # Load password settings user page and current settings, to change/check password
    elif not isadmin and companyquery:
        settings = connection.execute("Load_company_settings")
        frontend.loadpage("user_settings/user_password_change")
    return settings

def getusersettings(username):
    settings = connection.execute("load_user_settings", username)
    return settings

def signin (username, password, check):
    if check:

        signin = connection.execute("is_valid", username, password)

    else:
        signin
    return signin

def changepassword(username, oldpassword):
    signin