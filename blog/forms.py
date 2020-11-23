from django import forms
from .models import Comment
#check django form fields documentation for more details
class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields={'name','email','body'}
    