from django import forms
from .models import RSVP


# Auction form
class RsvpForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))

    class Meta:

        model = RSVP
        fields = ['first_name', 'last_name', 'email', 'will_be_present']