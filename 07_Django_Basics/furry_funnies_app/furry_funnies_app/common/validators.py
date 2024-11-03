from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your name must contain letters only!'
        else:
            self.__message = value

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class PasscodeDigitsCountValidator:
    """validates only digits and digits count"""

    def __init__(self, digits_count=None, message=None):
        self.message = message
        self.digits_count = digits_count

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Your passcode must be exactly 6 digits!'
        else:
            self.__message = value

    @property
    def digits_count(self):
        return self.__digits_count

    @digits_count.setter
    def digits_count(self, value):
        if value is None:
            self.__digits_count = 6
        else:
            self.__digits_count = value

    def __call__(self, value):
        if not value.isdigit() or len(value) != self.digits_count:
            raise ValidationError(self.message)
