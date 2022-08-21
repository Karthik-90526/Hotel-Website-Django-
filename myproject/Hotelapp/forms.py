from django import forms
from Hotelapp.models import signup
class register(forms.Form):
    class Meta:
        model =signup
        fields='_all_'