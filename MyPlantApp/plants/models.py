from django.db import models
from django.core.validators import MinLengthValidator
from .validators import plant_name_only_letters, check_name, plant_price_validator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2)],
    )
    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[check_name],
    )
    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[check_name],
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Plant(models.Model):
    CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )
    plant_type = models.CharField(
        max_length=14,
        blank=False,
        null=False,
        choices=CHOICES,
    )
    name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=[MinLengthValidator(2), plant_name_only_letters],

    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[plant_price_validator],
    )
    #
    # profile = models.ForeignKey(
    #     Profile,
    #     on_delete=models.CASCADE,
    # )
