# This file handles the tokens for forgotten passwords
# Arthur Nyoni

import uuid
from sqlalchemy import update
from app.models import User, engine, mysession

secret = 'Gr8Responsibility'

class ResetTokenGenerator:
    """
    Generates and checks tokens for password reset
    """
    key_salt = "Profile.Password.Management.System.ResetTokenGenerator"
    life = 0;

    # Generate unique token for password reset
    def make_token(self, user_email):

        if self.life<1:
            token = uuid.uuid4()
            token_to_db = update(User).where(User.email == user_email).values(token=token)
            engine.execute(token_to_db)
            self.life =1;
        else:
            token = -1
        return token

    # Remove token from db after use or timeout
    def remove_token(self,user_email):
        token_kill = update(User).where(User.email==user_email).values(token="")
        engine.execute(token_kill)

	# Check provided token against token stored in db and return True only if matched
    def check_token(self,user_email, token):
        #Retrieve db token for given usermail
        token_list = mysession.query(User).filter_by(user_email=user_email).all()
        token_db = token_list[0]
        token_match = token is token_db

        if not (user_email and token):
            return False
        if not token_match:
            return False

        self.remove_token(user_email)
        return True
