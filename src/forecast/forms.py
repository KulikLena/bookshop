from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your feedback', required=False)
    comment = forms.CharField()
f = CommentForm(auto_id=False)
print(f)