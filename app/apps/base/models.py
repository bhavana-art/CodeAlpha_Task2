from django.db import models


class BaseModel(models.Model):
	"""Custom base model with common fields and functionalities"""

	class Meta:
		abstract = True

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)


class LowerCaseCharField(models.CharField):
	"""Ensure that string is always lowercase"""
	def get_prep_value(self, value: str | None) -> str | None:
		value = super().get_prep_value(value)
		return value if value is None else value.lower()


class UpperCaseCharField(models.CharField):
	"""Ensure that string is always uppercase"""
	def get_prep_value(self, value: str | None) -> str | None:
		value = super().get_prep_value(value)
		return value if value is None else value.upper()
