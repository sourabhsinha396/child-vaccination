from django.contrib.auth import get_user_model


User = get_user_model()


class EmailAuthBackend(object):
	"""It provides the functionality to slide down to email to login,
	instead of just username"""
	def authenticate(self,request,username=None,password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user 
			return None
		except User.DoesNotExist:
			return None

	def get_user(self,user_id):
		try:
			return User.objects.get(id=user_id)
		except User.DoesNotExist:
			return None