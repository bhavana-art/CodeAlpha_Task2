from datetime import datetime

from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from django.test import TestCase

from apps.address.models import Continent, SubRegion, Country, City, Address
from apps.social_media.models import Account
from apps.social_media.models import LinkAccount


class LinkAccountTests(TestCase):
	def setUp(self):
		self.city = City.objects.create(
			name="barcelona",
			country=Country.objects.create(
				name="Spain",
				iso_alpha2="ES",
				iso_alpha3="ESP",
				iso_3116_2="ISO 3166-2:ES",
				code=724,
				continent=SubRegion.objects.create(
					name="Southern Europe",
					code=39,
					intermediate_region="",
					intermediate_region_code=None,
					continent=Continent.objects.create(
						name="Europe",
						code=150
					),
				)
			)
		)
		self.address_1 = Address.objects.create(
			city=self.city,
			street="St. Test, 21",
			zip="0845",
		)
		self.address_2 = Address.objects.create(
			city=self.city,
			street="Road Infinite, 315",
			zip="0825",
		)

		self.account_source = Account.objects.create(
			user=User.objects.create_user(
				'unittest_user',
				'unittest.social_media@test.com',
				'password',
				first_name='john',
				last_name='doe'
			),
			address=self.address_1,
			phone="+44 954-546-654",
			birthday=make_aware(datetime.strptime("1991-05-11", "%Y-%m-%d")),
			job="Unittester"
		)
		self.account_source.save()

		self.account_target = Account.objects.create(
			user=User.objects.create_user(
				'unittest_user_target',
				'unittest.social_media.target@test.com',
				'password',
				first_name='Friendly',
				last_name='Person'
			),
			address=self.address_2,
			phone="+44 954-546-654",
			birthday=make_aware(datetime.strptime("1991-05-11", "%Y-%m-%d")),
			job="Unittester"
		)
		self.account_target.save()

	def test_link_source_target_is_pending_by_default(self):
		link = LinkAccount.objects.create(source=self.account_source, target=self.account_target)
		link.save()

		self.assertEqual(link.status, "pending")
