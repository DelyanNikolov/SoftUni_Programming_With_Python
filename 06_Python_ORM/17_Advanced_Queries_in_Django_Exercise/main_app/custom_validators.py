from django.core.exceptions import ValidationError


class RangeValueValidator:
    """validates a value against a range, rises ValidationError with custom message"""
    def __init__(self, min_value: int, max_value: int, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}"
        else:
            self.__message = value

    def __call__(self, value: int):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.custom_validators.RangeValueValidator',
            [self.min_value, self.max_value],
            {'message': self.message},
        )
