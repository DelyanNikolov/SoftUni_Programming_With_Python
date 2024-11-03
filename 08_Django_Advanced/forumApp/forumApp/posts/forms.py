from django import forms
from django.forms import formset_factory

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.mixins import DisableFormFieldsMixin
from forumApp.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFormFieldsMixin):
    disabled_fields = (
        "__all__",
    )


class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        labels = {
            'author': '',
            'content': ''
        }

        error_messages = {
            'author': {
                'required': 'Author name is required!'
            },
            'content': {
                'required': 'Content is required!'
            }
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name...',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...'
        })


CommentFormSet = formset_factory(CommentForm, extra=1)
