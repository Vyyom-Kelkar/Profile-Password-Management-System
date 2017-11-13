from app.resetToken import ResetTokenGenerator

token = ResetTokenGenerator

#Set up SMTP server
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
email_server.starttls()
USERNAME = ""
PASSWORD = ""
email_server.login(USERNAME, PASSWORD)


#Generates token using python UUID
def send_password_reset(user_email):
    msg = MIMEMultipart()
    msg['From']=user_email
    msg['To']=user_email
    msg['Subject']="Password reset token for Profile Password Management"
    message="This is your token, it expires in 3 hours: "
    msg.attach(MIMEText(message, 'plain'))
    email_server.send_message(msg)
    del msg
    email_server.quit()

