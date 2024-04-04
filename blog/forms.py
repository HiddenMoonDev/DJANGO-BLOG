from django import forms

class BlogForm(forms.Form):
  content = forms.CharField(
    widget = forms.Textarea(
      attrs={'class': "form-control", 'placeholder': "Enter your blog content here.", 'required': True, 'name': 'content'}
    )
  )

  author = forms.CharField(
    widget = forms.TextInput(
      attrs={'class': 'form-control', 'placeholder': 'Enter your name here', 'required': True, 'maxlength': 10, 'name': 'author'}
    )
  )

  title = forms.CharField(
    widget = forms.TextInput(
      attrs={'class': 'form-control', 'placeholder': 'Enter your blog title here', 'required': True, 'maxlength': 10, 'name': 'title'}
    )
  )


class CommentForm(forms.Form):
  author = forms.CharField(max_length=10,
    widget = forms.TextInput(
      attrs={"class": "form-control", "placeholder": "Your Name", "required": True, "name": "author", 'maxlength': 10}
    )
  )

  body = forms.CharField(max_length=400,
    widget = forms.Textarea(
      attrs={"class": "form-control", "placeholder": "Leave a comment!", "required": True, "name": "body", 'maxlength': 400}
    )
  )