from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('footballtips/', views.AllTipsListView.as_view(), name='alltips'),
    path('favouritetips/', views.BestTipsListView.as_view(), name='besttips'),
    path('livescore/', views.LiveListView, name='livescore'),
    path('contact/', views.contact, name='contact'),
]