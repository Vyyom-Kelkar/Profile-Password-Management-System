import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.http import int_to_base36

# One time url token class
class AccountResetTokenGenerator(PasswordResetTokenGenerator)
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_con)
        )

#Set up SMTP server
email_server = smtplib.SMTP(host='smtp.gmail.com', port=587)
email_server.starttls()
USERNAME = "poulideveloping@gmail.com"
PASSWORD = "W1thGreatPower"
email_server.login(USERNAME, PASSWORD)


def generate_token():
    token = uuid.uuid4()
    return token

#Generates token using python UUID
def send_password_reset(user_email):
    reset = generate_token()
    msg = MIMEMultipart()
    msg['From']=user_email
    msg['To']=user_email
    msg['Subject']="Password reset token for Profile Password Management"
    message="This is your token, it expires in 3 hours: " + str(reset)
    msg.attach(MIMEText(message, 'plain'))
    email_server.send_message(msg)
    del msg
    email_server.quit()
    return reset

