from django import forms
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class LoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        print('username ',self.fields)
        ## here i add the new fields that i need
        # self.fields["new-field"] = forms.CharField(label='Some label', max_length=100)
        self.fields['login'] = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Username'
        }))
        self.fields['password'] = forms.CharField(widget = forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Password'
        }))

class UserForm(SignupForm):

    
    def __init__(self, *args, **kwargs):
         
        super(UserForm, self).__init__(*args, **kwargs)
        
        ## here i add the new fields that i need
        # self.fields["new-field"] = forms.CharField(label='Some label', max_length=100)
        
        self.fields['username'] = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Username'
        }))

        self.fields['first_name'] = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'First Name'
        }))
        self.fields['last_name'] = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Last Name'
        }))
        
        self.fields['email'] = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Email Address',
        }))
        
        
        self.fields['password1'] = forms.CharField(widget = forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Password'
        }))
        self.fields['password2'] = forms.CharField(widget = forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm password'
        }))

       
        
class ProfileForm(UserCreationForm):

    username = forms.CharField(widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Username'
        }))

    first_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))

    last_name = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email'
    }), help_text='Required. Inform a valid email address.')

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Password'
        }))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm password'
        }))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')