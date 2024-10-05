from django.core.exceptions import ValidationError


class OnlyLettersValidator:
    def __init__(self, message="Fruit name should only contain letters"):
        self.message = message

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'fruitipediaApp.fruits.validators.OnlyLettersValidator',
            (),
            {'message': self.message}
        )
