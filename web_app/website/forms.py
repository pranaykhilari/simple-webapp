from allauth.account.forms import LoginForm, SignupForm
from django import forms


class UserLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'input-field'
        self.fields['password'].widget.attrs['class'] = 'input-field'

class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = "Email"
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'input-field'

        self.fields['username'].required = False
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'input-field'

        self.fields['password1'].widget.attrs['class'] = 'input-field'

        del self.fields['password2']


class UserProfile(forms.Form):
    name  = forms.CharField(label="Name", max_length=100)
    contact_no = forms.CharField(required=False)
    name.widget.attrs.update({'class':'input-field'})
    name.widget.attrs.update({'placeholder': 'Name'})
    contact_no.widget.attrs.update({'class':'input-field'})
    contact_no.widget.attrs.update({'placeholder':'Mobile No'})
