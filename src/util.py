import re
from constants import Constants

class Util:

    @staticmethod
    def normalizestring(input):
        return re.sub(Constants.EMAIL_REGEX, Constants.NORMALIZE_CHAR, input)

    @staticmethod
    def get_nothing():
        return None