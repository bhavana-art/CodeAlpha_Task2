"""Populate the 'demo' account to play with
This scripts ain't the best, should be improved for production
"""
from django.db import migrations
from django.utils.timezone import make_aware
from datetime import datetime

from django.contrib.auth.models import User

from apps.address.models import City, Address
from ..models import Account


def populate(apps, schema_editor):
	# TODO: Learn how to use this approach instead, as per documentation, we SHOULD NOT use the model directly because they may be
	# updated by the time the migration run.
	# However the migration is not really friendly in terms of using already 'existing' data (which is, in this case the 'cities'
	# if we do so it won't be compatible because the data created in this process is 'faked' till submission i suppose?
	# _Address: Address = apps.get_model("address", "Address")
	# _City: City = apps.get_model("address", "City")
	# _Account: Account = apps.get_model("account", "Account")

	data = {
		"user": {
			"username": "peoplePerson",
			"first_name": "Guy",
			"last_name": "Awesome",
			"email": "awesome.guy@demo.com",
			"password": "awesome",
			"is_superuser": 0,
			"is_staff": 0,
			"is_active": 1,
			"date_joined": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		},
		"address": {
			"city": "barcelona",
			"street": "Calle Cantabria, 20",
			"zip": "08010"
		},
		"phone": "+34 672-456-7890",
		"birthday": "1991-05-11",
		"job": "Software Developer"
	}
	user = data["user"]
	address = data["address"]
	username = user["username"]

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
		('account', '0002_populate'),
	]

	operations = [
		migrations.RunPython(populate),
	]
