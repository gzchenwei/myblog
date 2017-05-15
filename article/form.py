from django import forms
from article.models import Article

class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'category', 'content')
