from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('signup/',views.signup,name="signup"),
	path('sent/', views.activation_sent_view, name="activation_sent"),
	path('login/',views.user_login,name="login"),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),
	path('password/change/',views.overrided_password_change,name="password_change"),
	path('password/reset/',auth_views.PasswordResetView.as_view(template_name='user_accounts/password_reset.html'),
													name="password_reset"),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user_accounts/password_reset_confirm.html'),
													name='password_reset_confirm'),
	path('reset/done/',views.password_reset_done,name='password_reset_done'),
	path('reset/complete/',views.password_reset_complete,name='password_reset_complete'),
	]