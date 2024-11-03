class ReadOnlyFieldsMixin:
    read_only_fields = []

    def make_fields_readonly(self):
        for field_name in self.read_only_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()


class DisableFieldsMixin:
    disable_fields = []

    def make_fields_disabled(self):
        for field in self.fields.values():
            field.disabled = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_disabled()