from django import forms

from petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter your comment...'}),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Search by pet name...'}
        )
    )