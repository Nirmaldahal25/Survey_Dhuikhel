# Generated by Django 4.2.1 on 2023-06-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personsform',
            name='married',
            field=models.IntegerField(choices=[(1, 'विवाहित'), (2, 'अविवाहित'), (3, 'सम्बन्धविच्छेद भएको')]),
        ),
    ]