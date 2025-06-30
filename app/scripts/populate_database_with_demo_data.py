# credit: https://stackoverflow.com/a/41826771/13903942
import os
import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "people.settings")
django.setup()

from django.contrib.auth.models import User
from apps.account.models import Account
from app.data.demo_accounts import demo_accounts


def get_or_create_users() -> list[tuple[User, dict]]:
	users = []
	for username, user_info in demo_accounts.items():
		account_info = user_info.pop("account")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = User.objects.create_user(**user_info)
			print(f"User {user} created")

		users.append((user.get_full_name(), account_info))
	return users

def run():
	# TODO: Create users
	# account = Account.objects.get(pk=2)
	# print(f"Account is {str(account)}")
	users = get_or_create_users()
	print(users)


if __name__ == '__main__':
	run()
