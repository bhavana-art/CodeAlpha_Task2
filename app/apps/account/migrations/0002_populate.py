"""Populates Accounts, json generated via scripts/create_demo_accounts_data.py
This scripts ain't the best, should be improved for production
"""
import json
from pathlib import Path
from django.db import migrations
from django.utils.timezone import make_aware
from datetime import datetime

from django.contrib.auth.models import User

from apps.address.models import City, Address
from ..models import Account


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / "accounts_100.json"


def read_json(path):
	with open(path) as file:
		json_data = json.loads(file.read())
	return json_data


def populate(apps, schema_editor):
	accounts_data = read_json(DATA_PATH)

	# TODO: Learn how to use this approach instead, as per documentation, we SHOULD NOT use the model directly because they may be
	# updated by the time the migration run.
	# However the migration is not really friendly in terms of using already 'existing' data (which is, in this case the 'cities'
	# if we do so it won't be compatible because the data created in this process is 'faked' till submission i suppose?
	# _Address: Address = apps.get_model("address", "Address")
	# _City: City = apps.get_model("address", "City")
	# _Account: Account = apps.get_model("account", "Account")

	for username, data in accounts_data.items():
		try:
			user = data["user"]
			address = data["address"]
		except Exception as e:
			print(e)
			raise

		Account.objects.create(
			user=User.objects.create_user(
				username=username,
				email=user["email"],
				password=user["password"],
				first_name=user["first_name"],
				last_name=user["last_name"],
				date_joined=make_aware(datetime.strptime(user["date_joined"], "%Y-%m-%d %H:%M:%S"))
			),
			address=Address.objects.create(
				city=City.objects.get(name=address["city"]),
				street=address["street"],
				zip=address["zip"],
			),
			phone=data["phone"],
			birthday=make_aware(datetime.strptime(data["birthday"], "%Y-%m-%d")),
			job=data["job"],
		).save()


class Migration(migrations.Migration):
	dependencies = [
		('account', '0001_initial'),
	]

	operations = [
		migrations.RunPython(populate),
	]
