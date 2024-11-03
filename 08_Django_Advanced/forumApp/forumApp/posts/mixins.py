from django import forms


class DisableFormFieldsMixin(forms.ModelForm):
    """takes field names to be disabled as tuple in disabled_fields
        __all__, to disable all fields
    """
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == "__all__" or field_name in self.disabled_fields:
                field.disabled = True
