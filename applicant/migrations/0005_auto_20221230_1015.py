# Generated by Django 3.2.12 on 2022-12-30 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0004_auto_20221230_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='Accept',
        ),
        migrations.AddField(
            model_name='personal',
            name='Accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='Score',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='school',
        ),
    ]
