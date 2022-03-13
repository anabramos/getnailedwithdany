from django import forms
from allauth.account.forms import SignupForm
from .models import Appointment


class CustomSignupForm(SignupForm):
    """
    Add custom field to Allauth SignupForm
    This feature I took from GeeksforGeeks tutorial
    Python: Extending and customizing django-allauth
    """
    first_name = forms.CharField(max_length=20, label='First Name',
                                 widget=forms.TextInput
                                 (attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=20, label='Last Name',
                                widget=forms.TextInput
                                (attrs={'placeholder': 'Last Name'}))

    def save(self, request):
        """
        Save custom filed to User Model
        """
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class DateInput(forms.DateInput):
    """
    Custom widget for datefields in form
    """
    input_type = 'datetime-local'


class AppointmentForm(forms.ModelForm):
    """
    Creates Form from Appointment Module
    """
    class Meta:
        """
        Renders specific fields from the Appointment Module into the Form
        """
        model = Appointment
        fields = ['service',
                  'timestamp']
        widgets = {
            'timestamp': DateInput()
        }
