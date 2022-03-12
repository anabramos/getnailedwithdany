from django import forms


class ContactUsForm(forms.Form):
    """ Contact us form for users to submit messages """
    yourname = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
