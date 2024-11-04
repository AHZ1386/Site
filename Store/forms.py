from django.forms import ModelForm
from .models import Comment

class PostCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']