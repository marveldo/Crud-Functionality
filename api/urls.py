from django.urls import path
from .views import Createuser,Getprofile
urlpatterns = [
    path('', Createuser),
    path('/<int:pk>',Getprofile),
]