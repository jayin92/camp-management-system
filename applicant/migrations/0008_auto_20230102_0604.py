# Generated by Django 3.2.12 on 2023-01-02 06:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicant', '0007_alter_applicant_reviewers'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='self_introduction',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='reviewers',
            field=models.ManyToManyField(related_name='reviewers', through='applicant.Review', to=settings.AUTH_USER_MODEL),
        ),
    ]
