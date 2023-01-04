from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

# Create your models here.

class Applicant(models.Model):
    
    SEX_CHOICES = (
        ("男", "男"),
        ("女", "女"),
    )

    SIZE_CHOICES = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("2L", "2L"),
    )

    PHASE_CHOICES = (
        ("earlybird", "早鳥"),
        ("normal", "一階"),
    )

    register_time = models.DateTimeField()
    email = models.EmailField()
    name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=20)
    birthday = models.DateField()
    sex = models.CharField(max_length=20, choices=SEX_CHOICES)
    telephone = models.CharField(max_length=20, null=True)
    parent_phone = models.CharField(max_length=20)
    self_phone = models.CharField(max_length=20)
    emergency_name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    emerge_phone = models.CharField(max_length=20, null=True, blank=True)
    school = models.CharField(max_length=512)
    major = models.CharField(max_length=512)
    club = models.CharField(max_length=512, null=True, blank=True)
    special_dietary = models.CharField(max_length=512, null=True, blank=True)
    special_disease = models.CharField(max_length=512, null=True, blank=True)
    facebook = models.CharField(max_length=512, null=True, blank=True)
    group_apply = models.BooleanField()
    group_person1 = models.ForeignKey("self", on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    group_person2 = models.ForeignKey("self", on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    group_person3 = models.ForeignKey("self", on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    self_introduction = models.TextField(null=True)
    picture = models.TextField(validators=[URLValidator()], null=True)
    motivation = models.TextField(null=True)
    agreement = models.TextField(validators=[URLValidator()], null=True)
    sweater_size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    want_to_say = models.TextField(null=True, blank=True)
    phase = models.CharField(max_length=512, null=True, choices=PHASE_CHOICES, blank=True)
    accept = models.BooleanField(default=False)
    reviewers = models.ManyToManyField(User, through='Review', through_fields=('applicant', 'user'), related_name='reviewers')
    avg_score = models.FloatField(default=0)

    def __str__(self):
        return self.name

    

class Review(models.Model):
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.applicant.name

