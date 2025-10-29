from django import forms

from user_app.models import User

class UserregisterForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','password','email']