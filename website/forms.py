from django import forms


class ContactUsForm(forms.Form):
    """ Contact us form for users to submit messages """
    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(label='Subject of your message', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
