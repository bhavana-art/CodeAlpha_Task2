from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.address.models import Address


class Account(BaseModel):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="accounts")
	phone = models.CharField(_('Phone'), max_length=125)
	birthday = models.DateField(_("Birthday"), null=True, blank=True)
	job = models.CharField(_("Job"), max_length=255, blank=True)

	# TODO * Add 'gender' enum in account male|female|prefer not say
	# Todo: add 'bio' is a text ;)

	def __str__(self) -> str:
		return self.fullname

	@property
	def fullname(self) -> str:
		return self.user.get_full_name()
