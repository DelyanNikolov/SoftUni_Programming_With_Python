from django import forms

from furry_funnies_app.mixins import ReadOnlyFieldsMixin, DisableFieldsMixin
from furry_funnies_app.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Put an attractive and unique title...'})
        self.fields['image_url'].label = 'Post Image URL'
        self.fields['content'].widget.attrs.update(
            {'placeholder': 'Share some interesting facts about your adorable pets...'}
        )


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''


class PostDeleteForm(ReadOnlyFieldsMixin, PostBaseForm):
    # there is a DisableFieldsMixin if the fields should be also disabled
    # by requirements all the fields should be read-only
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].help_text = ''

    read_only_fields = ['title', 'image_url', 'content']
