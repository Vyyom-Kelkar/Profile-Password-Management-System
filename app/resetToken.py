from datetime import date

from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.http import base36_to_int, int_to_base36

PASSWORD_RESET_TIMEOUT = 1

class ResetTokenGenerator:
    """
    Generates and checks tokens for password reset
    """
    key_salt = "Profile.Password.Management.System.ResetTokenGenerator"
    secret = 'Gr8Responsibility'

    def make_token(self, user_email):
        # Return a token that can be used once to reset password
        return self._make_token_with_ts(user_email, self._num_days(self._today()))


    def check_token(self, user_email, token):
        # Check that password reset token for given user is correct and not expired
        if not (user_email and token):
            return False
        # Parse token
        try:
            ts_b36, hash = token.split("-")
        except ValueError:
            return False

        try:
            ts = base36_to_int(ts_b36)
        except ValueError:
            return False


        # Check for tampering
        if not constant_time_compare(self._make_token_with_timestamp(user_email, ts), token):
            return False

        if (self._num_days(self._today())-ts) > PASSWORD_RESET_TIMEOUT:
            return False

        return True

def _make_token_with_timestamp(self, user_email, timestamp):
    ts_b36 = int_to_base36(timestamp)

    hash = salted_hmac(self.key_salt,
                       self._make_hash_value(user_email, timestamp),
                       secret=self.secret,
                       ).hexdigest()[::2]
    return "%s-%s" % (ts_b36, hash)


def _make_hash_value(self, user_email, timestamp):
    login_timestamp = '' if user_email.last_login is None else user_email.last_login.replace(microsecond=0, tzinfo=None)

    return str(user_email.pk) + user_email.password + str(login_timestamp) + str(timestamp)


def _num_days(self,dt):
    return (dt - date(2010,1,1)).days

def _today(self):
    return date.today()