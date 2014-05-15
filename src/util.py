import re, hashlib
from datetime import datetime, timedelta
from constants import Constants


class Util:

    @staticmethod
    def normalizestring(input):
        return re.sub(Constants.EMAIL_REGEX, Constants.NORMALIZE_CHAR, input)


    @staticmethod
    def md5(input):
        return hashlib.md5(input).digest()

    @staticmethod
    def expiry_time():
        now_plus_24 = datetime.now() + timedelta(hours=24)
        return now_plus_24

    @staticmethod
    def get_nothing():
        return None