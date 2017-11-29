# This file handles the tokens for forgotten passwords and sets up the email server
# Arthur Nyoni

import re
import uuid
import base64
from datetime import datetime
#from sqlalchemy import update
#from app.models import User, engine, mysession

# Gmail username and password for email smptp client
USERNAME = ""
PASSWORD = ""
BASE_URL ="http://localhost:5000/"

class ResetTokenGenerator:
    """
    Generates and checks tokens for password reset
    """
    def make_token(self, user_email):

        # Create a base64 encoded UUID for a token then remove any characters unfit for a url
        pre_token = base64.b64encode(uuid.uuid4().bytes).decode('utf-8')
        pre_token = re.sub(r'[\=\+\/]', lambda m: {'+': '-', '/': '_', '=': ''}[m.group(0)], pre_token)
        token = pre_token + str(datetime.now().strftime('%H:%M:%S'))

        #self.send_token(user_email,token)

        return token


    # def send_token(user_email,token):
    #     token_to_db = update(User).where(User.email == user_email).values(token=token)
    #    engine.execute(token_to_db)


    # def remove_token(user_email,token):
    #    token_death = update(User).where(User.email == user_email).values(token="")
    #    engine.execute(token_death)

    def check_token(self, user_email, token):
            # Retrieve db token for given usermail
            # token_list = mysession.query(User).filter_by(user_email=user_email).all()
            # token_db = token_list[0]

            # Compare user token to db token
            # token_match = token is token_db

            # Check life of token, if more than 3 hours deny and remove
            token_birth = str(token)[-8:]
            token_birth = datetime.strptime(token_birth,'%H:%M:%S')
            birth = datetime.combine(datetime.today(),token_birth)
            time_now = datetime.today().time().strftime('%H:%M:%S')
            time_elapsed = datetime.combine(datetime.today(),time_now)
            age = time_elapsed-birth

            # Catch cases
            if age >3:
                self.remove_token(user_email,token)
                return False
            # if not token_match:
            #    return False


            return True


#Set up SMTP server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
tokenator = ResetTokenGenerator

def generate_url(token):
    hyperlink_format = '<a href="{link}">{text}</a>'
    return hyperlink_format.format(link=BASE_URL+"forgotChange", text=token)



#Generates token using python UUID
def send_password_reset(user_email):
    email_server.starttls()
    email_server.login(USERNAME,PASSWORD)
    reset_token = tokenator.make_token(tokenator,user_email)
    msg = MIMEMultipart()
    url = generate_url(reset_token)
    print(url)
    msg['From']=user_email
    msg['To']=user_email
    msg['Subject']="Password reset token for Profile Password Management"
    message="Click this link to reset your password: " + url
    msg.attach(MIMEText(message,'html'))
    email_server.send_message(msg)
    del msg
    email_server.quit()
