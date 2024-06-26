from django.db import models
from django.core.validators import RegexValidator

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.


def save_user_photo(instance, filename):
    return f"stakeholders/{instance.mobile_number}/{filename}"


from forms.storage import OverwriteStorage


class About(models.Model):
    DHULIKHEL_1 = 1
    DHULIKHEL_2 = 2
    DHULIKHEL_3 = 3
    DHULIKHEL_4 = 4
    DHULIKHEL_5 = 5
    DHULIKHEL_6 = 6
    DHULIKHEL_7 = 7
    DHULIKHEL_8 = 8
    DHULIKHEL_9 = 9
    DHULIKHEL_10 = 10
    DHULIKHEL_11 = 11
    DHULIKHEL_12 = 12

    WODA = (
        (DHULIKHEL_1, "धुलिखेल वडा नं १"),
        (DHULIKHEL_2, "धुलिखेल वडा नं २"),
        (DHULIKHEL_3, "धुलिखेल वडा नं ३"),
        (DHULIKHEL_4, "धुलिखेल वडा नं ४"),
        (DHULIKHEL_5, "धुलिखेल वडा नं ५"),
        (DHULIKHEL_6, "धुलिखेल वडा नं ६"),
        (DHULIKHEL_7, "धुलिखेल वडा नं ७"),
        (DHULIKHEL_8, "धुलिखेल वडा नं ८"),
        (DHULIKHEL_9, "धुलिखेल वडा नं ९"),
        (DHULIKHEL_10, "धुलिखेल वडा नं १०"),
        (DHULIKHEL_11, "धुलिखेल वडा नं ११"),
        (DHULIKHEL_12, "धुलिखेल वडा नं १२"),
    )
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_regex = RegexValidator(
        regex=r"^(\+\d{1,3})?,?\s?\d{8,13}",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    mobile_number = models.CharField(
        null=True, blank=True, validators=[phone_regex], max_length=17
    )
    position = models.CharField(max_length=200, blank=True, null=True)
    address = models.IntegerField(choices=WODA, blank=True, null=True)
    photo = models.ImageField(
        null=True, blank=True, upload_to=save_user_photo, storage=OverwriteStorage()
    )

    def __str__(self):
        return self.name
