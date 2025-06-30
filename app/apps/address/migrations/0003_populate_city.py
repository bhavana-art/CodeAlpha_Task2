"""
This scripts ain't the best, should be improved for production
"""

from django.db import migrations
from ..models import Country, City


def populate(apps, schema_editor):
	_Country: Country = apps.get_model("address", "Country")

	italy = Country.objects.get(name='italy')
	france = Country.objects.get(name='france')
	spain = Country.objects.get(name='spain')
	portugal = Country.objects.get(name='portugal')
	germany = Country.objects.get(name='germany')
	austria = Country.objects.get(name='austria')
	netherlands = Country.objects.get(name='netherlands')
	uk = Country.objects.get(iso_alpha2='GB')
	ireland = Country.objects.get(name='ireland')

	usa = Country.objects.get(iso_alpha2='US')
	argentina = Country.objects.get(name='argentina')

	japan = Country.objects.get(name='japan')
	united_arab_emirates = Country.objects.get(name='united arab emirates')
	singapore = Country.objects.get(name='singapore')
	south_korea = Country.objects.get(iso_alpha2='KR')
	hong_kong = Country.objects.get(name='hong kong')

	City.objects.create(name='rome', country=italy).save()
	City.objects.create(name='milan', country=italy).save()
	City.objects.create(name='turin', country=italy).save()

	City.objects.create(name='paris', country=france).save()
	City.objects.create(name='lyon', country=france).save()

	City.objects.create(name='madrid', country=spain).save()
	City.objects.create(name='barcelona', country=spain).save()

	City.objects.create(name='lisbon', country=portugal).save()
	City.objects.create(name='porto', country=portugal).save()

	City.objects.create(name='berlin', country=germany).save()
	City.objects.create(name='munich', country=germany).save()

	City.objects.create(name='vienna', country=austria).save()
	City.objects.create(name='graz', country=austria).save()

	City.objects.create(name='amsterdam', country=netherlands).save()
	City.objects.create(name='rotterdam', country=netherlands).save()

	City.objects.create(name='london', country=uk).save()
	City.objects.create(name='edinburgh', country=uk).save()
	City.objects.create(name='manchester', country=uk).save()
	City.objects.create(name='oxford', country=uk).save()
	City.objects.create(name='liverpool', country=uk).save()

	City.objects.create(name='dublin', country=ireland).save()
	City.objects.create(name='belfast', country=ireland).save()

	City.objects.create(name='new york', country=usa).save()
	City.objects.create(name='las vegas', country=usa).save()
	City.objects.create(name='orlando', country=usa).save()
	City.objects.create(name='miami', country=usa).save()
	City.objects.create(name='chicago', country=usa).save()
	City.objects.create(name='san francisco', country=usa).save()
	City.objects.create(name='washington, D.C.', country=usa).save()

	City.objects.create(name='buenos aires', country=argentina).save()

	City.objects.create(name='tokyo', country=japan).save()
	City.objects.create(name='osaka', country=japan).save()

	City.objects.create(name='dubai', country=united_arab_emirates).save()
	City.objects.create(name='singapore', country=singapore).save()
	City.objects.create(name='seoul', country=south_korea).save()
	City.objects.create(name='Hong Kong', country=hong_kong).save()


class Migration(migrations.Migration):
	dependencies = [
		('address', '0002_populate'),
	]

	operations = [
		migrations.RunPython(populate),
	]
