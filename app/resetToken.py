import uuid

secret = 'Gr8Responsibility'

class ResetTokenGenerator:
    """
    Generates and checks tokens for password reset
    """
    key_salt = "Profile.Password.Management.System.ResetTokenGenerator"
    life = 0;

    def make_token(self, user_email):

        if self.life<1:
            token = uuid.uuid4()
            self.life =1;
        else:
            token = -1
        return token

    def check_token(self,user_email, token):
        # ToDo receive copy of token from db
        if not (user_email and token):
            return False
        if not (token is user_email.token):
            return False
        return True

tokenMan = ResetTokenGenerator()
