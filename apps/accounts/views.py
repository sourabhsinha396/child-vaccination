from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth import authenticate,login
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
# from this module
from .forms import LoginForm,RegisterForm,UpdateProfileModelForm


# Account Confirmation
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .token_generator import account_activation_token
from django.template.loader import render_to_string


def activation_sent_view(request):
    return render(request, 'accounts/snippets/activation_sent.html')


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            user.backend = "apps.accounts.custom_auth_backend.EmailAuthBackend"
            login(request, user)
            messages.success(request,'You are now logged in.')
            return redirect('vaccination:homepage')
        else:
            print(form.errors)
            messages.error(request,form.errors)
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return  render(request,'accounts/signup.html')


def user_login(request):
	if request.method == "POST":
		next_url= request.GET.get('next')

		form    = LoginForm(request.POST)
		context = {'form':form}
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request,username = username,password=password)
			print(user)
			if user is not None:
				if user.is_active:
					login(request,user)
					messages.success(request,'Successfully Logged In')
					if url_has_allowed_host_and_scheme(next_url,allowed_hosts=settings.ALLOWED_HOSTS,):
						return redirect(next_url)
					else:
						return redirect(reverse('vaccination:homepage'))
				else:
					messages.error(request,'You need to verify your email')
			else:
				messages.error(request,'We could not find an account with these credentials.')
			return render(request,'accounts/login.html',context)

		else:
			messages.error(request,form.errors)
			return render(request,'accounts/login.html',context)

	else:
		form = LoginForm()
		context = {'form':form}
		return render(request,'accounts/login.html',context)


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, 20, 'Logged out.')


@login_required
def overrided_password_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('/')
		else:
			messages.error(request,form.errors)
	else:
		form = PasswordChangeForm(request.user)
	context = {'form':form}
	return render(request, 'accounts/password_change.html',context)


def password_reset_done(request):
	return render(request,'accounts/password_reset_sent_msg.html')


def password_reset_complete(request):
	messages.success(request,'Password Reset Successful')
	return redirect(reverse('blogs:home'))