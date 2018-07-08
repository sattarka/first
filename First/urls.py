


from django.urls import path
from . import views

urlpatterns = [
    path('',views.first),
    path('countsss',views.count,name='count'),

]
