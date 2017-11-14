import urllib

from app.resetToken import ResetTokenGenerator
from app.resetConfig import BASE_URL,USERNAME,PASSWORD

token = ResetTokenGenerator

#Set up SMTP server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_server = smtplib.SMTP(host='smtp.gmail.com', port=587)


def generate_url(token):

    return BASE_URL + urllib.urlencode(token)



#Generates token using python UUID
def send_password_reset(user_email):
    email_server.starttls()
    email_server.login(USERNAME,PASSWORD)
    reset_token = token.make_token(user_email)
    msg = MIMEMultipart()
    msg['From']=user_email
    msg['To']=user_email
    msg['Subject']="Password reset token for Profile Password Management"
    message="This is your token, it expires in 3 hours: "
    msg.attach(MIMEText(message, 'plain'))
    email_server.send_message(msg)
    del msg
    email_server.quit()

