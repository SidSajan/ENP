from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from apps.accounts.models import NormalLogin

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields= ['username','email','first_name','last_name','password']


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model=User
		fields= ['email','first_name','last_name']


class LoginForm(forms.Form):
	username= forms.CharField()
	password = forms.CharField( widget=forms.PasswordInput)

	def clean(self):
		cleaned_data =super(LoginForm, self).clean()
		username =cleaned_data.get('username')
		password =cleaned_data.get('password')

		user = NormalLogin.objects.filter(username=username).first()
		if user:
			# convert to hash value
			if user.password != password:
				raise forms.ValidationError({'password':'The entered password is invalid'})
		else:
			raise forms.ValidationError({'username':'This username does not exist.'})
		return cleaned_data

class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text="enter password",
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    class Meta:
        model = NormalLogin
        fields = ("username",)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self._meta.model.USERNAME_FIELD in self.fields:
    #         self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    # def _post_clean(self):
    #     super()._post_clean()
    #     # Validate the password after self.instance is updated with form data
    #     # by super().
    #     password = self.cleaned_data.get('password2')
    #     if password:
    #         try:
    #             password_validation.validate_password(password, self.instance)
    #         except forms.ValidationError as error:
    #             self.add_error('password2', error)

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user