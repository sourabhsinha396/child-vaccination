from django.contrib.auth.tokens import PasswordResetTokenGenerator
#earlier we had six in django.utils but since 3.0 deprecated
#so now first "pip install six" then import from it


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
	pass
	##We can make our own encrypter here but for now relying on PasswordResetTokenGenerator
	# def hash_it(self,user):
	# 	return ( text_type(user.pk))

account_activation_token = AccountActivationTokenGenerator()
