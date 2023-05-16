# Generated by Django 4.2.1 on 2023-05-16 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='interestedoccupation',
            unique_together={('person', 'interested_occupation')},
        ),
        migrations.AlterUniqueTogether(
            name='personalskills',
            unique_together={('person', 'skills')},
        ),
        migrations.AlterUniqueTogether(
            name='persontrainings',
            unique_together={('person', 'training')},
        ),
    ]
