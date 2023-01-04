# Generated by Django 3.2.12 on 2023-01-02 11:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicant', '0010_auto_20230102_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='reviewers',
            field=models.ManyToManyField(related_name='reviewers', through='applicant.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
