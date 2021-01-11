from django import forms

class CommentForm(forms.Form):
    # Widgets tell Django to load it as a HTML element
    # Load as text input element
    author = forms.CharField(
        max_length=60, 
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "Placeholder": "Your Name"
        })
    )
    # Load as text area element
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment"
        })
    )