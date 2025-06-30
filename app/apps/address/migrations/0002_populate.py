"""Populates Addresses table with Country csv taken from https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv
This scripts ain't the best, should be improved for production
"""

from pathlib import Path
from django.db import migrations
from django.db.utils import IntegrityError
from ..models import Continent, SubRegion, Country, City, Address

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / "countries.csv"


def read_csv(path):
	with open(path) as csvfile:
		_rows = []
		for line in csvfile.read().split("\n"):
			if not line:
				continue
			row_clean = []
			for cell in line.split(","):
				if cell == '""':
					cell = ''
				else:
					cell.strip()
				row_clean.append(cell)

			row = {
				"country_name": row_clean[0],
				"country_iso_alpha2": row_clean[1],
				"country_iso_alpha3": row_clean[2],
				"country_code": row_clean[3],
				"country_iso_3116_2": row_clean[4],

				"continent_name": row_clean[5],
				"continent_code": row_clean[8],

				"sub_region_name": row_clean[6],
				"sub_region_code": row_clean[9],

				"intermediate_name": row_clean[7],
				"intermediate_code": row_clean[10],
			}
			_rows.append(row)

	_header = _rows.pop(0)
	return _header, _rows


def populate(apps, schema_editor):
	header, rows = read_csv(DATA_PATH)

	_Continent: Continent = apps.get_model("address", "Continent")
	_SubRegion: SubRegion = apps.get_model("address", "SubRegion")
	_Country: Country = apps.get_model("address", "Country")
	_City: City = apps.get_model("address", "City")
	_Address: Address = apps.get_model("address", "Address")

	continents = {}
	for row in rows:
		name = row["continent_name"]
		continent_code = row["continent_code"]
		if name in continents:
			continue
		if continent_code == '':
			continent_code = 0

		continent = _Continent.objects.create(
			name=name,
			code=int(continent_code),
		)
		continent.save()
		continents[name] = continent

	sub_regions = {}
	for row in rows:
		name = row["sub_region_name"]
		intermediate_name = row["intermediate_name"]
		if (name, intermediate_name) in sub_regions:
			continue

		continent_name = row["continent_name"]
		continent = continents[continent_name]
		sub_region_code = row["sub_region_code"]
		if sub_region_code == '':
			sub_region_code = 0

		intermediate_code = row["intermediate_code"]
		subregion = _SubRegion.objects.create(
			name=name,
			code=int(sub_region_code),
			intermediate_region=intermediate_name,
			intermediate_region_code=int(intermediate_code) if intermediate_code else None,
			continent=continent,
		)
		subregion.save()
		sub_regions[(name, intermediate_name)] = subregion

	for count, row in enumerate(rows):
		country_code = row["country_code"]
		sub_region_name = row["sub_region_name"]
		intermediate_name = row["intermediate_name"]
		subregion = sub_regions[(sub_region_name, intermediate_name)]
		try:
			country = _Country.objects.create(
				name=row["country_name"],
				iso_alpha2=row["country_iso_alpha2"],
				iso_alpha3=row["country_iso_alpha3"],
				iso_3116_2=row["country_iso_3116_2"],
				code=int(country_code),
				continent=subregion
			)
		except IntegrityError as error:
			print(f"Error {row} Error {error}")
			continue
		country.save()


class Migration(migrations.Migration):
	dependencies = [
		('address', '0001_initial'),
	]

	operations = [
		migrations.RunPython(populate),
	]
