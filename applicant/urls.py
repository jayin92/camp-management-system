from django.urls import path
from . import views

urlpatterns = [    
    path('api',views.ApplicantListApiView.as_view()),
    path('api/<int:applicant_id>',views.ApplicantDetailApiView.as_view()),
    path('review/api',views.ReviewsListApiView.as_view())
]