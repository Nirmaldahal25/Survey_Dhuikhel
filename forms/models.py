from django.db import models

# Create your models here.
import nepali_datetime
from django.contrib.auth.models import User
from forms.storage import OverwriteStorage
from django.core.validators import RegexValidator


def save_user_photo(instance, filename):
    return f"{instance.submitter.username}/{instance.mobile_number}/{filename}"


class PersonsForm(models.Model):
    # genders
    FEMALE = 1
    MALE = 2
    OTHERS = 3

    # woda
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

    GENDER = ((FEMALE, "महिला"), (MALE, "पुरुष"), (OTHERS, "अन्य"))
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

    RELIGION = {
        1: "हिन्दु",
        2: "बौद्व",
        3: "क्रिस्चियन",
        4: "मुस्लिम",
    }

    QUALIFICATION = {
        1: "आधारभुत तह",
        2: "एस.एल.सी./एस.ई.ई",
        3: "१०‌‌‍‍‌‌‍‍‍‌‌‌‌‌‌‌‌‌+२",
        4: "स्नातक",
        5: "स्नाकोत्तर",
    }

    CASTE = {
        1: "ब्राम्हण/क्षत्री",
        2: "जनजाती",
        3: "दलित",
        4: "अल्पसंख्यक",
    }

    BLOOD_GROUP = (
        (1, "A+"),
        (2, "A-"),
        (3, "B+"),
        (4, "B-"),
        (5, "AB+"),
        (6, "AB-"),
        (7, "O+"),
        (8, "O-"),
        (9, "थाछैन"),
    )
    name = models.CharField(max_length=256, null=False, blank=False)
    gender = models.IntegerField(choices=GENDER, null=False, blank=False)
    permanent_address = models.IntegerField(choices=WODA, blank=False, null=False)
    temporary_address = models.CharField(blank=False, null=False, max_length=300)
    email = models.EmailField(blank=True, null=True)
    citizenship = models.CharField(max_length=30, blank=True, null=True)
    bday = models.DateField(null=False, blank=False)
    fathers_name = models.CharField(blank=True, null=True, max_length=256)
    mothers_name = models.CharField(blank=True, null=True, max_length=256)
    religion = models.CharField(blank=True, null=True, max_length=100)
    caste = models.CharField(blank=True, null=True, max_length=100)
    qualification = models.CharField(blank=False, null=False, max_length=200)
    office_domestic = models.CharField(blank=True, null=True, max_length=400)
    office_international = models.CharField(blank=True, null=True, max_length=400)

    phone_regex = RegexValidator(
        regex=r"^(\+\d{1,3})?,?\s?\d{8,13}",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )
    mobile_number = models.CharField(
        null=False, blank=False, unique=True, validators=[phone_regex], max_length=17
    )
    submitter = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.DO_NOTHING
    )
    photo = models.ImageField(
        null=True, blank=True, upload_to=save_user_photo, storage=OverwriteStorage()
    )
    blood_group = models.IntegerField(choices=BLOOD_GROUP, blank=False, null=False)

    @property
    def age(self):
        if not self.bday:
            return 0
        born = nepali_datetime.datetime.from_datetime_date(self.bday)
        today = nepali_datetime.date.today()
        return (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )


class InterestedOccupation(models.Model):
    ADMIRED_OCCUPATION = {
        1: "कृषि तथा पशुपालन",
        2: "पर्यटन व्यवसाय(होमस्टे, होटल व्यवसाय)",
        3: "गित, संगीत र साहित्य सम्बन्धी",
        4: "खेलकुद सम्बन्धी",
        5: "साना तथा घरेलु उधोग",
        6: "सरकारी सेवा",
    }
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    interested_occupation = models.CharField(blank=False, null=False, max_length=400)

    class Meta:
        unique_together = ("person", "interested_occupation")


class PersonTrainings(models.Model):
    TRAININGS = {
        1: "कृषि तथा पशुपालन सम्बन्धी तालिम",
        2: "पर्यटन व्यवसाय(होमस्टे, होटल व्यवसाय) सम्बन्धी तालिम",
        3: "साना तथा घरेलु उधोग संचालन सम्बन्धी तालिम",
        4: "सरकारी सेवा तयारी तालिम",
        5: "गित, संगीत र साहित्य सम्बन्धी तालिम",
        6: "खेलकुद सम्बन्धी तालिम",
        7: "सकरात्मक सोच तथा सचेतनात्मक सोच सम्बन्धी अभिमुखिकरण तालिम",
    }
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    training = models.CharField(blank=False, null=False, max_length=400)

    class Meta:
        unique_together = ("person", "training")


class PersonalSkills(models.Model):
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    skills = models.CharField(blank=False, null=False, max_length=400)

    class Meta:
        unique_together = ("person", "skills")


class Occupation(models.Model):
    OCCUPATION = {
        1: "सरकारी सेवा करार",
        2: "सरकारी सेवा स्थायी",
        3: "शिक्षण सरकारी",
        4: "शिक्षण प्राइभेट",
        5: "प्राइभेट नोकरी",
        6: "बैंक",
        7: "विमा",
        8: "सहकारी संस्था",
        9: "होटल व्यवसायी",
        10: "आफ्नै व्यवसायी",
        11: "कुनै पेशा रोजगारमा संलग्न नरहेको",
    }
    occupation = models.CharField(blank=False, null=False, max_length=400)
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        unique_together = ("person", "occupation")
