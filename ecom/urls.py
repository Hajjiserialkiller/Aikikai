from django.urls import path
from ecom import views
from .views import video_list, onset

app_name = 'ecom'

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', video_list, name='videos'),
    path('onset/', onset,name='onset'),
]


