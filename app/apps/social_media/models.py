from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.base.models import BaseModel
from apps.account.models import Account


class Link(BaseModel):
	"""Base class of a social media 'link'"""

	class Status(models.TextChoices):
		PENDING = "pending", _("Pending")
		ACCEPTED = "accepted", _("Accepted")
		REJECTED = "rejected", _("Rejected")

	source = models.PositiveBigIntegerField()
	target = models.PositiveBigIntegerField()
	status = models.CharField(
		max_length=10,
		choices=Status,
		default=Status.PENDING,
	)

	class Meta:
		abstract = True


class LinkAccount(Link):
	source = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="source")
	target = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="target")

	class Meta:
		db_table = "social_media_link_account"
		unique_together = ("source", "target")
