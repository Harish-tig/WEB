from django.urls import path
from . import views

urlpatterns = [

    path('',views.scrape_function,name="head_function"),
    path('inovation/',views.inovation,name="inovation"),
    path('sports',views.sports,name="sports"),
    path('business/',views.business,name="business"),
    path('culture/',views.culture,name="culture")
]
