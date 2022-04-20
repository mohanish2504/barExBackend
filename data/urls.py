from django.urls import path
from . import views

data_urlpatterns = [
    path('enquiry',views.enquiry,name="enquiry")
]
