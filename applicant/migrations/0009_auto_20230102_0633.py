# Generated by Django 3.2.12 on 2023-01-02 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applicant', '0008_auto_20230102_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='reviewers',
            field=models.ManyToManyField(related_name='reviewers', through='applicant.Review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant'),
        ),
    ]