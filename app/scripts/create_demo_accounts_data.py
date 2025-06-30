"""
Use this script to create demo data for populating 'People!' Accounts models
"""
import random
import json
from datetime import datetime

from faker import Faker
from faker.providers import date_time, address, job, phone_number


DEFAULT_PASSWORD = "xPwVOJ-L0vVY3ERaLKgWOg"  # use same for all demo, so to don't go crazy if we want to test with a user the pass is always the same
LOCALES_MUTLI = ["en_GB", "fr_FR", "it_IT", "de_DE", "es_ES", "ru_RU", "ja_JP", "zh_CN"]  # check how make Django work with multiple languages
LOCALES = ["en_GB", "fr_FR", "it_IT", "de_DE", "es_ES"]
AVAILABLE_DEMO_CITIES = ['rome', 'milan', 'turin', 'paris', 'lyon', 'madrid', 'barcelona', 'lisbon', 'porto', 'berlin', 'munich', 'vienna', 'graz', 'amsterdam', 'rotterdam', 'london', 'edinburgh', 'manchester', 'oxford', 'liverpool', 'dublin', 'belfast', 'new york', 'las vegas', 'orlando', 'miami', 'chicago', 'san francisco', 'washington, d.c.', 'buenos aires', 'tokyo', 'osaka', 'dubai', 'singapore', 'seoul', 'hong kong']
PRETTY_PRINT = False

fake = Faker(LOCALES)

fake_with_providers = Faker()
fake_with_providers.add_provider(date_time)
fake_with_providers.add_provider(address)
fake_with_providers.add_provider(job)
fake_with_providers.add_provider(phone_number)

def format_datetime(date_time: datetime) -> str:
	return date_time.strftime("%Y-%m-%d %H:%M:%S")

def format_date(date_time: datetime) -> str:
	return date_time.strftime("%Y-%m-%d")

def create_accounts(total_users):
	print(f"Total users: {total_users}")
	print("Creating demo data...")
	users_data = {}
	for count in range(total_users):
		username = fake.user_name()
		users_data[username] = {
			"user": {
				"username": username,
				"first_name": fake.first_name(),
				"last_name": fake.last_name(),
				"email": fake.email(),
				"password": DEFAULT_PASSWORD,
				"is_superuser": 0,
				"is_staff": 0,
				"is_active": 1,
				"date_joined": format_datetime(fake_with_providers.date_time_this_decade()),
			},
			"address": {
				"city": random.choice(AVAILABLE_DEMO_CITIES),
				"street": f"{fake.street_name()}, {fake.building_number()}",
				"zip": fake_with_providers.postcode()
			},
			"phone": fake_with_providers.phone_number(),
			"birthday": format_date(fake_with_providers.date_of_birth()),
			"job": fake_with_providers.job(),
		}
	if PRETTY_PRINT:
		print(json.dumps(users_data, indent=4))
	else:
		print(json.dumps(users_data))
	print("-"*200)

create_accounts(100)
