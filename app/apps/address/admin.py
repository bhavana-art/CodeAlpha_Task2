from django.contrib import admin

from .models import Continent, SubRegion, Country, City, Address


class SubRegionTabularInline(admin.TabularInline):
	model = SubRegion


class ContinentAdmin(admin.ModelAdmin):
	inlines = (SubRegionTabularInline,)


class CityTabularInline(admin.TabularInline):
	model = City


class CountryAdmin(admin.ModelAdmin):
	inlines = (CityTabularInline,)


class AddressTabularInline(admin.TabularInline):
	model = Address


class CityAdmin(admin.ModelAdmin):
	inlines = (AddressTabularInline,)


admin.site.register(Continent, ContinentAdmin)
admin.site.register(SubRegion)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address)
