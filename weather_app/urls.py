from django.urls import path
from weather_app.views import *
urlpatterns = [

    path('', index, name='index'),

]

