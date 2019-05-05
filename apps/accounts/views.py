from django.views.generic import TemplateView, View
from .forms import ProfileForm, UserForm
from django.shortcuts import redirect, render
from apps.accounts.forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# class LoginView(TemplateView):
#     template_name = "accounts/login.html"

class LoginView(View):
	form_class=LoginForm
	template_name="accounts/login.html"

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			return redirect('accounts:profile')
		return render(request,self.template_name,{'form':form})


# Create your views here.
class SignUpView(View):
	form_class=UserCreationForm
	template_name="accounts/signup.html"

	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			user=form.save(commit=False)

			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			# user.(password)
			user.password = password
			
			user.save()


			# user=authenticate(username=username,password=password)

			# if user is not None:

			# 	if user.is_active:
			# 		login(request,user)
			return redirect('accounts:profile')

		return render(request,self.template_name,{'form':form})

class ProfileView(TemplateView):
	template_name="accounts/profile.html"
 

def logout_view(request):
	logout(request)
	return redirect('accounts:login')