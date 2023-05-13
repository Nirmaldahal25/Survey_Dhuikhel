from django.db import models

# Create your models here.
import nepali_datetime


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
        5: "अन्य",
    }

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
        12: "अन्य",
    }

    ADMIRED_OCCUPATION = {
        1: "कृषि तथा पशुपालन",
        2: "पर्यटन व्यवसाय(होमस्टे, होटल व्यवसाय)",
        3: "गित, संगीत र साहित्य सम्बन्धी",
        4: "खेलकुद सम्बन्धी",
        5: "साना तथा घरेलु उधोग",
        6: "सरकारी सेवा",
        7: "अन्य",
    }
    CASTE = {
        1: "ब्राम्हण/क्षत्री",
        2: "जनजाती",
        3: "दलित",
        4: "अल्पसंख्यक",
        5: "अन्य",
    }
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
    occupation = models.CharField(blank=False, null=False, max_length=200)
    interested_occupation = models.CharField(blank=True, null=True, max_length=400)
    office_domestic = models.CharField(blank=True, null=True, max_length=400)
    office_international = models.CharField(blank=True, null=True, max_length=400)
    mobile_number = models.PositiveIntegerField(null=False, blank=False)
    submitter_name = models.CharField(null=False, blank=True, max_length=400)

    @property
    def age(self):
        if not self.bday:
            return 0
        born = nepali_datetime.datetime.from_datetime_date(self.bday)
        today = nepali_datetime.date.today()
        return (
            today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        )


class EducationQualifications(models.Model):
    QUALIFICATION = {
        1: "आधारभुत तह",
        2: "एस.एल.सी./एस.ई.ई",
        3: "१०‌‌‍‍‌‌‍‍‍‌‌‌‌‌‌‌‌‌+२",
        4: "स्नातक",
        5: "स्नाकोत्तर",
        6: "अन्य",
    }
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    qualification = models.CharField(blank=False, null=False, max_length=200)


class PersonTrainings(models.Model):
    TRAININGS = {
        1: "कृषि तथा पशुपालन सम्बन्धी तालिम",
        2: "पर्यटन व्यवसाय(होमस्टे, होटल व्यवसाय) सम्बन्धी तालिम",
        3: "साना तथा घरेलु उधोग संचालन सम्बन्धी तालिम",
        4: "सरकारी सेवा तयारी तालिम",
        5: "गित, संगीत र साहित्य सम्बन्धी तालिम",
        6: "खेलकुद सम्बन्धी तालिम",
        7: "सकरात्मक सोच तथा सचेतनात्मक सोच सम्बन्धी अभिमुखिकरण तालिम",
        8: "अन्य",
    }
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    training = models.CharField(blank=False, null=False, max_length=2000)


class PersonalSkills(models.Model):
    person = models.ForeignKey(
        PersonsForm, on_delete=models.CASCADE, null=False, blank=False
    )
    skills = models.CharField(blank=False, null=False, max_length=2000)
