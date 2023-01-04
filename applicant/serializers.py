from rest_framework import serializers
from . import models
class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Applicant
        fields = [
            "id",
            "register_time",
            "email",
            "name",
            "id_number",
            "birthday",
            "sex",
            "telephone",
            "parent_phone",
            "self_phone", 
            "emergency_name",
            "address",
            "emerge_phone",
            "school",
            "major",
            "club",
            "special_dietary",
            "special_disease",
            "facebook",
            "group_apply",
            "group_person1",
            "group_person2",
            "group_person3",
            "self_introduction",
            "picture",
            "motivation",
            "agreement",
            "sweater_size",
            "want_to_say",
            "phase",
            "accept",
            "reviewers",
            "avg_score"
        ]

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ["score","applicant","user"]
