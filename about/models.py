from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.

def save_user_photo(instance, filename):
    return f"{instance.name}/{instance.mobile_number}/{filename}"
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
    name = models.CharField(max_length=122, null=False, blank=False)
    email = models.CharField(max_length=122, null=True, blank=True)
    mobile_number = models.PositiveIntegerField(null=False, blank=False)
    position = models.CharField(max_length=100)
    address = models.IntegerField(choices=WODA, blank=False, null=False)
    photo = models.ImageField(
        null=True, blank=True, upload_to=save_user_photo, storage=OverwriteStorage()
    )

    def __str__(self):
        return self.name
    