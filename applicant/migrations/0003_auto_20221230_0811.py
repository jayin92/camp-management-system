# Generated by Django 3.2.12 on 2022-12-30 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_personal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='Club',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='EmergePhone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='FB',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='InformedFrom',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Motivation',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ParentAgree',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ParentPhone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='personal',
            name='SelfPhone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='personal',
            name='SpecialDietary',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='SpecialDisease',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='Telephone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='WantToSay',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
