# Generated by Django 4.2.1 on 2023-06-01 15:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import forms.models
import forms.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonsForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('gender', models.IntegerField(choices=[(1, 'महिला'), (2, 'पुरुष'), (3, 'अन्य')])),
                ('permanent_address', models.IntegerField(choices=[(1, 'धुलिखेल वडा नं १'), (2, 'धुलिखेल वडा नं २'), (3, 'धुलिखेल वडा नं ३'), (4, 'धुलिखेल वडा नं ४'), (5, 'धुलिखेल वडा नं ५'), (6, 'धुलिखेल वडा नं ६'), (7, 'धुलिखेल वडा नं ७'), (8, 'धुलिखेल वडा नं ८'), (9, 'धुलिखेल वडा नं ९'), (10, 'धुलिखेल वडा नं १०'), (11, 'धुलिखेल वडा नं ११'), (12, 'धुलिखेल वडा नं १२')])),
                ('temporary_address', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=30, null=True)),
                ('bday', models.DateField()),
                ('fathers_name', models.CharField(blank=True, max_length=256, null=True)),
                ('mothers_name', models.CharField(blank=True, max_length=256, null=True)),
                ('religion', models.CharField(blank=True, max_length=100, null=True)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('qualification', models.CharField(max_length=200)),
                ('office_domestic', models.CharField(blank=True, max_length=400, null=True)),
                ('office_international', models.CharField(blank=True, max_length=400, null=True)),
                ('mobile_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^(\\+\\d{1,3})?,?\\s?\\d{8,13}')])),
                ('photo', models.ImageField(blank=True, null=True, storage=forms.storage.OverwriteStorage(), upload_to=forms.models.save_user_photo)),
                ('blood_group', models.IntegerField(choices=[(1, 'A+'), (2, 'A-'), (3, 'B+'), (4, 'B-'), (5, 'AB+'), (6, 'AB-'), (7, 'O+'), (8, 'O-'), (9, 'थाछैन')])),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonTrainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training', models.CharField(max_length=2000)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.personsform')),
            ],
            options={
                'unique_together': {('person', 'training')},
            },
        ),
        migrations.CreateModel(
            name='PersonalSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=2000)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.personsform')),
            ],
            options={
                'unique_together': {('person', 'skills')},
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=300)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.personsform')),
            ],
            options={
                'unique_together': {('person', 'occupation')},
            },
        ),
        migrations.CreateModel(
            name='InterestedOccupation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interested_occupation', models.CharField(max_length=400)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.personsform')),
            ],
            options={
                'unique_together': {('person', 'interested_occupation')},
            },
        ),
    ]
